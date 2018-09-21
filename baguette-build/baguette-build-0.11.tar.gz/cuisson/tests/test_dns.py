#-*- coding:utf-8 -*-
import json
from .fixtures import *

def test_set_dns_public(queue_factory, rabbitmq, rabbitmq_proc, build, valid_recette2, api_namespace):
    """
    Test than went we build a public app, a dns message is sent.
    """
    service = cuisson.service.Cuisson()
    recipe = build.get_recipe()
    recipe.generate_definition()
    exc, queue = queue_factory('queue', 'dns', 'create-record')
    #
    assert service.set_dns(recipe.definition['private'], recipe.definition['domain_name']) is True
    message = next(queue.consume())
    assert json.loads(message.body) == {"domain": "mybranch.myrepo.owner.projects.baguette.io"}
    clear_rabbitmq(rabbitmq_proc, rabbitmq)

def test_set_dns_private(queue_factory, rabbitmq, rabbitmq_proc, build, valid_recette1):
    """
    Test than went we build a private app, no dns message is sent.
    """
    service = cuisson.service.Cuisson()
    recipe = build.get_recipe()
    recipe.generate_definition()
    exc, queue = queue_factory('queue', 'dns', 'create-record')
    #
    assert service.set_dns(recipe.definition['private'], recipe.definition['domain_name']) is False
