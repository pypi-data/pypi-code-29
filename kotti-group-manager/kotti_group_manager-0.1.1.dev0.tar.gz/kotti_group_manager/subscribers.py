from kotti import DBSession
from kotti.events import subscribe
from kotti.events import ObjectInsert
# from kotti.events import ObjectUpdate
# from kotti.events import ObjectDelete
# from kotti.security import has_permission, set_groups
from kotti.security import Principal
from sqlalchemy.exc import IntegrityError

from kotti_group_manager.resources import GroupPage
from kotti_group_manager.security import (
    create_group_from_user_email_domain,
    set_group_page_permission
)


@subscribe(ObjectInsert, Principal)
def new_user_handler(event):
    user = event.object
    create_group_from_user_email_domain(user)


@subscribe(ObjectInsert, GroupPage)
def update_group_page_permission_handler(event):
    group_page = event.object
    set_group_page_permission(group_page, group_page.group_name)
    
