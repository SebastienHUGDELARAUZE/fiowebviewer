.PHONY: all sdist develop bdist_wheel git_hooks requirements requirements_to_wheels

all: bdist_wheel

PY_ENV_PATH=/usr/bin
PYTHON=$(PY_ENV_PATH)/python
PIP=$(PY_ENV_PATH)/pip

LIB := lib

### initialization ###

requirements: requirements.txt
	$(PIP) install -r requirements.txt

requirements-dev: requirements-dev.txt
	$(PIP) install -r requirements-dev.txt

create_tables:
	$(PYTHON) create_tables.py

### develop ###

develop: requirements requirements-dev git_hooks
	$(PYTHON) setup.py develop

git_hooks:
	@if ! [[ -L .git/hooks/pre-commit ]]; then \
        echo "Installing git pre-commit hook"; \
        ln -fs ../../git/pre-commit .git/hooks/pre-commit; \
    fi

### wheel / dist ###

sdist:
	$(PYTHON) setup.py sdist

requirements_to_wheels:
	$(PIP) wheel -r requirements.txt

bdist_wheel:
	# Mocking environment to enable creating wheel
	# without exporting environment variables
	TMP=$$(mktemp -d --suffix .fio-wheel-build) ;\
	echo $$TMP ;\
	mkdir -p "$$TMP/data" ;\
	mkdir -p "$$TMP/cache" ;\
	mkdir -p "$$TMP/log" ;\
	echo "DATA_PATH = \"$$TMP/data\"" >> "$$TMP/config.cfg" ;\
	echo "ERROR_LOG = \"$$TMP/log/error.log\"" >> "$$TMP/config.cfg" ;\
	echo "CACHE_PATH = \"$$TMP/cache\"" >> "$$TMP/config.cfg" ;\
	echo "DATABASE = \"sqlite:///$$TMP/data/database.db\"" >> "$$TMP/config.cfg" ;\
	export FIOWEBVIEWER_SETTINGS="$$TMP/config.cfg" ;\
	$(PYTHON) setup.py bdist_wheel --universal ;\
	rm -rf "$$TMP"
