# -*- coding: utf-8 -*-
"Collection and collection queries"

from future import standard_library
standard_library.install_aliases()
from builtins import object
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
    join,
)
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from enum import Enum
from abc import abstractmethod, abstractproperty
from urllib.parse import urlencode

from rdflib import URIRef

from ..lib.sqla_types import URLString as RDFURI
from ..lib.abc import classproperty
from ..lib.sqla import CrudOperation
from . import Base, DiscussionBoundBase
from .auth import User
from .discussion import Discussion

# Note: Rules come after Collections.


# An object creation/modification will run through relevant Collections, in case there are materialized impacts.
# (So Collections need to be able to hook to those events.)
# BUT the main thing happening at log-in is that a celery(?) task will run that will feed CollectionApplications to the front-end.
# Should it remain aware that the user is logged-in? Probably.
# 1. materializing Collections
# 2. Collections for logged-in users.
# Note: CollectionCondition or CollectionFunction?
# Do I need to materialize those in the DB? Not so sure.

class CollectionEventTypes(Enum):

    SimpleCollectionEvent = 1  # will we need this?
    ResourceEntersCollection = 2
    ResourceUpdated = 3
    ResourceLeavesCollection = 4
    CollectionStable = 5
    KeyAttributeUpdated = 6  # when collection's main aim is to tally a derived attribute
    # Not sure I need those; intended for mappers
    ResourceReferredUpdated = 7
    ResourceReferredLeaves = 8  # used to delete transient resources by contents. Dubious.
    UserAction = 9  # An eg of an event that is not a collection event


class AbstractCollection(object):
    def __init__(self, name, description=None, base_collection=None,
                 base_resource_type=None, parameters=None, bindings=None):
        self.name = name
        self.description = description
        self.base_collection = base_collection
        self.subscribers = []
        self.base_resource_type = base_resource_type
        self.parameters = parameters or {}
        self.bindings = bindings or {}
        if base_collection is not None:
            base_collection.subscribe(self)
            self.base_resource_type = (
                base_resource_type or base_collection.base_resource_type)

    def parameters(self):
        return self.parameters

    def unbound_parameters(self):
        return {k for k in self.parameters if k not in self.bindings}

    def signature(self, params=None):
        if params is None:
            params = self.bindings
        else:
            params = self.bindings.copy().update(params)
        sorted_param_keys = list(params.keys())
        sorted_param_keys.sort()
        name = self.name
        if params:
            name += '?'+'&'.urlencode(params)
        return name

    @abstractmethod
    def resources(self):
        return ()

    @abstractmethod
    def __len__(self):
        return 0

    @abstractmethod
    def contains(self, resource):
        return False

    @abstractmethod
    def contains_json(self, resource_json):
        return False

    @abstractmethod
    def last_change(self):
        return None

    @abstractmethod
    def events_since(self, timestamp):
        # yield
        pass

    def subscribe(self, client):
        # TODO: What if it's there?
        self.subscribers.append(client)

    def unsubscribe(self, client):
        # TODO: What if it's not there?
        self.subscribers.pop(client)

    def event_cascade(self, event):
        yield event

    def active(self):
        # it could depend on having an active subscriber
        return True

    def active_subscribers(self):
        for sub in self.subscribers:
            if sub.active():
                yield sub

    def propagate(self, event):
        # basic strategy, optionally subclass
        for event in self.event_cascade(event):
            for client in self.active_subscribers():
                # How to avoid the same client receiving the same event twice?
                client.propagate(event)

    def js_equivalent_filter(self):
        return None


class DataTypeDescription(object):
    pass  # Has URIRef. Materialized?


class CollectionEvent(object):
    """Something that may trigger a collection, and may be produced by a collection

    Must have a signature, and be recomposable from same."""
    event_type = None  # given by owning collection, no?
    data_type = None
    resource_endpoint = None  # if non-transient
    collection_endpoint = None  # maybe
    active = True  # What is lifecycle? Propagating, handled...
    resource_uri = None
    _resource = None
    _resource_json = None
    last_transaction_uid = None

    @property
    def resource(self):
        if self._resource is None:
            self._resource = get_named_object(self.resource_uri)
        return self._resource

    @property
    def resource_json(self):
        if self._resource_json is None:
            self._resource_json = self.resource.generic_json()
        return self._resource_json


