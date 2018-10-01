from __future__ import print_function
from copy import deepcopy

from sqlalchemy.orm import class_mapper, undefer, with_polymorphic
from sqlalchemy.orm.session import make_transient

from ..models import DiscussionBoundBase, Discussion, AgentProfile, Webpage, Permission, Role#, Widget, IdeaWidgetLink
from assembl.lib.sqla import class_registry

no_traverse = (AgentProfile, Webpage, Permission, Role)#, Widget, IdeaWidgetLink)


def print_path(path):
    try:
        print(path)
    except Exception as e:
        print("error", [(x, y.__class__) for (x,y) in path])


def recursive_fetch(ob, visited=None):
    visited = visited or {ob}
    # path = path or [('', ob)]
    # print "fetch",
    # print_path(path)
    mapper = class_mapper(ob.__class__)

    for attr in mapper.iterate_properties:
        if getattr(attr, 'deferred', False):
            getattr(ob, attr.key)
    for reln in mapper.relationships:
        subobs = getattr(ob, reln.key)
        if not subobs:
            continue
        if not isinstance(subobs, list):
            subobs = [subobs]
        for subob in subobs:
            if subob in visited:
                continue
            visited.add(subob)
            if isinstance(subob, no_traverse):
                continue
            recursive_fetch(subob, visited)
            #, path + [(reln.key, subob)], visited)

def recursive_transient(from_session, to_session, ob, excludeClasses = None):
    excludeClasses = excludeClasses or ()
    if isinstance(ob, excludeClasses):
        return
    # path = path or [('', ob)]
    mapper = class_mapper(ob.__class__)
    pk_keys = set([c.key for c in mapper.primary_key])

    if any([getattr(ob, key) for key in pk_keys]):
        # print "transient",
        # print_path(path)
        if isinstance(ob, excludeClasses):
            return
        make_transient(ob)
        values = []
        # ob.db.expire(ob, pk_keys)
        for k in pk_keys:
            setattr(ob, k, None)
        for reln in mapper.relationships:
            if isinstance(reln.mapper.class_, excludeClasses):
                continue
            subobs = getattr(ob, reln.key)
            if not subobs:
                continue
            if not isinstance(subobs, list):
                if reln.direction.name == 'MANYTOONE':
                    values.append((reln.key, subobs))
                    #ob.db.expire(ob, [c.key for c in reln.local_columns])
                    for c in reln.local_columns:
                        setattr(ob, c.key, None)
                    setattr(ob, c.key, None)
                subobs = [subobs]
            for subob in subobs:
                if isinstance(subob, excludeClasses):
                    continue
                recursive_transient(from_session, to_session, subob, excludeClasses)
                #, path + [(reln.key, subob)])
        for (k, v) in values:
            setattr(ob, k, v)


def prefetch(session, discussion_id):
    for name, cls in list(class_registry.items()):
        if issubclass(cls, DiscussionBoundBase) and cls != DiscussionBoundBase:
            mapper = class_mapper(cls)
            undefers = [undefer(attr.key) for attr in mapper.iterate_properties
                        if getattr(attr, 'deferred', False)]
            condition = cls.get_discussion_condition(discussion_id)
            session.query(with_polymorphic(cls, "*")).filter(condition).options(*undefers).all()


def clone_discussion(from_session, discussion_id, to_session=None, new_slug=None):
    discussion = Discussion.get(discussion_id)
    prefetch(from_session, discussion_id)
    recursive_fetch(discussion)
    if to_session is None:
        to_session = from_session
        discussion.slug = new_slug or (discussion.slug + "_copy")
    else:
        discussion.slug = new_slug or discussion.slug
    #excludeClasses = (User, AgentProfile) if to_session == from_session else []
    recursive_transient(from_session, to_session, discussion, no_traverse)
    to_session.add(discussion)
    to_session.flush()
