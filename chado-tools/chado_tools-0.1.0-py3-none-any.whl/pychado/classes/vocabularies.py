import sqlalchemy
import sqlalchemy.engine.reflection
import sqlalchemy.ext.declarative
import sqlalchemy.orm
from pychado import dbutils, utils

Base: sqlalchemy.ext.declarative.DeclarativeMeta = sqlalchemy.ext.declarative.declarative_base()


def inspect(tablename):
    inspector = sqlalchemy.engine.reflection.Inspector.from_engine(engine)
    cols = inspector.get_columns(tablename)
    for col in cols:
        print(col)
    print()
    cols = inspector.get_indexes(tablename)
    for col in cols:
        print(col)
    print()
    print(inspector.get_table_comment(tablename))
    print()
    print(inspector.get_foreign_keys(tablename))
    print()
    print(inspector.get_pk_constraint(tablename))
    print()
    print(inspector.get_unique_constraints(tablename))
    print()
    print(inspector.get_check_constraints(tablename))


class Db(Base):
    """Class for the CHADO 'db' table"""
    # Columns
    db_id = sqlalchemy.Column(sqlalchemy.BIGINT, nullable=False, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(255), nullable=False)
    description = sqlalchemy.Column(sqlalchemy.VARCHAR(255), nullable=True)
    urlprefix = sqlalchemy.Column(sqlalchemy.VARCHAR(255), nullable=True)
    url = sqlalchemy.Column(sqlalchemy.VARCHAR(255), nullable=True)

    # Relationships
    __tablename__ = "db"
    dbxref = sqlalchemy.orm.relationship("DbxRef", back_populates=__tablename__)

    # Constraints
    __table_args__ = (sqlalchemy.UniqueConstraint(name, name="db_c1"), )


class DbxRef(Base):
    """Class for the CHADO 'dbxref' table"""
    # Columns
    dbxref_id = sqlalchemy.Column(sqlalchemy.BIGINT, nullable=False, primary_key=True, autoincrement=True)
    db_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        Db.db_id, onupdate="CASCADE", ondelete="CASCADE", deferrable=True, initially="DEFERRED"), nullable=False)
    accession = sqlalchemy.Column(sqlalchemy.VARCHAR(1024), nullable=False)
    version = sqlalchemy.Column(sqlalchemy.VARCHAR(255), nullable=False, server_default=sqlalchemy.text("''"))
    description = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)

    # Relationships
    __tablename__ = "dbxref"
    db = sqlalchemy.orm.relationship("Db", back_populates=__tablename__)
    cvterm = sqlalchemy.orm.relationship("CvTerm", back_populates=__tablename__)

    # Constraints
    __table_args__ = (sqlalchemy.UniqueConstraint(db_id, accession, version, name="dbxref_c1"),
                      sqlalchemy.Index("dbxref_idx1", db_id),
                      sqlalchemy.Index("dbxref_idx2", accession),
                      sqlalchemy.Index("dbxref_idx3", version))


class Cv(Base):
    """Class for the CHADO 'cv' table"""
    # Columns
    cv_id = sqlalchemy.Column(sqlalchemy.BIGINT, nullable=False, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.VARCHAR(255), nullable=False)
    definition = sqlalchemy.Column(sqlalchemy.TEXT, nullable=True)

    # Relationships
    __tablename__ = "cv"
    cvterm = sqlalchemy.orm.relationship("CvTerm", back_populates=__tablename__)

    # Constraints
    __table_args__ = (sqlalchemy.UniqueConstraint(name, name="cv_c1"),)


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

    # Relationships
    __tablename__ = "cvterm"
    dbxref = sqlalchemy.orm.relationship("DbxRef", back_populates=__tablename__)
    cv = sqlalchemy.orm.relationship("Cv", back_populates=__tablename__)
    cvtermprop = sqlalchemy.orm.relationship("CvTermProp", back_populates=__tablename__)
    cvtermsynonym = sqlalchemy.orm.relationship("CvTermSynonym", back_populates=__tablename__)
    cvterm_relationship = sqlalchemy.orm.relationship("CvTermRelationship", back_populates=__tablename__)
    cvterm_dbxref = sqlalchemy.orm.relationship("CvTermDbxRef", back_populates=__tablename__)

    # Constraints
    __table_args__ = (sqlalchemy.UniqueConstraint(name, cv_id, is_obsolete, name="cvterm_c1"),
                      sqlalchemy.UniqueConstraint(dbxref_id, name="cvterm_c2"),
                      sqlalchemy.Index("cvterm_idx1", cv_id),
                      sqlalchemy.Index("cvterm_idx2", name),
                      sqlalchemy.Index("cvterm_idx3", dbxref_id))


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

    # Relationships
    __tablename__ = "cvtermprop"
    cvterm = sqlalchemy.orm.relationship("CvTerm", back_populates=__tablename__)

    # Constraints
    __table_args__ = (sqlalchemy.UniqueConstraint(cvterm_id, type_id, value, rank, name="cvtermprop_c1"),
                      sqlalchemy.Index("cvtermprop_idx1", cvterm_id),
                      sqlalchemy.Index("cvtermprop_idx2", type_id))


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

    # Relationships
    __tablename__ = "cvterm_relationship"
    cvterm = sqlalchemy.orm.relationship("CvTerm", back_populates=__tablename__)

    # Constraints
    __table_args__ = (sqlalchemy.UniqueConstraint(subject_id, object_id, type_id, name="cvterm_relationship_c1"),
                      sqlalchemy.Index("cvterm_relationship_idx1", type_id),
                      sqlalchemy.Index("cvterm_relationship_idx2", subject_id),
                      sqlalchemy.Index("cvterm_relationship_idx3", object_id))


