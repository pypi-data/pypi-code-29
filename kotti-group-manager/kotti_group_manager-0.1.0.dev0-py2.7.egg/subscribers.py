from kotti import DBSession
from kotti.events import subscribe
from kotti.events import ObjectInsert
from kotti.events import ObjectUpdate
from kotti.events import ObjectDelete
from kotti.security import has_permission, set_groups
from kotti.security import Principal
from kotti.util import title_to_name
from kotti_controlpanel.util import get_setting
from kotti_toolkit.security import (
    create_group,
    find_groups_by_email_domain
)
from sqlalchemy.exc import IntegrityError


@subscribe(ObjectInsert, Principal)
def new_user_handler(event):
    try:
        user = event.object
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
            group = create_group(
                title=group_title,
                email="groupinfo@{}".format(email_domain),
                name=title_to_name(group_title)
            )
            if group is False:
                raise ValueError(
                    "Group {} was not created".format(group_title)
                )
        user_groups = user.groups
        user_groups.append(group.name)
        user.groups = user_groups
        DBSession.add(user)
    except Exception as e:
        print e