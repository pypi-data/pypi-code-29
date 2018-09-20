from datetime import datetime
from kotti import DBSession
from kotti.security import has_permission, set_groups
from kotti.security import Principal
from kotti.resources import get_root, Document
from kotti.util import title_to_name
from kotti_controlpanel.util import get_setting
from kotti_toolkit.security import (
    create_group,
    find_groups_by_email_domain,
    is_group
)
from sqlalchemy.exc import IntegrityError

from kotti_group_manager import _


def create_groups_listing_page():
    root = get_root()
    container_name = "_ug"
    if container_name not in root:
        listing_page = root[container_name] = Document(
            name=container_name,
            title=_('Groups'),
            description=_('List groups'),
            creation_date=datetime.now(),
            modification_date=datetime.now()
        )
        return listing_page
    return root[container_name]


def set_group_page_permission(group_page, group_name):
    set_groups(group_name, group_page, set(["role:viewer", group_name]))
    

def create_group_page_from_group(group):
    from kotti_group_manager.resources import GroupPage
    root = create_groups_listing_page()
    group_name = group.name.replace("group:", '')
    if group_name in root:
        return None
    group_page = root[group_name] = GroupPage(
        title=group.title,
        group_name=group.name,
        creation_date=datetime.now(),
        modification_date=datetime.now()
    )
    set_group_page_permission(group_page, group.name)
    return group_page


def create_group_from_user_email_domain(user):
    if is_group(user):
        return
    email_domain_as_group = get_setting('email_domain_as_group', default=False)
    if not email_domain_as_group:
        return
    try:
        if not user.email:
            raise ValueError('No email found for {}'.format(user.id))
        eparts = user.email.split("@")
        if len(eparts) != 2:
            raise ValueError('Invalid email found for {}'.format(user.id))
        email_domain = eparts[-1]
        blacklisted_domains = get_setting('domains', default=[])
        if email_domain in blacklisted_domains:
            raise ValueError(
                'Email domain for {} is black listed'.format(user.email)
            )
        group = find_groups_by_email_domain(email_domain, limit=1).first()
        if not group:
            group_title = email_domain.split(".")[0].capitalize()
            group_name = title_to_name(group_title)
            group = create_group(
                title=group_title,
                email="groupinfo@{}".format(email_domain),
                name=group_name
            )
            if group is False:
                raise ValueError(
                    "Group {} was not created".format(group_title)
                )
        else:
            group_name = group.name.replace("group:", "")
        user_groups = user.groups
        user_groups.append('group:{}'.format(group_name))
        user.groups = user_groups
        DBSession.add(user)
    except ValueError as e:
        print e
        group = None
        
    if not group:
        return
    group_as_content = get_setting('group_as_content', default=False)
    if not group_as_content:
        return
    group_page = create_group_page_from_group(group)
    if group_page is not None:
        set_groups(user.name, group_page, set(["role:owner"]))
    


