# -*- coding: utf-8 -*-
"Rule and rule queries"

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

from rdflib import URIRef

from ..lib.sqla_types import URLString as RDFURI
from ..lib.abc import classproperty
from ..lib.sqla import CrudOperation
from . import Base, DiscussionBoundBase
from .auth import User
from .discussion import Discussion

# Note: Rules come after Rules.


# An object creation/modification will run through relevant Rules, in case there are materialized impacts.
# (So Rules need to be able to hook to those events.)
# BUT the main thing happening at log-in is that a celery(?) task will run that will feed RuleApplications to the front-end.
# Should it remain aware that the user is logged-in? Probably.
# 1. materializing Rules
# 2. Rules for logged-in users.
# Note: RuleCondition or RuleFunction?
# Do I need to materialize those in the DB? Not so sure.

class RuleEventTypes(Enum):

    SimpleRuleEvent = 1
    ResourceUpdated = 2
    ResourceEntersRule = 3
    ResourceLeavesRule = 4
    ResourceReferredUpdated = 5
    ResourceAttributeUpdated = 9  # when collection's main aim is to tally a derived attribute
    ResourceReferredLeaves = 8  # used to delete transient resources by contents
    RuleStable = 6
    UserAction = 7


class DataTypeDescription(object):
    pass  # Has URIRef. Materialized?


class RuleEvent(object):
    """Something that may trigger a rule, and may be produced by a rule

    Must have a signature, and be recomposable from same."""
    event_type = None  # given by owning collection, no?
    data_type = None
    resource_endpoint = None  # if non-transient
    collection_endpoint = None  # maybe
    active = True  # What is lifecycle? Propagating, handled...
    resource = None
    serialized_resource = None
    last_transaction_uid = None


class RuleTemplate(Base):
    """A basic rule with possibly unbound variables.
    """
    __tablename__ = "rule_template"
    id = Column(Integer, primary_key=True)
    identifier = Column(RDFURI, nullable=False, unique=True)
    target_type = Column(RDFURI, nullable=False, unique=True)


