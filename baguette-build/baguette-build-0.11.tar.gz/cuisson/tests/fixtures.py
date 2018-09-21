#-*- coding:utf-8 -*-
import datetime
import uuid
import mock
import multiprocessing
import os
import random
import shutil
import string
import time
import pytest
import cuisson
import cuisson.service
import farine.exceptions
import farine.rpc
import farine.settings
import docker
from pytest_rabbitmq.factories.client import clear_rabbitmq
from farine.tests.fixtures import *
from pytest_postgresql import factories


postgresql_proc = factories.postgresql_proc()
postgres = factories.postgresql('postgresql_proc')

def gen_str(length=15):
    """
    Generate a string of `length`.
    """
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in xrange(length))

@pytest.fixture(autouse=True)
def init(postgres):
    """
    auto load the settings and init the db.
    """
    farine.settings.load()
    db = farine.connectors.sql.setup(farine.settings.cuisson)
    db.execute_sql('CREATE TABLE "build" ("uid" VARCHAR(255) NOT NULL PRIMARY KEY, "owner" VARCHAR(255) NOT NULL, "repo" VARCHAR(255) NOT NULL, "branch" VARCHAR(255) NOT NULL, "date_created" TIMESTAMP DEFAULT NOW())')
    db.execute_sql('CREATE TABLE "status" ("id" SERIAL NOT NULL PRIMARY KEY, "uid_id" VARCHAR(255) NOT NULL, "status" VARCHAR(255) NOT NULL, "fail" BOOLEAN NOT NULL DEFAULT FALSE,  "context" json NOT NULL, "date_created" TIMESTAMP DEFAULT NOW(), FOREIGN KEY(uid_id) REFERENCES build(uid))')
    db.close()
    farine.connectors.sql.init('cuisson', db)

@pytest.fixture
def db_factory():
    def factory(owner, repo, branch, fail=False, nb_steps=9, date_created=None):
        from cuisson.models import Build, Status
        uid = uuid.uuid4().hex
        Build.create(owner=owner, branch=branch, repo=repo, uid=uid, date_created=date_created)
        steps = ['clone', 'generate-recipe', 'generate-definition', 'generate-dockerfile', 'generate-dns', 'build-docker', 'push-docker', 'done']
        for step in steps[:nb_steps+1]:
            Status.create(uid=uid, status=step, fail=fail, context={}, date_created=date_created)
        return uid
    return factory

@pytest.fixture
def buildb1(db_factory):
    u1 = db_factory('buildb1owner', 'buildb1repo', 'buildb1branch', date_created=datetime.datetime(2000,1,1,0,0))
    return u1

@pytest.fixture
def buildb1bis(db_factory):
    u1bis = db_factory('buildb1owner', 'buildb1repobis', 'buildb1branchbis', date_created=datetime.datetime.now())
    return u1bis


@pytest.fixture
def buildb2(db_factory):
    return db_factory('buildb2owner', 'buildb2repo', 'buildb2branch', date_created=datetime.datetime.now())

@pytest.fixture
def valid_recette1(build):
    """
    Generate a temporary directory
    containing a dummy valid baguette.yaml.
    :returns: The directory path.
    :rtype: str
    """
    path = os.path.join(os.path.dirname(__file__))
    shutil.copy(os.path.join(path, 'recipes', 'Recette1'), os.path.join(build.base_dir, 'baguette.yaml'))

@pytest.fixture
def valid_recette2(build):
    """
    Generate a temporary directory
    containing a dummy valid baguette.yaml.
    :returns: The directory path.
    :rtype: str
    """
    path = os.path.join(os.path.dirname(__file__))
    shutil.copy(os.path.join(path, 'recipes', 'Recette2'), os.path.join(build.base_dir, 'baguette.yaml'))

@pytest.fixture()
def build():
    """
    Build fixture.
    """
    with mock.patch('git.Repo.clone_from', mock.Mock()):
        obj = cuisson.build.Build('owner', 'myrepo', 'mybranch', 'uid')
        obj.init()
        os.makedirs(obj.base_dir)
    return obj

@pytest.yield_fixture()
def api_namespace():
    api_namespace = mock.Mock(return_value={'status':0, 'result':{'count':1}})
    with mock.patch('cuisson.recipe.sel.request.Request.get', api_namespace):
        yield

@pytest.yield_fixture()
def docker_registry_build():
    registry = mock.Mock(return_value={})
    with mock.patch('docker.Client.images.build', registry):
        yield

@pytest.yield_fixture()
def docker_registry_buildko():
    registry = mock.Mock(return_value=[{'error':'error'}])
    with mock.patch('docker.Client.images.build', registry) as r:
        yield

@pytest.yield_fixture()
def docker_registry_push():
    registry = mock.Mock(return_value={})
    with mock.patch('docker.Client.images.push', registry):
        yield

@pytest.yield_fixture()
def docker_registry_pushko():
    registry = mock.Mock(return_value=["{'error':'error'}"])
    with mock.patch('docker.Client.images.push', registry) as r:
        yield

@pytest.yield_fixture()
def docker_registry_cleanup():
    registry = mock.Mock(return_value={})
    with mock.patch('docker.Client.images.remove', registry):
        yield

@pytest.yield_fixture()
def docker_registry_cleanupko():
    with mock.patch('docker.Client.images.remove') as r:
        r.side_effect= docker.errors.APIError('error', None, mock.Mock())
        yield r

def _rpc_server(callback_name):
    server = cuisson.service.Cuisson()
    farine.settings.load()
    farine.rpc.Server(service='cuisson', callback_name=callback_name, callback=getattr(server, callback_name), name='cuisson').start()

@pytest.fixture()
def rpc_server_factory(request, rabbitmq_proc, rabbitmq):
    def factory(callback_name):
        process = multiprocessing.Process(
            target=lambda:_rpc_server(callback_name),
        )
        def cleanup():
            process.terminate()
            clear_rabbitmq(rabbitmq_proc, rabbitmq)
        request.addfinalizer(cleanup)
        process.start()
        time.sleep(5)
        return process
    return factory
