class Action(TombstonableMixin, OriginMixin, DiscussionBoundBase):
    """
    An action that can be taken by an actor (a :py:class:`.auth.User`).

    Most actions are expressed in terms of actor-verb-target-time,
    with verbs including but not restricted to CRUD operations.
    """
    __tablename__ = 'action'
    __external_typename = "Update"

    id = Column(Integer, primary_key=True)
    type = Column(String(255), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'action',
        'polymorphic_on': type,
        'with_polymorphic': '*'
    }

    actor_id = Column(
        Integer,
        ForeignKey('user.id', ondelete='CASCADE', onupdate='CASCADE'),
        nullable=False, index=True,
        info={'rdf': QuadMapPatternS(
            None, VERSION.who, AgentProfile.agent_as_account_iri.apply(None))}
    )

    actor = relationship(
        User,
        backref=backref('actions', order_by="Action.creation_date",
                        cascade="all, delete-orphan")
    )

    verb = 'did something to'

    # Because abstract, do in concrete subclasses
    # @classmethod
    # def special_quad_patterns(cls, alias_maker, discussion_id):
    #     return [QuadMapPatternS(None,
    #         RDF.type, IriClass(VirtRDF.QNAME_ID).apply(Action.type),
    #         name=QUADNAMES.class_Action_class)]

    def populate_from_context(self, context):
        if not(self.actor_dagent or self.actor_dagent_id):
            from .auth import DiscussionAgent
            self.actor_dagent = context.get_instance_of_class(DiscussionAgent)
        super(Action, self).populate_from_context(context)

    @as_native_str()
    def __repr__(self):
        return "%s %s %s %s>" % (
            super(Action, self).__repr__()[:-1],
            self.actor.display_name() if self.actor else 'nobody',
            self.verb,
            self.object_type)

    def is_owner(self, uagent):
        return self.actor_dagent.profile_id == uagent.user_id

    def container_url(self):
        return "/data/Discussion/%d/all_users/%d/actions" % (
            self.get_discussion_id(), self.actor_id)

    def get_default_parent_context(self, request=None, user_id=None):
        return self.actor.get_collection_context(
            'actions', request=request, user_id=user_id)

    @classmethod
    def restrict_to_owners(cls, q, user_id):
        return q.join(DiscussionAgent).filter(DiscussionAgent.profile_id == user_id)

    crud_permissions = CrudPermissions(
        P_READ, P_SYSADMIN, P_SYSADMIN, P_SYSADMIN, P_READ, P_READ, P_READ)

