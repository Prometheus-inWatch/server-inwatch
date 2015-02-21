# -*- coding: utf-8 -*-
import os

BDNAME=os.environ['BDNAME']
BDHOST=os.environ['OPENSHIFT_MYSQL_DB_HOST']#+':'+os.environ['OPENSHIFT_MYSQL_DB_PORT']
BDPASS=os.environ['OPENSHIFT_MYSQL_DB_PASSWORD']
BDUSER=os.environ['OPENSHIFT_MYSQL_DB_USERNAME']
