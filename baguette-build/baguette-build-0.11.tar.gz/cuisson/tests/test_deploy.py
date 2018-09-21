#-*- coding:utf-8 -*-
import json
from .fixtures import *

def test_deploy(queue_factory, rabbitmq, rabbitmq_proc, build, valid_recette2, api_namespace):
    """
    Test than went we build a public app, a dns message is sent.
    """
    service = cuisson.service.Cuisson()
    recipe = build.get_recipe()
    recipe.generate_definition()
    exc, queue = queue_factory('queue', 'deployment', 'create')
    #
    assert service.deploy(recipe.definition) is True
    message = next(queue.consume())
    assert json.loads(message.body) == {"definition": recipe.definition}
    clear_rabbitmq(rabbitmq_proc, rabbitmq)
