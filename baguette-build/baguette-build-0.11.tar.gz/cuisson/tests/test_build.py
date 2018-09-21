#-*- coding:utf-8 -*-
"""
Test the build process.
"""
#pylint:disable=wildcard-import,unused-wildcard-import,redefined-outer-name
import json
from .fixtures import *

def test_init():
    """
    Test that we clone the repo.
    """
    build = cuisson.build.Build(gen_str(), gen_str(), 'mybranch', gen_str())
    git_mock = mock.Mock()
    with mock.patch('git.Repo.clone_from', git_mock):
        build.init()
        git_mock.assert_called_once()

def test_reset_path(build):
    """
    Test that reset_path() delete the repo path.
    """
    assert os.path.exists(build.base_dir)
    build.reset_path()
    assert not os.path.exists(build.base_dir)

def test_get_recipe(build, valid_recette1):
    """
    Test that get_recipe() retrieve a Recipe
    when there is a valid recipe.
    """
    assert isinstance(build.get_recipe(), cuisson.recipe.Recipe)

def test_no_get_recipe(build):
    """
    Test that get_recipe() returns False
    when there is an invalid recipe.
    """
    assert build.get_recipe() is False

def test_cleanup(build, valid_recette1):
    """
    Test that build.cleanup() calls build.reset_path()
    and recipe.cleanup().
    """
    assert os.path.exists(build.base_dir)
    assert build.get_recipe()
    #
    recipe_mock = mock.Mock()
    with mock.patch('cuisson.recipe.Recipe.cleanup', recipe_mock):
        build.cleanup()
        assert not os.path.exists(build.base_dir)
        recipe_mock.assert_called_once()

def test_full_post_receive(queue_factory, rabbitmq, rabbitmq_proc, docker_registry_build, docker_registry_push, docker_registry_cleanup):
    """
    Test the full workflow when cuisson is called by the git hook.
    """
    owner, repo, branch  = gen_str(), gen_str(), gen_str()
    exc, queue = queue_factory('queue', 'deployment', 'create')
    #1. Need to mock git clone
    def fake_clone(git_uri, base_dir, branch):
        os.makedirs(base_dir)
        path = os.path.join(os.path.dirname(__file__))
        shutil.copy(os.path.join(path, 'recipes', 'Recette1'), os.path.join(base_dir, 'baguette.yaml'))
    with mock.patch('git.Repo.clone_from', mock.MagicMock(side_effect=fake_clone)):
        messages = list(json.loads(m) for m in cuisson.service.Cuisson().post_receive(owner, repo, branch))
        assert messages[-1]['fail'] == False
        assert messages[-1]['status'] == 'done'
    message = next(queue.consume())
    assert json.loads(message.body).get('definition')
    clear_rabbitmq(rabbitmq_proc, rabbitmq)
