import sqlalchemy.orm
import sqlalchemy.ext.declarative
from pychado.classes.base import Base
from pychado.classes.general import DbxRef

# Object-relational mappings for the CHADO Controlled Vocabulary (CV) module


class Cv(Base):
    """Class for the CHADO 'cv' table"""
    # Columns
    cv_id = sqlalchemy.Column(sqlalchemy.BIGINT, nullable=False, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(255), nullable=False)
    definition = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)

    # Constraints
    __tablename__ = "cv"
    __table_args__ = (sqlalchemy.UniqueConstraint(name, name="cv_c1"),)

    # # Relationships
    # cvterm = sqlalchemy.orm.relationship("CvTerm", backref=__tablename__)


class CvTerm(Base):
    """Class for the CHADO 'cvterm' table"""
    # Columns
    cvterm_id = sqlalchemy.Column(sqlalchemy.BIGINT, nullable=False, primary_key=True, autoincrement=True)
    cv_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        Cv.cv_id, onupdate="CASCADE", ondelete="CASCADE", deferrable=True, initially="DEFERRED"), nullable=False)
    dbxref_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        DbxRef.dbxref_id, onupdate="CASCADE", ondelete="CASCADE", deferrable=True, initially="DEFERRED"),
                                  nullable=False)
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(1024), nullable=False)
    definition = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)
    is_obsolete = sqlalchemy.Column(sqlalchemy.INTEGER, nullable=False, server_default="0")
    is_relationshiptype = sqlalchemy.Column(sqlalchemy.INTEGER, nullable=False, server_default="0")

    # Constraints
    __tablename__ = "cvterm"
    __table_args__ = (sqlalchemy.UniqueConstraint(name, cv_id, is_obsolete, name="cvterm_c1"),
                      sqlalchemy.UniqueConstraint(dbxref_id, name="cvterm_c2"),
                      sqlalchemy.Index("cvterm_idx1", cv_id),
                      sqlalchemy.Index("cvterm_idx2", name),
                      sqlalchemy.Index("cvterm_idx3", dbxref_id))
    
    # Relationships
    dbxref = sqlalchemy.orm.relationship(DbxRef, backref=__tablename__)
    cv = sqlalchemy.orm.relationship(Cv, backref=__tablename__)
    # cvtermprop = sqlalchemy.orm.relationship("CvTermProp", backref=__tablename__)
    # cvtermsynonym = sqlalchemy.orm.relationship("CvTermSynonym", backref=__tablename__)
    # cvterm_relationship = sqlalchemy.orm.relationship("CvTermRelationship", backref=__tablename__)
    # cvterm_dbxref = sqlalchemy.orm.relationship("CvTermDbxRef", backref=__tablename__)


class CvTermProp(Base):
    """Class for the CHADO 'cvtermprop' table"""
    # Columns
    cvtermprop_id = sqlalchemy.Column(sqlalchemy.BIGINT, nullable=False, primary_key=True, autoincrement=True)
    cvterm_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        CvTerm.cvterm_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    type_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        CvTerm.cvterm_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    value = sqlalchemy.Column(sqlalchemy.TEXT, nullable=False, server_default=sqlalchemy.text("''"))
    rank = sqlalchemy.Column(sqlalchemy.INTEGER, nullable=False, server_default="0")

    # Constraints
    __tablename__ = "cvtermprop"
    __table_args__ = (sqlalchemy.UniqueConstraint(cvterm_id, type_id, value, rank, name="cvtermprop_c1"),
                      sqlalchemy.Index("cvtermprop_idx1", cvterm_id),
                      sqlalchemy.Index("cvtermprop_idx2", type_id))

    # Relationships
    cvterm = sqlalchemy.orm.relationship(CvTerm, foreign_keys=cvterm_id, backref="cvtermprop_cvterm")
    type = sqlalchemy.orm.relationship(CvTerm, foreign_keys=type_id, backref="cvtermprop_type")


class CvTermRelationship(Base):
    """Class for the CHADO 'cvterm_relationship' table"""
    # Columns
    cvterm_relationship_id = sqlalchemy.Column(sqlalchemy.BIGINT, nullable=False, primary_key=True, autoincrement=True)
    type_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        CvTerm.cvterm_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    subject_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        CvTerm.cvterm_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    object_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        CvTerm.cvterm_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)

    # Constraints
    __tablename__ = "cvterm_relationship"
    __table_args__ = (sqlalchemy.UniqueConstraint(subject_id, object_id, type_id, name="cvterm_relationship_c1"),
                      sqlalchemy.Index("cvterm_relationship_idx1", type_id),
                      sqlalchemy.Index("cvterm_relationship_idx2", subject_id),
                      sqlalchemy.Index("cvterm_relationship_idx3", object_id))

    # Relationships
    type = sqlalchemy.orm.relationship(CvTerm, foreign_keys=type_id, backref="cvterm_relationship_type")
    subject = sqlalchemy.orm.relationship(CvTerm, foreign_keys=subject_id, backref="cvterm_relationship_subject")
    object = sqlalchemy.orm.relationship(CvTerm, foreign_keys=object_id, backref="cvterm_relationship_object")


class CvTermSynonym(Base):
    """Class for the CHADO 'cvtermsynonym' table"""
    # Columns
    cvtermsynonym_id = sqlalchemy.Column(sqlalchemy.BIGINT, nullable=False, primary_key=True, autoincrement=True)
    cvterm_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        CvTerm.cvterm_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    synonym = sqlalchemy.Column(sqlalchemy.VARCHAR(1024), nullable=False)
    type_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        CvTerm.cvterm_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=True)

    # Constraints
    __tablename__ = "cvtermsynonym"
    __table_args__ = (sqlalchemy.UniqueConstraint(cvterm_id, synonym, name="cvtermsynonym_c1"),
                      sqlalchemy.Index("cvtermsynonym_idx1", cvterm_id))

    # Relationships
    cvterm = sqlalchemy.orm.relationship(CvTerm, foreign_keys=cvterm_id, backref="cvtermsynonym_cvterm")
    type = sqlalchemy.orm.relationship(CvTerm, foreign_keys=type_id, backref="cvtermsynonym_type")


class CvTermDbxRef(Base):
    """Class for the CHADO 'cvterm_dbxref' table"""
    # Columns
    cvterm_dbxref_id = sqlalchemy.Column(sqlalchemy.BIGINT, nullable=False, primary_key=True, autoincrement=True)
    cvterm_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        CvTerm.cvterm_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    dbxref_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        DbxRef.dbxref_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    is_for_definition = sqlalchemy.Column(sqlalchemy.INTEGER, nullable=False, server_default="0")

    # Constraints
    __tablename__ = "cvterm_dbxref"
    __table_args__ = (sqlalchemy.UniqueConstraint(cvterm_id, dbxref_id, name="cvterm_dbxref_c1"),
                      sqlalchemy.Index("cvterm_dbxref_idx1", cvterm_id),
                      sqlalchemy.Index("cvterm_dbxref_idx2", dbxref_id))

    # Relationships
    cvterm = sqlalchemy.orm.relationship(CvTerm, foreign_keys=cvterm_id, backref="cvterm_dbxref_cvterm")
    dbxref = sqlalchemy.orm.relationship(DbxRef, foreign_keys=dbxref_id, backref="cvterm_dbxref_dbxref")
