import click
import configparser
from helper import *
from query import *
from analytics import *
import os
configInstance = configparser.ConfigParser()
configInstance.read('grank.ini')


if not os.path.exists('result'):
    os.makedirs('result')

if not os.path.exists('output'):
    os.makedirs('output')

@click.group()
def cli():
    pass

@cli.command()
@click.option('--token', prompt=True,help="Your Github Personal Token")
@click.option('--keyword', prompt=True,help="The Corp Keyword")
def config(token,keyword):
    """Grank Settings"""
    configInstance["login"] = {}
    configInstance["login"]["token"]=token
    configInstance["corp"] = {}
    configInstance["corp"]["keyword"]=keyword
    configInstance["time"] = {}
    configInstance["time"]["start_time"]='2017-01-01'
    configInstance["time"]["end_time"]='2018-09-24'
    configInstance["rank"] = {}
    configInstance["top"] = 3
    with open('grank.ini', 'w') as configfile:
        configInstance.write(configfile)

@cli.command()
def login():
    """Who am I"""
    if is_login():
        result = run(login_query)
        username = result["data"]["viewer"]["login"]
        click.echo('Your Username is  %s' % username);
        pass



@cli.command()
@click.option('--owner', prompt=True)
@click.option('--repository', prompt=True)
def analytics(owner,repository):
    """Analytics a repo"""
    analytics_repo(owner,repository)
    pass

