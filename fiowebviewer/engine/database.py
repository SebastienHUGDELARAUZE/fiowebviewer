# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
# Copyright 2019 The fiowebviewer Authors. All rights reserved.

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    create_engine,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import (
    relationship,
    sessionmaker,
)
from sqlalchemy.schema import ForeignKey

from fiowebviewer.engine.run import fio_webviewer

databaseName = fio_webviewer.config["DATABASE_NAME"]
databaseHost = fio_webviewer.config["DATABASE_HOST"]
databaseUser = fio_webviewer.config["DATABASE_USER"]
databasePassword = fio_webviewer.config["DATABASE_PASSWORD"]

engine = create_engine(
    f"mysql+pymysql://{databaseUser}:{databasePassword}@{databaseHost}/{databaseName}?charset=utf8mb4")
Base = declarative_base()
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)


class FioOutput(Base):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    date_submitted = Column(DateTime, nullable=False)

    # Information
    name = Column(String(64), nullable=True)
    hostname = Column(String(64), nullable=True)
    fio_version = Column(String(32), nullable=True)
    timestamp = Column(Integer, nullable=True)
    timestamp_ms = Column(Integer, nullable=True)
    time = Column(DateTime, nullable=True)

    # Global options

    # Read:
    #  -

    def __repr__(self):
        return self.date_submitted


class Tag(Base):
    __tablename__ = 'tags'
    id = Column(Integer, primary_key=True)
    tag = Column(String(128), nullable=False)
    result_id = Column(Integer, ForeignKey("data.id"), nullable=False)
    result = relationship(FioOutput)

    def __repr__(self):
        return self.tag
