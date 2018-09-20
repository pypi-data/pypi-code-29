import sqlalchemy.orm
import sqlalchemy.ext.declarative
import sqlalchemy.engine.reflection
from pychado import utils, dbutils
from pychado.classes import general, controlled_vocabulary
from pychado.classes.base import Base


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


params = utils.parse_yaml(dbutils.default_configuration_file())
params["database"] = "mychado"
uri = dbutils.generate_uri(params)
engine = sqlalchemy.create_engine(uri, echo=False)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session: sqlalchemy.orm.Session = Session()

Base.metadata.create_all(engine)#, tables=[general.Db.__table__, general.DbxRef.__table__, controlled_vocabulary.Cv.__table__, controlled_vocabulary.CvTerm.__table__])

mydb = general.Db(name='SO', description='sequence ontology', urlprefix='www.example.com/', url='so')
session.add(mydb)
session.commit()

q = session.query(general.Db).filter(general.Db.name.like("Affymetrix%"))
for instance in q:
    print(instance.name)
print()
q = session.query(general.Db).filter(general.Db.name.like("S%"))
for instance in q:
    print(instance.name)
print()

inspect(controlled_vocabulary.CvTermDbxRef.__table__)
