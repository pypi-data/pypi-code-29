from sqlalchemy import (
    Column,
    Integer,
    String,
    Unicode,
    UnicodeText,
    ForeignKey,
    Index,
    )
from sqlalchemy.dialects.postgresql import ENUM
from rdflib import URIRef, Literal

from assembl.lib.sqla_types import URIRefString
from assembl.models import (
    metadata, Base, Locale, Idea, Content, AgentProfile, Action,
    IdeaGraphView, IdeaLink, Discussion, IdeaVote, TextFragmentIdentifier,
    AbstractAgentAccount, URIRefDb)


_tables = [
    URIRefDb, Discussion, Content, Idea, AgentProfile, Action, IdeaGraphView, IdeaLink,
    IdeaVote,
    TextFragmentIdentifier, # legacy. Should not be used.
    AbstractAgentAccount,
]

_table_names = [t.__tablename__ for t in _tables]
_tables_by_name = {t.__tablename__: t for t in _tables}

table_enum = ENUM(*_table_names, name='table_enum', metadata=metadata)


class RefQuad(Base):
    __tablename__ = "rquad"
    id = Column(Integer, primary_key=True)
    # Maybe an indicator to distinguish quoted
    # horrible attempt to create a universal foreign key...
    subject_table = Column(table_enum, nullable=False)
    subject_id = Column(Integer, nullable=False)
    predicate_id = Column(Integer, ForeignKey(URIRefDb.id), nullable=False, index=True)
    object_table = Column(table_enum, nullable=False)
    object_id = Column(Integer, nullable=False)
    context_id =  Column(Integer, ForeignKey(URIRefDb.id))
    __table_args__ = (
        Index('rquad_subject_idx', subject_table, subject_id),
        Index('rquad_object_idx', object_table, object_id),
        Index('rquad_subject_pred_idx', subject_table, subject_id, predicate_id),
        Index('rquad_object_pred_idx', object_table, object_id, predicate_id),
    )

    def subject_ob(self):
        ob = _tables_by_name[self.subject_table].get(self.subject)
        if self.subject_table == URIRefDb.__tablename__:
            return ob.val
        else:
            return ob

    @property
    def subject(self):
        table = _tables_by_name[self.subject_table]
        if self.subject_table == URIRefDb.__tablename__:
            return table.get(self.subject_id).val
        else:
            return table.val_generic(self.subject_id)

    @property
    def predicate(self):
        return URIRefDb.get(self.predicate_id).val

    @property
    def context(self):
        return URIRefDb.get(self.context_id).val

    def object_ob(self):
        ob = _tables_by_name[self.object_table].get(self.object)
        if self.object_table == URIRefDb.__tablename__:
            return ob.val
        else:
            return ob

    @property
    def object(self):
        table = _tables_by_name[self.object_table]
        if self.object_table == URIRefDb.__tablename__:
            return table.get(self.object_id).val
        else:
            return table.val_generic(self.object_id)


# triggers on insert to check ID fits appropriate table;
# trigger on each table's delete to cascade. UGH.

class LitQuad(Base):
    __tablename__ = "lquad"
    id = Column(Integer, primary_key=True)
    # Maybe an indicator to distinguish quoted
    subject_table = Column(table_enum, nullable=False)
    subject_id = Column(Integer, nullable=False)
    predicate_id = Column(Integer, ForeignKey(URIRefDb.id), nullable=False, index=True)
    object_value = Column(UnicodeText)
    context_id =  Column(Integer, ForeignKey(URIRefDb.id))
    object_type_id =  Column(Integer, ForeignKey(URIRefDb.id))
    lang = Column(String(11), nullable=True)
    __table_args__ = (
        Index('lquad_subject_idx', subject_table, subject_id),
        Index('rquad_subject_pred_idx', subject_table, subject_id, predicate_id),
    )

    @property
    def predicate(self):
        return URIRefDb.get(self.predicate_id).val

    @property
    def context(self):
        return URIRefDb.get(self.context_id).val

    def subject_ob(self):
        ob = _tables_by_name[self.subject_table].get(self.subject)
        if self.subject_table == URIRefDb.__tablename__:
            return ob.val
        else:
            return ob

    @property
    def subject(self):
        table = _tables_by_name[self.subject_table]
        if self.subject_table == URIRefDb.__tablename__:
            return table.val_generic(self.subject_id)
        else:
            return table.get(self.subject_id).val

    @property
    def object_type(self):
        if self.object_type_id:
            return URIRefDb.get(self.object_type_id).val

    def object(self):
        return Literal(self.object_value, datatype=self.object_type, lang=self.lang)

# Another crazy idea to reproduce Virtuoso:
# create a view which is a union of RefQuad and known predicates.
