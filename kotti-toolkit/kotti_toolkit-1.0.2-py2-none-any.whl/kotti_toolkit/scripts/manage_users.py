# -*- coding: utf-8 -*-
import os
import csv
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
import click
import ConfigParser
import subprocess

from datetime import datetime
from pyramid.paster import bootstrap

from kotti.resources import get_root
from kotti import DBSession
from kotti.resources import Document
from kotti.security import get_principals
from kotti.security import set_groups
from kotti.security import principals_with_local_roles
from kotti.events import UserDeleted

import sqlalchemy.orm.exc
from sqlalchemy import func, over
from kotti.security import ROLES
from kotti.security import SHARING_ROLES
from kotti.security import USER_MANAGEMENT_ROLES

from funcs import get_end_time, print_seperator

from kotti_toolkit.util import slugify
from kotti_toolkit.security import Principal


def create_user(config_file, username, title, password,
                email, roles=[], groups=[], registered=False,
                pyramid_env=None, close_pyramid_env=False):
    """Create Kotti user or principal."""
    if not pyramid_env:
        pyramid_env = bootstrap(config_file)
    start_time = time.time()
    with transaction.manager:
        if roles:
            groups = roles
        principals = get_principals()
        principal = principals.search(name=username, email=email).first()
        print principal
        if principal:
            print "username or email already exists in the database"
            return
        user = Principal(username, title=title, email=email,
                         active=True, password=password, groups=list(groups))
        principals[user.id] = user
    print "%s to create a user" % get_end_time(start_time)
    if close_pyramid_env:
        pyramid_env['closer']()


def create_group(config_file, group_name,
                 title=None, email="merle@dpk.com", groups=[],
                 pyramid_env=None, close_pyramid_env=False):
    """Create Kotti user group."""
    if not pyramid_env:
        pyramid_env = bootstrap(config_file)
    start_time = time.time()
    with transaction.manager:
        principals = get_principals()
        if not title:
            title = group_name
        group_name = "group:%s" % group_name
        principal = principals.search(name=group_name, email=email).first()
        if not principal:
            group = Principal(name=group_name, title=title, email=email,
                              active=True, groups=groups)
            principals[group.id] = group
            print " Created %s" % group_name
            print " %s to create a group" % get_end_time(start_time)
    if close_pyramid_env:
        pyramid_env['closer']()


def delete_users(config_file, pyramid_env=None, close_pyramid_env=False):
    """Delete all users except admin users"""
    start_time = time.time()
    count = 0
    if not pyramid_env:
        pyramid_env = bootstrap(config_file)
    with transaction.manager:
        principals = get_principals()
        for principal in principals.search(match="any", active=True).all():
            if((principal.name != "admin" or
               "role:admin" not in principal.groups) and
               not principal.name.startswith("group")):
                principals.__delitem__(principal.name)
                UserDeleted(principal)
                print " %s Deleted" % principal.name
                count += 1
    pyramid_env['closer']()
    print "{} to delete all non-admin users, i.e. {} users".format(
        get_end_time(start_time),
        count
    )
    if close_pyramid_env:
        pyramid_env['closer']()