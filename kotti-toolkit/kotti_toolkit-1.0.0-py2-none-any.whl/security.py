
from kotti import DBSession
from kotti.security import Principal
from kotti.security import Principals, get_principals, set_groups
from kotti.util import title_to_name
from sqlalchemy.ext.declarative import declared_attr, declarative_base
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import (
    Column, ForeignKey, Integer, Unicode,
    Float, Boolean, Date, String
)
from sqlalchemy.orm import (
    relationship, backref
)
from sqlalchemy.dialects.postgresql import UUID
from kotti_toolkit import _
from kotti_toolkit.util import merge_list, slugify


def is_user(principal):
    return not principal.name.startswith("group:")


def is_group(principal):
    return principal.name.startswith("group:")


def create_user(username, title, password,
                email, roles=[], groups=[], active=True):
    """ Create an user account.

    :param username:    Username for the acction
    :param title:       Full name of the user.
    :param password:    Password for the account.
    :param email:       Email address for the account.
    :param roles:       Permissions and roles for the account, e.g. ['role:admin'].
    :param groups:      Groups which this group may belong to, e.g. ['group:edpm_2017'].
    :param active:      Set to True to active the user, else False. The default is True.
    :returns:           True if the user was created successfully, else False.
    """
    principals = get_principals()
    principal = principals.search(name=username, email=email).first()
    if principal:
        return None
    groups = merge_list(groups, roles)
    user = Principal(username, title=title, email=email,
                     active=active, password=password, groups=groups)
    principals[user.id] = user
    return user


def find_group(name):
    """ Find group

    :param name:        Group name.
    :returns:           The Principal object fot the group.
    """
    if not name.startswith("group:"):
        name = "group:{}".format(name)
    principals = get_principals()
    return principals.search(name=name).first()

def _find_principal_by_email_domain(email_domain):
    query = Principal.query
    pattern = "(@{})".format(email_domain)
    return query.filter(Principal.email.op('~')(pattern))

    
def find_users_by_email_domain(email_domain, limit=100):
    query = _find_principal_by_email_domain(email_domain)
    query = query.filter(Principal.name.contains("group:") == False)
    return query.limit(limit)


def find_groups_by_email_domain(email_domain, limit=100):
    query = _find_principal_by_email_domain(email_domain)
    query = query.filter(Principal.name.contains("group:") == True)
    return query.limit(limit)


def create_group(title, email, name="", groups=[], roles=[]):
    """ Create an user group.

    :param name:        ID of the group, should not contain any space.
    :param title:       Title/name of the group.
    :param email:       Email address of the group.
    :param roles:       Permissions and roles for the group, e.g. ['role:admin'].
    :param groups:      Parent groups which this group may belong to, e.g. ['group:edpm_2017'].
    :returns:           True if the group was created successfully, else False.
    """
    principals = get_principals()
    if not name:
        name = title_to_name(title)
    if not name.startswith("group:"):
        name = "group:{}".format(name)
    principal = principals.search(name=name, email=email).first()
    if not principal:
        groups = merge_list(groups, roles)
        group = Principal(name=name, title=title, email=email,
                     active=True, groups=groups)
        principals[group.id] = group
        # DBSession.add(group)
        return group
    return None