class CvTermSynonym(Base):
    """Class for the CHADO 'cvtermsynonym' table"""
    # Columns
    cvtermsynonym_id = sqlalchemy.Column(sqlalchemy.BIGINT, nullable=False, primary_key=True, autoincrement=True)
    cvterm_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        CvTerm.cvterm_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    synonym = sqlalchemy.Column(sqlalchemy.VARCHAR(1024), nullable=False)
    type_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        CvTerm.cvterm_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=True)

    # Relationships
    __tablename__ = "cvtermsynonym"
    cvterm = sqlalchemy.orm.relationship("CvTerm", back_populates=__tablename__)

    # Constraints
    __table_args__ = (sqlalchemy.UniqueConstraint(cvterm_id, synonym, name="cvtermsynonym_c1"),
                      sqlalchemy.Index("cvtermsynonym_idx1", cvterm_id))


class CvTermDbxRef(Base):
    """Class for the CHADO 'cvterm_dbxref' table"""
    # Columns
    cvterm_dbxref_id = sqlalchemy.Column(sqlalchemy.BIGINT, nullable=False, primary_key=True, autoincrement=True)
    cvterm_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        CvTerm.cvterm_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    dbxref_id = sqlalchemy.Column(sqlalchemy.BIGINT, sqlalchemy.ForeignKey(
        DbxRef.dbxref_id, onupdate="CASCADE", ondelete="CASCADE"), nullable=False)
    is_for_definition = sqlalchemy.Column(sqlalchemy.INTEGER, nullable=False, server_default="0")

    # Relationships
    __tablename__ = "cvterm_dbxref"
    cvterm = sqlalchemy.orm.relationship("CvTerm", back_populates=__tablename__)

    # Constraints
    __table_args__ = (sqlalchemy.UniqueConstraint(cvterm_id, dbxref_id, name="cvterm_dbxref_c1"),
                      sqlalchemy.Index("cvterm_dbxref_idx1", cvterm_id),
                      sqlalchemy.Index("cvterm_dbxref_idx2", dbxref_id))




params = utils.parse_yaml(dbutils.default_configuration_file())
params["database"] = "wurst"
uri = dbutils.generate_uri(params)
engine = sqlalchemy.create_engine(uri, echo=False)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session: sqlalchemy.orm.Session = Session()

Base.metadata.create_all(engine)

# meta = sqlalchemy.MetaData(bind=engine)
# print(meta.sorted_tables)
# print(DbxRef.__table__)

# meta.create_all(engine)
# q = session.query(Db).filter(Db.name.like("Affymetrix%"))
# for instance in q:
#     print(instance.name)
# print()

# actualTable = 'dbxref'
# actualTable = sqlalchemy.Table(checkedTable, meta, autoload=True, autoload_with=engine)
# inspect(actualTable)
inspect(DbxRef.__table__)








class Dbold:
    """Class for databases as used in the 'db' CHADO table"""

    def __init__(self, identifier: int, name: str, description: str, url_prefix: str, url: str):
        self.db_id: int = identifier
        self.name: str = name
        self.description: str = description
        self.urlprefix: str = url_prefix
        self.url: str = url

    def table(self):
        db = sqlalchemy.Table(
            sqlalchemy.Column("db_id", sqlalchemy.Integer, sqlalchemy.Sequence('db_db_id_seq'), primary_key=True),
            sqlalchemy.Column("name", sqlalchemy.String(255)),
            sqlalchemy.Column("description", sqlalchemy.String(255)),
            sqlalchemy.Column("urlprefix", sqlalchemy.String(255)),
            sqlalchemy.Column("url", sqlalchemy.String(255)))


class DbxRefold:
    """Class for database reference numbers as used in the 'dbxref' CHADO table"""

    def __init__(self, identifier: int, database: Db, description: str, accession: str, version: str):
        self.dbxref_id: int = identifier
        self.db: Db = database
        self.accession: str = accession
        self.version: str = version
        self.description: str = description


class Cvold:
    """Class for vocabularies as used in the 'cv' CHADO table"""

    def __init__(self, **kwargs):
        self.cv_id: int = 0
        self.name: str = ""
        self.definition: str = ""

        for key, value in kwargs.items():
            print(key, value)
            if hasattr(self, key):
                setattr(self, key, value)

    # def __init__(self, identifier: int, name: str, definition: str):
    #     self.cv_id: int = identifier
    #     self.name: str = name
    #     self.definition: str = definition


class CvTermold:
    """Class for terms as used in the 'cvterm' CHADO table"""

    def __init__(self, identifier: int, name: str, definition: str, vocabulary: Cvold, reference: DbxRefold, obsolete: bool,
                 reltype: bool):
        self.cvterm_id: int = identifier
        self.cv: Cvold = vocabulary
        self.dbxref: DbxRefold = reference
        self.name: str = name
        self.definition: str = definition
        self.is_obsolete: bool = obsolete
        self.is_relationshiptype: bool = reltype


from pychado import utils

def exists_entry(table: str, **kwargs) -> bool:
    table = table.lower()
    if table == "cv":
        obj = Cvold(**kwargs)
    else:
        obj = utils.EmptyObject
    parameters = vars(obj)

    returnvalues = ", ".join([key for key in parameters])
    conditions = " AND ".join([key + "=" + value for key, value in parameters.items() if value])
    if not conditions:
        conditions = "TRUE"

    query = " ".join(["SELECT", returnvalues, "FROM", table, "WHERE", conditions])
    print(query)
    return True


if __name__ == '__main__':
    print("done")
    #exists_entry("CV", name="relation", wurst="cervela", definition="such thing")