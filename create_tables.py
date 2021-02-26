#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Use of this source code is governed by a BSD-style
# license that can be found in the LICENSE file.
# Copyright 2019 The fiowebviewer Authors. All rights reserved.

import argparse

from sqlalchemy import (
    create_engine,
)

from fiowebviewer.engine.run import (
    fio_webviewer,
)
from fiowebviewer.engine import (
    database,
)

databaseName = fio_webviewer.config["DATABASE_NAME"]
databaseHost = fio_webviewer.config["DATABASE_HOST"]
databaseUser = fio_webviewer.config["DATABASE_USER"]
databasePassword = fio_webviewer.config["DATABASE_PASSWORD"]

engine = create_engine(f"mysql+pymysql://{databaseUser}:{databasePassword}@{databaseHost}/{databaseName}?charset=utf8mb4")

parser = argparse.ArgumentParser()
parser.add_argument('--drop', help='drop existing tables', action='store_true',
                    default=False)

args = parser.parse_args()

if args.drop:
    database.Base.metadata.drop_all(engine)
database.Base.metadata.create_all(engine)
