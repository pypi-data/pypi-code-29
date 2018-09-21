#-*- coding:utf-8 -*-
"""
Manage the build workflow.
"""
import os
import shutil
import git
import farine.settings
from cuisson.recipe import Recipe
from slugify import slugify

class Build(object):
    """
    Build the image in order to deploy.
    """
    def __init__(self, owner, repo, branch, uid):
        """
        Clone the repo to deploy.
        :param owner: The owner of the git repo.
        :type owner: str
        :param repo: The name of the git repo.
        :type repo: str
        :param branch: The repo branch.
        :type branch: str
        :param uid: The build unique identifier.
        :type uid: str
        """
        self.owner = owner
        self.repo = repo
        self.branch = branch.replace('refs/heads/', '')
        self.uid = uid
        tmp = farine.settings.cuisson['tmp']#pylint:disable=no-member
        self.git_uri = farine.settings.cuisson['git'].format(self.owner, self.repo)#pylint:disable=no-member
        self.base_dir = os.path.join(tmp, owner, repo, self.uid)

    def init(self):
        """
        Initialize the build : reset the path and clone the repo
        """
        #1. Reset the base_dir (if some artefacts were left)
        self.reset_path()
        #2. Clone and checkout the repo to the specified branch
        git.Repo.clone_from(self.git_uri, self.base_dir, branch=self.branch)
        #3. Slugify the branch
        self.branch = slugify(self.branch)

    def cleanup(self):
        """
        Cleanup the build :
        reset the path and cleanup the docker tag.
        """
        recipe = self.get_recipe()
        recipe.generate_definition()
        recipe.cleanup()
        self.reset_path()
        return True

    def reset_path(self, recreate=False):
        """
        Reset the repo path: remove it and recreate it.
        :param recreate: Recreate the path. Default to `True`.
        :type recreate: bool
        :rtype: bool
        """
        #1. Force removal of the folder
        try:
            shutil.rmtree(self.base_dir)
        except OSError:
            pass
        #2. Recreate it
        if recreate:
            os.makedirs(self.base_dir)
        return True

    def get_recipe(self):
        """
        Retrieve the config file baguette.yml.
        If not present, do not build.
        :returns: If there is a config file or not
        :rtype: bool
        """
        path = os.path.join(self.base_dir, 'baguette.yml')
        if os.path.exists(path):
            return Recipe(path, self.owner, self.repo, self.branch, self.uid)
        path = os.path.join(self.base_dir, 'baguette.yaml')
        if os.path.exists(path):
            return Recipe(path, self.owner, self.repo, self.branch, self.uid)
        return False