class AbstractSQLACollection(AbstractCollection):
    # collection of sqla resources. Not to be confused with collection
    # materialized through sqla
    name = None
    description = None

    def __init__(self, name, description=None, base_collection=None,
                 base_resource_type=None, parameters=None, bindings=None):
        super(AbstractSQLACollection, self).__init__(
            name, description, base_collection, base_resource_type,
            parameters, bindings)

    @abstractproperty
    def query(self):
        pass

    def resources(self):
        return self.query.all()

    def __len__(self):
        return self.query.count()



class SQLAClassCollection(AbstractSQLACollection):

    def __init__(self, name, description=None, base_collection=None,
                 base_resource_type=None, parameters=None, bindings=None):
        super(SQLAClassCollection, self).__init__(
            name, description, base_collection, base_resource_type,
            parameters, bindings)

    @abstractproperty
    def query(self):
        cls = self.base_resource_type
        return cls.default_db.query(cls)


class DiscussionDispatchCollection(SQLAClassCollection):
    pass




class CollectionTemplate(Base):
    """A basic collection with possibly unbound variables.
    """
    __tablename__ = "collection_template"
    id = Column(Integer, primary_key=True)
    identifier = Column(RDFURI, nullable=False, unique=True)
    target_type = Column(RDFURI, nullable=False, unique=True)



