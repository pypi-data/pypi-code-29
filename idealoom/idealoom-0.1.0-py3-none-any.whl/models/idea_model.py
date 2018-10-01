# -*- coding: utf-8 -*-
"""Defining an idea model that determines interface elements"""

from sqlalchemy import (
    Column,
    Boolean,
    Integer,
    String,
    ForeignKey,
    UniqueConstraint,
)
from sqlalchemy.orm import (
    relationship,
    backref,
)

from ..auth import (
    CrudPermissions, P_READ, P_ADMIN_DISC)
from . import DiscussionBoundBase
from .discussion import Discussion
from .idea import Idea
from .langstrings import LangString, LangStringEntry


class IdeaModel(DiscussionBoundBase):
    """A model applicable to an idea"""
    __tablename__ = "idea_model"
    id = Column(Integer, primary_key=True)
    discussion_id = Column(Integer, ForeignKey(
        Discussion.id, ondelete='CASCADE', onupdate='CASCADE'),
        nullable=False, index=True)
    identifier = Column(String(100), unique=True)
    base_panel_name = Column(String(60))
    propagate_children = Column(Boolean, default=True, server_default='true')
    show_idea_panel = Column(Boolean, default=False, server_default='false')
    name_ls_id = Column(Integer, ForeignKey(LangString.id), nullable=False)

    name = relationship(
        LangString, foreign_keys=(name_ls_id,),
        backref=backref("name_of_idea_model", uselist=False),
        single_parent=True,
        cascade="all, delete-orphan")

    discussion = relationship(
        "Discussion",
        backref=backref(
            'idea_models',
            cascade="all, delete-orphan"),
    )

    def get_discussion_id(self):
        return self.discussion_id

    @classmethod
    def get_discussion_conditions(cls, discussion_id, alias_maker=None):
        return (cls.discussion_id == discussion_id, )

    crud_permissions = CrudPermissions(P_ADMIN_DISC, P_READ)


class MessageModel(DiscussionBoundBase):
    """A model applicable to messages of a given idea model"""
    __tablename__ = "message_model"
    __table_args__ = (
        UniqueConstraint('idea_model_id', 'identifier'), )
    id = Column(Integer, primary_key=True)
    idea_model_id = Column(Integer, ForeignKey(
        IdeaModel.id, ondelete='CASCADE', onupdate='CASCADE'),
        nullable=False, index=True)
    identifier = Column(String(100), nullable=False)
    name_ls_id = Column(Integer, ForeignKey(LangString.id), nullable=False)

    name = relationship(
        LangString, foreign_keys=(name_ls_id,),
        backref=backref("name_of_message_model", uselist=False),
        single_parent=True,
        cascade="all, delete-orphan")

    idea_model = relationship(
        IdeaModel,
        backref=backref(
            'message_models',
            cascade="all, delete-orphan"),
    )

    def get_discussion_id(self):
        return self.idea_model.discussion_id

    @classmethod
    def get_discussion_conditions(cls, discussion_id, alias_maker=None):
        if alias_maker is None:
            message_model = cls
            idea_model = IdeaModel
        else:
            message_model = alias_maker.alias_from_class(cls)
            idea_model = alias_maker.alias_from_relns(message_model.source)
        return ((message_model.idea_model_id == idea_model.id),
                (idea_model.discussion_id == discussion_id))

    crud_permissions = CrudPermissions(P_ADMIN_DISC, P_READ)
