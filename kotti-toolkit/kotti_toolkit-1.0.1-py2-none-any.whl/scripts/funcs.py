# -*- coding: utf-8 -*-
import os
import sys
import json
import re
import uuid
import time
import operator
import random
import transaction
import progress.bar
import gzip
import zipfile
import ConfigParser
import subprocess
import csv
import difflib
import unicodecsv
from datetime import datetime, timedelta

from glob import glob
from pyramid.paster import bootstrap

from kotti.resources import get_root
from kotti import DBSession
from kotti.resources import Document, Tag, TagsToContents
from kotti.security import get_principals
from kotti.security import set_groups, Principal as User
from kotti.security import principals_with_local_roles
from kotti.events import UserDeleted

import sqlalchemy.orm.exc
from kotti_toolkit import util
from kotti_toolkit.security import create_group, create_user

def get_sql_url(config_file):
    """Returns the sql url from the configuration ini file"""
    config = ConfigParser.ConfigParser()
    config.readfp(open(config_file))
    return config.get('app:kotti', 'sqlalchemy.url', 1)


def get_login_url_db(sql_url=None, config_file=None):
    """ Returns the sql login url and database name from
        the configuration ini file or sql url.
    """
    if not sql_url:
        sql_url = get_sql_url(config_file)
    dbname_index = sql_url.rfind("/")
    dbname = sql_url[dbname_index+1:]
    login_url = sql_url[0:dbname_index]
    if '@' not in sql_url:
        login_url = sql_url
        dbname = sql_url.split('//')[1]
    if "?" in dbname:
        dbname = dbname[:dbname.index("?")]
    return login_url, dbname


def get_user_from_login_url(login_url):
    return login_url.replace("postgres://", '').split(':')[0]


def get_end_time(s_time):
    m, s = divmod(int(time.time() - s_time), 60)
    h, m = divmod(m, 60)
    return "It took %d hr(s) : %02d mins : %02d seconds" % (h, m, s)


def print_seperator():
    print "-" * 70