class CollectionTemplateVariable(Base):
    __tablename__ = "collection_template_variable"
    id = Column(Integer, primary_key=True)
    collection_template_id = Column(Integer, ForeignKey(
        CollectionTemplate.id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False)
    name = Column(String, nullable=False)
    binding_type = Column(RDFURI, nullable=False, unique=True)
    template = relationship(CollectionTemplate, backref='variables')


class Collection(Base):
    __tablename__ = "collection"
    id = Column(Integer, primary_key=True)
    # do collections always have an URI identifier?
    # Does that give a URL?
    # what if transient, ad-hoc collection?
    identifier = Column(RDFURI, nullable=False, unique=True)
    target_type = Column(RDFURI, nullable=False, unique=True)
    collection_template_id = Column(Integer, ForeignKey(
        CollectionTemplate.id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=True)
    transient_collection = Column(Boolean, server_default='false')
    transient_expiry = Column(DateTime, nullable=True)
    transient_connection_token = Column(String, nullable=True)
    transient_results = Column(Boolean, server_default='false')
    active = Column(Boolean, server_default='false')
    # lifecycle = Column(String) # Or enum? basically active/obsolete/dismissed/snoozed...

    @property
    def fully_bound(self):
        "Are all variables bound in this collection and its dependents?"
        # TODO: optimize
        if not self.collection_template:
            return True
        vars = self.collection_template.variables
        bound_vars = {binding.variable_defs for binding in self.bindings}
        if set(vars) - bound_vars:
            return False
        for collection in self.depends_on_collections:
            if not collection.fully_bound:
                return False
        return True

    def process_event(self, event, parameters=None):
        # check if relevant or return
        # for each relevant cached store event: invalidate
        # transform event into derived event
        # Store derived event if appropriate
        # for each dependendant collection: dispatch
        pass

    def get_base_query(self):
        """Optimization: get a SQL query which will give the basis for events' resource

        Can be refined by dependant collections, instead of getting all active_events."""
        # if refines: delegate and decorate (maybe in subclass?)
        # otherwise create a query object... how? subclass. Not implemented locally.
        pass

    def get_active_dependent_collections(self, recursive=True):
        """Get all collections that depend on this one and are active.
        This method should be active as well.
        """
        pass

    def rebind_vars(
            self, transient_token=None, transient_expiry=None,
            activate=True, **bindings):
        """Clone, with the new bindings patching old ones.
        If either transient_token or expiry is given,
        make the clone transient.
        Make the clone active in general."""
        pass

    def invalidate_cache(self):
        pass

    def get_resources(self):
        "Get all the resources in this collection. (vs events)"
        # may use the cache unless recompute
        pass

    def prefilter_resource(self, resource):
        # before alteration
        return True

    def alter_resource(self, resource):
        "Alter a resource"
        # may use the cache
        return resource

    def postfilter_resource(self, resource):
        # after alteration
        return True

    def alter_event(self, event):
        "Filter/alter an event by altering the underlying resource"
        # may use the cache
        old_resource = event.resource
        if event.event_type == CollectionEventTypes.CollectionStable:
            if len(self.depends_on_collections) == 1:
                yield event
            # else, find a few more cases where this could be transmitted.
            return
        if (event.event_type == CollectionEventTypes.ResourceLeavesCollection and
                self.transient_results):
            yield CollectionEvent(
                resource=old_resource,
                event_type=CollectionEventTypes.ResourceReferredLeaves)
            return
        new_resource = self.alter_resource(old_resource)
        # TODO: check that the new resource is of the right datatype, and otherwise validate
        assert new_resource
        if new_resource is not old_resource:
            # TODO: get the old version of old_resource, to destroy the transformed cache?
            # Ideally cache should rely on a resource invariant.
            pass
        if (event.event_type != CollectionEventTypes.ResourceLeavesCollection and
                not (new_resource is not None and
                     self.prefilter_resource(old_resource) and
                     self.postfilter_resource(new_resource))):
            if new_resource:
                yield CollectionEvent(resource=new_resource,
                            event_type=CollectionEventTypes.ResourceLeavesCollection)
            return
        yield CollectionEvent(resource=new_resource, event_type=event.event_type)

    def get_resources_as_events(self):
        """Get the collection of resources in this collection
        as a set of ResourceEntersCollection followed by a CollectionStable events"""
        # may use the cache
        pass

    def get_events_since(self, timestamp):
        # timestamp or kafka ID?
        pass

    def get_resource_count(self):
        pass


    """
    Based on a Collection, an instance of objects that triggered that collection. There should be a main target object (many? Not sure we’ll have non-idea targets for awhile.)
    MIGHT NOT BE MATERIALIZED.
    Exception: If CollectionApplication creates a materialized notification, it cannot be transient, and knows about that notification.
    Note that, when creating transient CollectionApplication,
    a CollectionProcessor should check if a corresponding materialized CollectionApplication exists.
    Often, a CollectionApplication will be un-triggered by clicking on the notification email or reading the notification (dismiss button)
    Materializing is a form of caching concern: a transient CollectionApplication is created on demand by the backend.
    """
    # send_on_socket = True  # class-dependent? instance-dependent?
    # user_bound = True  # hmm.... User would be part of bindings, yes?
    # Question: What to do with a RCA that is identical for a bunch of users, but not valid for all (eg because read/unread)
    # Answer: Clone. Sigh.


class CollectionBindingType(Enum):
    LITERAL = 1
    RESOURCE_URI = 2
    RULE_URI = 2
    UNIVERSAL_QUANTIFIER = 3


class CollectionVariableBinding(Base):
    __tablename__ = "collection_variable_binding"
    id = Column(Integer, primary_key=True)
    sqla_type = Column(String(20), nullable=False)
    collection_id = Column(Integer, ForeignKey(
        Collection.id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False)
    template_variable_id = Column(Integer, ForeignKey(
        CollectionTemplateVariable.id),
        nullable=False)
    literal = Column(JSONB)
    collection = relationship(Collection, backref='bindings')
    variable_def = relationship(CollectionTemplateVariable)

    __mapper_args__ = {
        'polymorphic_identity': 'abstract',
        'polymorphic_on': sqla_type,
        'with_polymorphic': '*'
    }


class CollectionVariableBindingUniversal(CollectionVariableBinding):
    __mapper_args__ = {
        'polymorphic_identity': 'universal',
    }


class CollectionVariableBindingResource(CollectionVariableBinding):
    __tablename__ = "collection_variable_binding_res"
    id = Column(Integer, ForeignKey(
        CollectionVariableBinding.id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False, primary_key=True)
    uri = Column(RDFURI, nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'resource',
    }


class CollectionVariableBindingInternalCollection(CollectionVariableBinding):
    __tablename__ = "collection_variable_binding_collection"
    __mapper_args__ = {
        'polymorphic_identity': 'collection',
    }
    id = Column(Integer, ForeignKey(
        CollectionVariableBinding.id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False, primary_key=True)
    value_collection_id = Column(Integer, ForeignKey(
        Collection.id, ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    subbindings = Column(JSONB, nullable=False)
    # hmmm. subbindings only matter when I'm binding, not to a real collection,
    # but to a virtual collection, eg semi-materialized collection template!
    # Is that a choice? Is that a distinct choice?


class CollectionVariableBindingLiteral(CollectionVariableBinding):
    __tablename__ = "collection_variable_binding_literal"
    __mapper_args__ = {
        'polymorphic_identity': 'literal',
    }
    id = Column(Integer, ForeignKey(
        CollectionVariableBinding.id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False, primary_key=True)
    data = Column(JSONB, nullable=False)


Collection.dependent_collections = relationship(
    Collection, viewonly=True,
    secondary=join(
        CollectionVariableBindingInternalCollection.__table__,
        CollectionVariableBinding.__table__),
    primaryjoin=Collection.id == CollectionVariableBinding.collection_id,
    secondaryjoin=Collection.id == CollectionVariableBindingInternalCollection.value_collection_id,
    backref="depends_on_collections")


class AbstractCollectionSet(Base):
    """Set of partially bound collections, to be used as a template"""
    __tablename__ = "abstract_collection_set"
    id = Column(Integer, primary_key=True)
    identifier = Column(RDFURI, unique=True)
    description = Column(UnicodeText)

    def bind(self, discussion_id, **bindings):
        """Clone all collections in the set so they are fully bound, yielding a BoundCollectionSet."""
        pass


class BoundCollectionSet(AbstractCollectionSet, DiscussionBoundBase):
    """Collection set bound to a given discussion. Associates collections to discussions,
    also allows mass enable/disable of collections.
    Q: Are there collections bound to discussions otherwise?"""
    __tablename__ = "bound_collection_set"
    id = Column(Integer, ForeignKey(AbstractCollectionSet.id), primary_key=True)
    discussion_id = Column(Integer, ForeignKey(Discussion.id), nullable=False)


class CollectionSetCollectionAssociation(Base):
    __tablename__ = "collection_set_collection_association"
    collection_set_id = Column(Integer, ForeignKey(AbstractCollectionSet.id, ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    collection_id = Column(Integer, ForeignKey(Collection.id, ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    order = Column(Float)  # Todo: look at the ordering pattern in sqla doc.


class CollectionCachedEntity(Base):
    """
    A cached entity. Has bound parameters. Sometimes it makes sense for a Collection to store a computation, and the CollectionApplications can be created faster using those. (Does the front-end need to know about those?)
    CachedCollectionEventIdeaParameter = CachedCollectionEventId+ParamName+IdeaId. If idea changes, we can kill all RCC fast. (and so on with other types.)
    OR CollectionCachedCollectionEvent could have a signature as a small json object, we lose delete cascades but we could do uniqueness on signatures.
    Note that I may have a CachedCollectionEvent that just happens to have a CollectionApplication as 1st parameter, and then I can do this partial bind stuff I spoke about earlier."""
    __tablename__ = "collection_cached_event"
    id = Column(Integer, primary_key=True)
    # collection_id = Column(Integer, ForeignKey(Collection.id), nullable=False)
    # discussion_id = Column(Integer, ForeignKey(Discussion.id), nullable=False)
    # bindings = Column(JSONB, index=True)
    signature = Column(JSONB, unique=True)
    content = Column(JSONB)


class CollectionProcessor(object):
    def get_logged_in_users(self):
        # Get from changes router. Sigh.
        # Actually: (User, discussion_id) pairs.
        pass

    def get_definitions(self, discussion_id, user_id):
        # get all relevant collection definitions
        pass

    def get_active_events(self, discussion_id, user_id):
        # get all relevant events
        pass

    def process_event(self, event):
        # get all unique relevant collections from:
        #   * immediate collections
        #   * cache objects
        #   * collections relevant to logged-in users
        #   * subscribed collections
        # for each collection: dispatch
        # (maybe just dispatch on all collections?)
        pass
