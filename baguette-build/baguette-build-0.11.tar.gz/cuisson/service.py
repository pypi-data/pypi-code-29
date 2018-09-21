#-*- coding:utf-8 -*-
#pylint:disable=line-too-long,no-self-use
"""
Entrypoint for the build.
"""
import uuid
from cuisson.build import Build
from cuisson.models import Build as Model, Status
from farine.connectors.sql import fn
import farine.amqp
import farine.rpc

class Cuisson(object):
    """
    Build the app:
    - clone it
    - build the docker image
    - push the docker image
    """

    @farine.rpc.method()
    def list(self, owner, offset=0, limit=10):
        """
        Get the last build records given an owner.
        :param owner: The owner to retrieve the builds.
        :type owner: str
        :param offset: The offset to start retrieving builds. Default to 0.
        :type limit: int
        :param limit: The number of builds to retrieve. Default to 10.
        :type limit: int
        :returns: The owner builds.
        :type: dict
        """
        output = {'count':0, 'next':None, 'previous':None, 'results':[]}
        output['count'] = Model.select(fn.count(fn.distinct(Model.uid))).where(Model.owner == owner).scalar()
        builds = Model.select().where(Model.owner == owner).order_by(Model.date_created.desc()).offset(offset).limit(limit)
        for build in builds:
            query = Status.select().where(Status.uid == build.uid).order_by(Status.date_created.desc()).get()
            output['results'].append(build.to_json(extras={'status':query.status}))
        return output

    @farine.rpc.method()
    def detail(self, owner, uid):
        """
        Given an owner and an uid, retrieve the details.
        :param owner: The owner to retrieve the build details.
        :type owner: str
        :param uid: The build uid.
        :type uid: str
        :returns: The build details.
        :type: list
        """
        output = {'count':0, 'next':None, 'previous':None, 'results':[]}
        #1. Check permission
        exist = Model.select().where(Model.owner == owner, Model.uid == uid).scalar()
        if not exist:
            return output
        # 2. Retrieve all the status
        output['count'] = Status.select().where(Status.uid == uid).count()
        query = Status.select().where(Status.uid == uid).order_by(Status.date_created.desc())
        output['results'] = [q.to_json() for q in query]
        return output

    @farine.rpc.method()
    def post_receive(self, owner, repo, branch):
        """
        Called after a completed push.
        Entrypoint of the deployment process.
        TODO:split this method.

        :param owner: The owner of the git repo.
        :type owner: str
        :param repo: The name of the git repo.
        :type repo: str
        :param branch: The repo branch.
        :type branch: str
        :rtype:None
        """
        uid = uuid.uuid4().hex
        Model.create(owner=owner, repo=repo, branch=branch, uid=uid)
        step = Status.create(uid=uid, status='clone', context={'repo':repo, 'branch':branch})
        yield step.to_json()
        #1. Instanciate the build
        build = Build(owner, repo, branch, uid)
        build.init()
        #2. Retrieve the recipe
        step = Status.create(uid=uid, status='generate-recipe', context={})
        #TODO: the recipe/definition must be in its own service
        yield step.to_json()
        recipe = build.get_recipe()
        if not recipe:
            step.fail = True
            step.save()
            yield step.to_json()
        else:
            #3. Generate the definition
            #TODO: the recipe/definiton must be in its own service
            step = Status.create(uid=uid, status='generate-definition', context={})
            yield step.to_json()
            recipe.generate_definition()
            #4. Generate the `DockerFile`
            step = Status.create(uid=uid, status='generate-dockerfile', context={})
            yield step.to_json()
            recipe.generate_dockerfile()
            #5. Send the dns record update
            step = Status.create(uid=uid, status='generate-dns', context={'domain':recipe.definition['domain_name']})
            yield step.to_json()
            self.set_dns(recipe.definition['private'], recipe.definition['domain_name'])#pylint:disable=no-value-for-parameter
            #6. Create a docker image
            step = Status.create(uid=uid, status='build-docker', context={})
            yield step.to_json()
            if not recipe.build_dockerfile():
                step.fail = True
                step.save()
                build.cleanup()
                yield step.to_json()
            else:
                #7. Push the docker image
                step = Status.create(uid=uid, status='push-docker', context={})
                yield step.to_json()
                if not recipe.push_dockerfile():
                    step.fail = True
                    step.save()
                    build.cleanup()
                    yield step.to_json()
                else:
                    #8. Delete everything
                    build.cleanup()#TODO:async
                    #9. Over
                    self.deploy(recipe.definition)#pylint:disable=no-value-for-parameter
                    step = Status.create(uid=uid, status='done', context={})
                    yield step.to_json()

    @farine.amqp.publish(exchange='dns', routing_key='create-record')
    def set_dns(self, publish, private, domain):
        """
        Send a message to create/update the app domain.
        :param private: The app is private.
        :type private: bool
        :param domain: The app domain name
        :type domain: str
        :rtype: bool
        """
        if not private:
            publish({'domain':domain})
            return True
        return False

    @farine.amqp.publish(exchange='deployment', routing_key='create')
    def deploy(self, publish, definition):
        """
        Send a message to start the deployment.
        :param definition: The definition of the app to launch.
        :type definiton: dict
        :rtype: bool
        """
        publish({'definition':definition})
        return True
