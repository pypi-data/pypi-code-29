from __future__ import print_function
from builtins import next
from copy import deepcopy
import itertools
from collections import defaultdict

from sqlalchemy.orm import class_mapper, undefer, with_polymorphic
from sqlalchemy.orm.session import make_transient
from sqlalchemy.orm.properties import ColumnProperty

from ..models import DiscussionBoundBase, Discussion, AgentProfile, Webpage, Permission, Role#, Widget, IdeaWidgetLink
from assembl.lib.sqla import class_registry

no_traverse = (AgentProfile, Webpage, Permission, Role)#, Widget, IdeaWidgetLink)
early_relations = {
    Discussion.__class__: {
        Discussion.root_idea.property,
        Discussion.table_of_contents.property}
}

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

class_info = {}

def get_mapper_info(mapper):
    if mapper not in class_info:
        pk_keys_cols = set([c for c in mapper.primary_key])
        direct_reln = {r for r in mapper.relationships
                       if r.direction.name == 'MANYTOONE'}
        direct_reln_cols = set(itertools.chain(
            *[r.local_columns for r in direct_reln]))
        avoid_columns = pk_keys_cols.union(direct_reln_cols)
        copy_col_props = {a for a in mapper.iterate_properties
                          if isinstance(a, ColumnProperty)
                          and not avoid_columns.intersection(set(a.columns))}

        non_nullable_reln = {r for r in direct_reln
            if any([not c.nullable for c in r.local_columns])}
        nullable_relns = direct_reln - non_nullable_reln
        class_info[mapper] = (direct_reln, copy_col_props, nullable_relns, non_nullable_reln)
    return class_info[mapper]

def recursive_clone(from_session, to_session, ob, excludeClasses=None, copies_of=None, copies=None, promises=None, in_process=None, changes=None):
    copies_of = copies_of or {}
    if ob in copies_of:
        return copies_of[ob]
    copies = copies or set()
    if ob in copies:
        return ob
    in_process = in_process or set()
    if ob in in_process:
        return None
    excludeClasses = excludeClasses or ()
    if isinstance(ob, excludeClasses):
        copies_of[ob] = ob
        return ob
    promises = promises or defaultdict(list)
    mapper = class_mapper(ob.__class__)
    (direct_reln, copy_col_props, nullable_relns, non_nullable_reln) = get_mapper_info(mapper)
    values = {r.key: getattr(ob, r.key, None) for r in copy_col_props}

    print("->", ob.__class__, ob.id)
    in_process.add(ob)
    for r in non_nullable_reln:
        subob = getattr(ob, r.key, None)
        assert subob is not None
        assert subob not in in_process
        print('recurse ^0', r.key)
        result = recursive_clone(from_session, to_session, subob, excludeClasses, copies_of, copies, promises, in_process, changes)
        assert result is not None
        assert result.id
        print('result', result.__class__, result.id)
        values[r.key] = result
    local_promises = {}
    for r in nullable_relns:
        subob = getattr(ob, r.key, None)
        if subob is not None:
            if subob in copies_of:
                values[r.key] = copies_of[subob]
            else:
                local_promises[r] = subob
    values.update(changes[ob])
    if ob.__class__ == Discussion:
        values['next_synthesis'] = None
        values['root_idea'] = None
        values['table_of_contents'] = None
    copy = ob.__class__(**values)
    to_session.add(copy)
    to_session.flush()
    print("<-", ob.__class__, ob.id, copy.id)
    copies_of[ob] = copy
    copies.add(copy)
    in_process.remove(ob)
    if ob in promises:
        for (o, r) in promises[ob]:
            print('fullfilling', o.__class__, o.id, r.key)
            setattr(o, r.key, copy)
        del promises[ob]
    for reln, subob in list(local_promises.items()):
        if subob in in_process:
            promises[subob].append((copy, reln))
        else:
            print('key', r.key)
            result = recursive_clone(from_session, to_session, subob, excludeClasses, copies_of, copies, promises, in_process, changes)
            if result is None:  # in process
                print("promising", subob.__class__, subob.id, reln.key)
                promises[subob].append((copy, reln))
            else:
                print("delayed", key, result.__class__, result.id)
                setattr(copy, key, result)
    # exceptions
    if isinstance(ob, Discussion):
        recursive_clone(from_session, to_session, ob.root_idea, excludeClasses, copies_of, copies, promises, in_process, changes)
        # recursive_clone(from_session, to_session, ob.table_of_contents, excludeClasses, copies_of, copies, promises, in_process, changes)
        # recursive_clone(from_session, to_session, ob.synthesis, excludeClasses, copies_of, copies, promises, in_process, changes)
    for r in mapper.relationships:
        if r in direct_reln:
            continue
        print('key', r.key)
        subobs = getattr(ob, r.key)
        if subobs is None:
            continue
        if not isinstance(subobs, list):
            subobs = [subobs]
        for subob in subobs:
            print('recurse 0', r.key)
            recursive_clone(from_session, to_session, subob, excludeClasses, copies_of, copies, promises, in_process, changes)
    return copy

