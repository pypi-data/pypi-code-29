# -*- coding: utf-8 -*-

from itertools import chain, groupby
from collections import defaultdict
from abc import ABCMeta, abstractmethod
from datetime import datetime

from rdflib import URIRef
from sqlalchemy.orm import (
    relationship, backref, aliased, contains_eager, joinedload, deferred,
    column_property, with_polymorphic)
from sqlalchemy.orm.attributes import NO_VALUE
from sqlalchemy.sql import text, column
from sqlalchemy.sql.expression import union_all, bindparam, literal_column

from sqlalchemy import (
    Column,
    Boolean,
    Integer,
    String,
    Unicode,
    Float,
    UnicodeText,
    DateTime,
    ForeignKey,
    inspect,
    select,
    func,
)
from sqlalchemy.ext.associationproxy import association_proxy
from ..semantic import IriClass, PatternIriClass
from virtuoso.alchemy import SparqlClause

from . import DiscussionBoundBase, HistoryMixin
from .discussion import Discussion
from ..semantic import (
    QuadMapPatternS, AppQuadStorageManager)
from ..semantic.namespaces import (
    SIOC, IDEA, ASSEMBL, DCTERMS, QUADNAMES, FOAF, RDF, VirtRDF)


class Idea(Base):
    def idea_read_counts_sparql(cls, discussion_id, post_id, user_id):
        """Given a post and a user, give the total and read count
         of posts for each affected idea
        This one is slower than the sql version below."""
        from .auth import AgentProfile
        local_uri = AppQuadStorageManager.local_uri()
        discussion_storage = \
            AppQuadStorageManager.discussion_storage_name()
        idea_ids = cls.get_idea_ids_showing_post(post_id)
        user_uri = URIRef(AgentProfile.uri_generic(user_id, local_uri)).n3()
        results = []
        for idea_id in idea_ids:
            ((read,),) = list(cls.default_db.execute(SparqlClause(
            """select count(distinct ?change) where {
            %s idea:includes* ?ideaP .
            ?postP assembl:postLinkedToIdea ?ideaP .
            ?post sioc:reply_of* ?postP .
            ?change a version:ReadStatusChange;
                version:who %s ;
                version:what ?post }""" % (
                URIRef(Idea.uri_generic(idea_id, local_uri)).n3(),
                user_uri), quad_storage=discussion_storage.n3())))
            results.append((idea_id, read))
        return results

    def get_synthesis_contributors(self, id_only=True):
        # author of important extracts
        from .idea_content_link import Extract
        from .auth import AgentProfile
        from .post import Post
        from sqlalchemy.sql.functions import count
        local_uri = AppQuadStorageManager.local_uri()
        discussion_storage = \
            AppQuadStorageManager.discussion_storage_name()

        idea_uri = URIRef(self.uri(local_uri))
        clause = '''select distinct ?annotation where {
            %s idea:includes* ?ideaP .
            ?annotation assembl:resourceExpressesIdea ?ideaP }'''
        extract_ids = [x for (x,) in self.db.execute(
            SparqlClause(clause % (
                idea_uri.n3(),),
                quad_storage=discussion_storage.n3()))]
        r = list(self.db.query(AgentProfile.id, count(Extract.id)).join(
            Post, Post.creator_id==AgentProfile.id).join(Extract).filter(
            Extract.important == True, Extract.id.in_(extract_ids)))
        r.sort(key=lambda x: x[1], reverse=True)
        if id_only:
            return [AgentProfile.uri_generic(a) for (a, ce) in r]
        else:
            ids = [a for (a, ce) in r]
            order = {id: order for (order, id) in enumerate(ids)}
            agents = self.db.query(AgentProfile).filter(AgentProfile.id.in_(ids)).all()
            agents.sort(key=lambda a: order[a.id])
            return agents

    def get_contributors(self):
        # anyone who contributed to any of the idea's posts
        local_uri = AppQuadStorageManager.local_uri()
        discussion_storage = \
            AppQuadStorageManager.discussion_storage_name()

        idea_uri = URIRef(self.uri(local_uri))
        clause = '''select count(distinct ?postP), count(distinct ?post), ?author where {
            %s idea:includes* ?ideaP .
            ?postP assembl:postLinkedToIdea ?ideaP  .
            ?post sioc:reply_of* ?postP .
            ?post sioc:has_creator ?author }'''
        r = self.db.execute(
            SparqlClause(clause % (
                idea_uri.n3(),),
                quad_storage=discussion_storage.n3()))
        r = [(int(cpp), int(cp), 'local:Agent/' + a.rsplit('/',1)[1]
              ) for (cpp, cp, a) in r]
        r.sort(reverse=True)
        return [a for (cpp, cp, a) in r]

    @classmethod
    def get_idea_ids_showing_post(cls, post_id, direct=False, indirect=True):
        "Given a post, give the ID of the ideas that show this message"
        # This works because of a virtuoso bug...
        # where DISTINCT gives IDs instead of URIs.
        from .generic import Content
        from .idea_content_link import Extract
        assert direct or indirect
        discussion_storage = \
            AppQuadStorageManager.discussion_storage_name()

        post_uri = URIRef(Content.uri_generic(
            post_id, AppQuadStorageManager.local_uri()))
        if indirect and not direct:
            clause = '''select distinct ?idea where {
                %s sioc:reply_of* ?post .
                ?post assembl:postLinkedToIdea ?ideaP .
                ?idea idea:includes* ?ideaP }'''
        elif direct and not indirect:
            clause = '''select distinct ?idea where {
                %s sioc:reply_of* ?post .
                ?post assembl:postLinkedToIdea ?idea }'''
        if direct and indirect:
            # Not used anymore, to be cleaned.
            clause = '''select distinct ?postP, ?ideaP, ?idea, ?ex where {
                %s sioc:reply_of* ?postP .
                ?postP assembl:postLinkedToIdea ?ideaP  .
                ?idea idea:includes* ?ideaP .
                optional { ?ex oa:hasSource ?postP ;
                    assembl:resourceExpressesIdea ?ideaP . } }'''
            r = list(cls.default_db.execute(
                SparqlClause(clause % (
                    post_uri.n3(),),
                    quad_storage=discussion_storage.n3())))
            r = [(int(x), int(y), int(z), int(e) if e else None)
                 for (x, y, z, e) in r]

            def comp(xxx_todo_changeme, xxx_todo_changeme1):
                (pp1, ip1, i1, e1) = xxx_todo_changeme
                (pp2, ip2, i2, e2) = xxx_todo_changeme1
                direct_idea1 = ip1 == i1
                direct_idea2 = ip2 == i2
                direct_post1 = pp1 == post_id
                direct_post2 = pp2 == post_id
                if direct_idea1 != direct_idea2:
                    return -1 if direct_idea1 else 1
                if direct_post1 != direct_post2:
                    return -1 if direct_post1 else 1
                if pp1 != pp2:
                    # assume hry is congruent with post order.
                    return pp2 - pp1
                if ip1 != ip2:
                    # TODO: Real hry order. Should be rare.
                    return ip2 - ip1
                if i1 != i2:
                    # TODO: Real hry order.
                    return i2 - i1
                if e1 != e2:
                    return e2 - e1
                return 0
            r.sort(cmp=comp)
            # can't trust virtuoso's uniqueness.
            r = [e for e, _ in groupby(r)]
            return [(
                Idea.uri_generic(i),
                Idea.uri_generic(ip),
                Content.uri_generic(pp),
                Extract.uri_generic(ex) if ex else None
            ) for (pp, ip, i, ex) in r]
        else:
            return [int(id) for (id,) in cls.default_db.execute(
                SparqlClause(clause % (
                    post_uri.n3(),),
                    quad_storage=discussion_storage.n3()))]