class RuleTemplateVariable(Base):
    __tablename__ = "rule_template_variable"
    id = Column(Integer, primary_key=True)
    rule_template_id = Column(Integer, ForeignKey(
        RuleTemplate.id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False)
    name = Column(String, nullable=False)
    binding_type = Column(RDFURI, nullable=False, unique=True)
    template = relationship(RuleTemplate, backref='variables')


class Rule(Base):
    __tablename__ = "rule"
    id = Column(Integer, primary_key=True)
    # do rules always have an URI identifier?
    # Does that give a URL?
    # what if transient, ad-hoc rule?
    identifier = Column(RDFURI, nullable=False, unique=True)
    target_type = Column(RDFURI, nullable=False, unique=True)
    rule_template_id = Column(Integer, ForeignKey(
        RuleTemplate.id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=True)
    transient_rule = Column(Boolean, server_default='false')
    transient_expiry = Column(DateTime, nullable=True)
    transient_connection_token = Column(String, nullable=True)
    transient_results = Column(Boolean, server_default='false')
    active = Column(Boolean, server_default='false')
    # lifecycle = Column(String) # Or enum? basically active/obsolete/dismissed/snoozed...

    @property
    def fully_bound(self):
        "Are all variables bound in this rule and its dependents?"
        # TODO: optimize
        if not self.rule_template:
            return True
        vars = self.rule_template.variables
        bound_vars = {binding.variable_defs for binding in self.bindings}
        if set(vars) - bound_vars:
            return False
        for rule in self.depends_on_rules:
            if not rule.fully_bound:
                return False
        return True

    def process_event(self, event, parameters=None):
        # check if relevant or return
        # for each relevant cached store event: invalidate
        # transform event into derived event
        # Store derived event if appropriate
        # for each dependendant rule: dispatch
        pass

    def get_base_query(self):
        """Optimization: get a SQL query which will give the basis for events' resource

        Can be refined by dependant rules, instead of getting all active_events."""
        # if refines: delegate and decorate (maybe in subclass?)
        # otherwise create a query object... how? subclass. Not implemented locally.
        pass

    def get_active_dependent_rules(self, recursive=True):
        """Get all rules that depend on this one and are active.
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
        if event.event_type == RuleEventTypes.RuleStable:
            if len(self.depends_on_rules) == 1:
                yield event
            # else, find a few more cases where this could be transmitted.
            return
        if (event.event_type == RuleEventTypes.ResourceLeavesRule and
                self.transient_results):
            yield RuleEvent(
                resource=old_resource,
                event_type=RuleEventTypes.ResourceReferredLeaves)
            return
        new_resource = self.alter_resource(old_resource)
        # TODO: check that the new resource is of the right datatype, and otherwise validate
        assert new_resource
        if new_resource is not old_resource:
            # TODO: get the old version of old_resource, to destroy the transformed cache?
            # Ideally cache should rely on a resource invariant.
            pass
        if (event.event_type != RuleEventTypes.ResourceLeavesRule and
                not (new_resource is not None and
                     self.prefilter_resource(old_resource) and
                     self.postfilter_resource(new_resource))):
            if new_resource:
                yield RuleEvent(resource=new_resource,
                            event_type=RuleEventTypes.ResourceLeavesRule)
            return
        yield RuleEvent(resource=new_resource, event_type=event.event_type)

    def get_resources_as_events(self):
        """Get the collection of resources in this collection
        as a set of ResourceEntersRule followed by a RuleStable events"""
        # may use the cache
        pass

    def get_events_since(self, timestamp):
        # timestamp or kafka ID?
        pass

    def get_resource_count(self):
        pass


    """
    Based on a Rule, an instance of objects that triggered that rule. There should be a main target object (many? Not sure we’ll have non-idea targets for awhile.)
    MIGHT NOT BE MATERIALIZED.
    Exception: If RuleApplication creates a materialized notification, it cannot be transient, and knows about that notification.
    Note that, when creating transient RuleApplication,
    a RuleProcessor should check if a corresponding materialized RuleApplication exists.
    Often, a RuleApplication will be un-triggered by clicking on the notification email or reading the notification (dismiss button)
    Materializing is a form of caching concern: a transient RuleApplication is created on demand by the backend.
    """
    # send_on_socket = True  # class-dependent? instance-dependent?
    # user_bound = True  # hmm.... User would be part of bindings, yes?
    # Question: What to do with a RCA that is identical for a bunch of users, but not valid for all (eg because read/unread)
    # Answer: Clone. Sigh.


class RuleBindingType(Enum):
    LITERAL = 1
    RESOURCE_URI = 2
    RULE_URI = 2
    UNIVERSAL_QUANTIFIER = 3


class RuleVariableBinding(Base):
    __tablename__ = "rule_variable_binding"
    id = Column(Integer, primary_key=True)
    sqla_type = Column(String(20), nullable=False)
    rule_id = Column(Integer, ForeignKey(
        Rule.id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False)
    template_variable_id = Column(Integer, ForeignKey(
        RuleTemplateVariable.id),
        nullable=False)
    literal = Column(JSONB)
    rule = relationship(Rule, backref='bindings')
    variable_def = relationship(RuleTemplateVariable)

    __mapper_args__ = {
        'polymorphic_identity': 'abstract',
        'polymorphic_on': sqla_type,
        'with_polymorphic': '*'
    }


class RuleVariableBindingUniversal(RuleVariableBinding):
    __mapper_args__ = {
        'polymorphic_identity': 'universal',
    }


class RuleVariableBindingResource(RuleVariableBinding):
    __tablename__ = "rule_variable_binding_res"
    id = Column(Integer, ForeignKey(
        RuleVariableBinding.id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False, primary_key=True)
    uri = Column(RDFURI, nullable=False)
    __mapper_args__ = {
        'polymorphic_identity': 'resource',
    }


class RuleVariableBindingInternalRule(RuleVariableBinding):
    __tablename__ = "rule_variable_binding_rule"
    __mapper_args__ = {
        'polymorphic_identity': 'rule',
    }
    id = Column(Integer, ForeignKey(
        RuleVariableBinding.id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False, primary_key=True)
    value_rule_id = Column(Integer, ForeignKey(
        Rule.id, ondelete="CASCADE", onupdate="CASCADE"), nullable=False)
    subbindings = Column(JSONB, nullable=False)
    # hmmm. subbindings only matter when I'm binding, not to a real rule,
    # but to a virtual rule, eg semi-materialized rule template!
    # Is that a choice? Is that a distinct choice?


class RuleVariableBindingLiteral(RuleVariableBinding):
    __tablename__ = "rule_variable_binding_literal"
    __mapper_args__ = {
        'polymorphic_identity': 'literal',
    }
    id = Column(Integer, ForeignKey(
        RuleVariableBinding.id, ondelete="CASCADE", onupdate="CASCADE"),
        nullable=False, primary_key=True)
    data = Column(JSONB, nullable=False)


Rule.dependent_rules = relationship(
    Rule, viewonly=True,
    secondary=join(
        RuleVariableBindingInternalRule.__table__,
        RuleVariableBinding.__table__),
    primaryjoin=Rule.id == RuleVariableBinding.rule_id,
    secondaryjoin=Rule.id == RuleVariableBindingInternalRule.value_rule_id,
    backref="depends_on_rules")


class AbstractRuleSet(Base):
    """Set of partially bound rules, to be used as a template"""
    __tablename__ = "abstract_rule_set"
    id = Column(Integer, primary_key=True)
    identifier = Column(RDFURI, unique=True)
    description = Column(UnicodeText)

    def bind(self, discussion_id, **bindings):
        """Clone all rules in the set so they are fully bound, yielding a BoundRuleSet."""
        pass


class BoundRuleSet(AbstractRuleSet, DiscussionBoundBase):
    """Rule set bound to a given discussion. Associates rules to discussions,
    also allows mass enable/disable of rules.
    Q: Are there rules bound to discussions otherwise?"""
    __tablename__ = "bound_rule_set"
    id = Column(Integer, ForeignKey(AbstractRuleSet.id), primary_key=True)
    discussion_id = Column(Integer, ForeignKey(Discussion.id), nullable=False)


class RuleSetRuleAssociation(Base):
    __tablename__ = "rule_set_rule_association"
    rule_set_id = Column(Integer, ForeignKey(AbstractRuleSet.id, ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    rule_id = Column(Integer, ForeignKey(Rule.id, ondelete="CASCADE", onupdate="CASCADE"), primary_key=True)
    order = Column(Float)  # Todo: look at the ordering pattern in sqla doc.


class RuleCachedEntity(Base):
    """
    A cached entity. Has bound parameters. Sometimes it makes sense for a Rule to store a computation, and the RuleApplications can be created faster using those. (Does the front-end need to know about those?)
    CachedRuleEventIdeaParameter = CachedRuleEventId+ParamName+IdeaId. If idea changes, we can kill all RCC fast. (and so on with other types.)
    OR RuleCachedRuleEvent could have a signature as a small json object, we lose delete cascades but we could do uniqueness on signatures.
    Note that I may have a CachedRuleEvent that just happens to have a RuleApplication as 1st parameter, and then I can do this partial bind stuff I spoke about earlier."""
    __tablename__ = "rule_cached_event"
    id = Column(Integer, primary_key=True)
    # rule_id = Column(Integer, ForeignKey(Rule.id), nullable=False)
    # discussion_id = Column(Integer, ForeignKey(Discussion.id), nullable=False)
    # bindings = Column(JSONB, index=True)
    signature = Column(JSONB, unique=True)
    content = Column(JSONB)


class RuleProcessor(object):
    def get_logged_in_users(self):
        # Get from changes router. Sigh.
        # Actually: (User, discussion_id) pairs.
        pass

    def get_definitions(self, discussion_id, user_id):
        # get all relevant rule definitions
        pass

    def get_active_events(self, discussion_id, user_id):
        # get all relevant events
        pass

    def process_event(self, event):
        # get all unique relevant rules from:
        #   * immediate rules
        #   * cache objects
        #   * rules relevant to logged-in users
        #   * subscribed rules
        # for each rule: dispatch
        # (maybe just dispatch on all rules?)
        pass
