# -*- coding: utf-8 -*-
import os
import sys
import json
import re
import csv
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

from pyramid.paster import bootstrap

from kotti.resources import get_root
from kotti import DBSession
from kotti.resources import Document
from kotti.security import USER_MANAGEMENT_ROLES

import sqlalchemy.orm.exc

import funcs
import manage_users
from kotti_toolkit import util


def abort_if_false(ctx, param, value):
    if not value:
        ctx.abort()


@click.command()
@click.argument('config_file', type=click.Path('r'))
@click.option('--yes', is_flag=True, callback=abort_if_false,
              help="Skip the prompt message and proceed with dropping and create a new site",
              expose_value=False,
              prompt='This will erase all pervious data, are you sure you want to create a new site?')
def new_site(config_file, login, **kwargs):
    """ Create a new site from scratch.

    Executing this command will drop and recreate the database for this application.

    Args:
        config_file (str):      Path to the configuration ini file for the site.

    """
    start_time = time.time()
    login_url, dbname = funcs.get_login_url_db(config_file=config_file)
    print 'using the following database url: {}'.format(login_url)
    if login:
        subprocess.call(["psql", login_url, "-c",
                         "drop database if exists {};".format(dbname)])
        subprocess.call(["psql", login_url, "-c",
                         "create database {};".format(dbname)])
    else:
        subprocess.call(["dropdb","--if-exists","{}".format(dbname)])
        subprocess.call(["createdb", "{}".format(dbname)])
    print "{} to build a new site.".format(funcs.get_end_time(start_time))


##############################################################################
# USER MANAGEMENT
##############################################################################
@click.command()
@click.argument('config_file', type=click.Path('r'))
@click.argument('username')
@click.option('--title', help="Firstname and Lastname", default="DPK User")
@click.option('--password', help="Password", default="dpk2016dev")
@click.option('--email', help="Email", default="kotti@example.com")
@click.option('--roles', help="User roles",
              type=click.Choice(USER_MANAGEMENT_ROLES), multiple=True)
@click.version_option(version='0.1.0')
def create_user(**kwargs):
    manage_users.create_user(close_pyramid_env=True, **kwargs)
