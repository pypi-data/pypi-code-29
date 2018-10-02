import sqlalchemy.orm
import sqlalchemy.ext.declarative
from pychado import utils, dbutils
from pychado.classes import general, controlled_vocabulary
from pychado.classes.base import Base


params = utils.parse_yaml(dbutils.default_configuration_file())
params["database"] = "wurst"
uri = dbutils.generate_uri(params)
engine = sqlalchemy.create_engine(uri, echo=False)
Session = sqlalchemy.orm.sessionmaker(bind=engine)
session: sqlalchemy.orm.Session = Session()

Base.metadata.create_all(engine, tables=[general.Db.__table__, general.DbxRef.__table__, controlled_vocabulary.Cv.__table__, controlled_vocabulary.CvTerm.__table__])

mydb = general.Db(name='SO', description='sequence ontology', urlprefix='www.example.com/', url='so')
session.add(mydb)
session.commit()