def assign_dict(values, r, subob):
    assert r.direction.name == 'MANYTOONE'
    values[r.key] = subob
    for col in r.local_columns:
        fkcol = next(iter(col.foreign_keys)).column
        k = next(iter(r.local_columns))
        values[col.key] = getattr(subob, fkcol.key)

def assign_ob(ob, r, subob):
    assert r.direction.name == 'MANYTOONE'
    setattr(ob, r.key, subob)
    for col in r.local_columns:
        fkcol = next(iter(col.foreign_keys)).column
        k = next(iter(r.local_columns))
        setattr(ob, col.key, getattr(subob, fkcol.key))

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
    #recursive_fetch(discussion)
    changes = defaultdict(dict)
    if to_session is None:
        to_session = from_session
        changes[discussion]['slug'] = new_slug or (discussion.slug + "_copy")
    else:
        changes[discussion]['slug'] = new_slug or discussion.slug
    excludeClasses = no_traverse
    copies_of = {}
    copies = set()
    in_process = set()
    promises = defaultdict(list)

    def resolve_promises(ob, copy):
        if ob in promises:
            for (o, reln) in promises[ob]:
                print('fullfilling', o.__class__, o.id, k)
                assign_ob(o, reln, copy)
            del promises[ob]

    def recursive_clone(ob):
        if ob in copies_of:
            return copies_of[ob]
        if ob in copies:
            return ob
        if ob in in_process:
            print("in process", ob.__class__, ob.id)
            return None
        if isinstance(ob, excludeClasses):
            copies_of[ob] = ob
            return ob
        if isinstance(ob, DiscussionBoundBase):
            assert discussion_id == ob.get_discussion_id()

        mapper = class_mapper(ob.__class__)
        (direct_reln, copy_col_props, nullable_relns, non_nullable_reln) = get_mapper_info(mapper)
        values = {r.key: getattr(ob, r.key, None) for r in copy_col_props}

        print("->", ob.__class__, ob.id)
        in_process.add(ob)
        for r in non_nullable_reln:
            subob = getattr(ob, r.key, None)
            assert subob is not None
            assert subob not in in_process
            print('recurse ^0', r.key)
            result = recursive_clone(subob)
            assert result is not None
            assert result.id
            print('result', result.__class__, result.id)
            assign_dict(values, r, result)
        local_promises = {}
        for r in nullable_relns:
            subob = getattr(ob, r.key, None)
            if subob is not None:
                if subob in copies_of:
                    assign_dict(values, r, copies_of[subob])
                else:
                    local_promises[r] = subob
        values.update(changes[ob])
        copy = ob.__class__(**values)
        to_session.add(copy)
        to_session.flush()
        print("<-", ob.__class__, ob.id, copy.id)
        copies_of[ob] = copy
        copies.add(copy)
        in_process.remove(ob)
        resolve_promises(ob, copy)
        for reln, subob in list(local_promises.items()):
            if subob in in_process:
                promises[subob].append((copy, reln))
            else:
                print('recurse 0', reln.key)
                result = recursive_clone(subob)
                if result is None:  # in process
                    print("promising", subob.__class__, subob.id, reln.key)
                    promises[subob].append((copy, reln))
                else:
                    print("delayed", reln.key, result.__class__, result.id)
                    assign_ob(copy, reln, result)
        return copy

    treating = set()
    def stage_2_rec_clone(ob):
        if ob in treating:
            return
        if isinstance(ob, excludeClasses):
            return
        print("treating", ob.__class__, ob.id)
        treating.add(ob)
        if ob in copies_of:
            copy = copies_of[ob]
        elif ob in copies:
            copy = ob
        else:
            copy = recursive_clone(ob)
            resolve_promises(ob, copy)
        treating.add(copy)
        mapper = class_mapper(ob.__class__)
        (direct_reln, copy_col_props, nullable_relns, non_nullable_reln) = get_mapper_info(mapper)
        for r in mapper.relationships:
            if r in direct_reln:
                continue
            subobs = getattr(ob, r.key)
            if subobs is None:
                continue
            if not isinstance(subobs, list):
                subobs = [subobs]
            for subob in subobs:
                stage_2_rec_clone(subob)

    recursive_clone(discussion)
    stage_2_rec_clone(discussion)
    #excludeClasses = (User, AgentProfile) if to_session == from_session else []
    #recursive_transient(from_session, to_session, discussion, no_traverse)
    #to_session.add(discussion)
    #to_session.flush()
