from ghostbot import Ghostbot, GhostbotProfile, StatusCode, Scaffolds
from ghostbot.core import Basis, Service
from ghostbot.utils.logger import Logger
from ghostbot.utils.os import Computer, FileSystem as fs
from ghostbot.utils.datetime import Datetime
from ghostbot.utils.string import String
from ghostbot.utils.template import TemplateEngine
from ghostbot.utils.json import Json
from .repository import Repository


class Wizard(Basis, Service):
    PROJECTS_JSON = "projects.json"
    PROJECTS_SCHEMA = "projects"
    PROJECTS_VERSION = "0.1.0"

    def __init__(self):
        super().__init__()
        self.logger = Logger(__name__)
        self._engine = TemplateEngine()
        self._repository = Repository()
        self._projects = None

    def startup(self):
        pass

    def shutdown(self):
        pass

    def execute(self, target, name, directory):
        if target == Scaffolds.PROJECT:
            self.project(name, directory)
        elif target == Scaffolds.AGENT:
            self.agent(name, directory)
        elif target == Scaffolds.CONTAINER:
            self.container(name, directory)
        elif target == Scaffolds.REACTOR:
            self.reactor(name, directory)
        else:
            self.error(StatusCode[508], target)

    def setup(self, signature=None, project_name=None, project_home=None):
        if signature:
            Ghostbot.signature(signature)
            self._repository.activate_project(signature)
        if project_name:
            Ghostbot.project_name(project_name)
        if project_home:
            Ghostbot.project_home(project_home)

    def project(self, name, directory=None):
        if directory is None:
            directory = fs.homedir()
        directory = fs.join(directory, name)
        if self._load_projects():
            if not fs.exists(directory):
                if fs.exists(fs.parent(directory)):
                    params = {
                        "now": Datetime.now(to_string=True),
                        "today": Datetime.today(to_string=True),
                        "project_home": directory,
                        "project_name": name
                    }
                    fs.make_directory(directory)
                    self.logger.info(StatusCode[131], directory)
                    self._project_generator(directory, self._projects["projects"], params)
                    signature = self._repository.append_project(name, directory, self.PROJECTS_VERSION, Computer.name())
                    self.setup(signature, name, directory)
                else:
                    self.error(StatusCode[230], fs.parent(directory))
            else:
                self.error(StatusCode[231], directory)
        else:
            self.error(StatusCode[201], __name__)

    def agent(self, name, directory=None):
        args = {
            "target": Scaffolds.AGENT,
            "name": name,
            "directory": directory,
            "marker": "sample_agent.py.tpl",
            "template": "agent.py.tpl",
            "status": 131
        }
        self._target_generator(args)

    def container(self, name, directory=None):
        args = {
            "target": Scaffolds.CONTAINER,
            "name": name,
            "directory": directory,
            "marker": "sample_container.py.tpl",
            "template": "container.py.tpl",
            "status": 132
        }
        self._target_generator(args)

    def reactor(self, name, directory=None):
        args = {
            "target": Scaffolds.REACTOR,
            "name": name,
            "directory": directory,
            "marker": "sample_reactor.py.tpl",
            "template": "reactor.py.tpl",
            "status": 133
        }
        self._target_generator(args)

    def _load_projects(self):
        if not self._projects:
            path = fs.join(GhostbotProfile.assets_resources, self.PROJECTS_JSON)
            self.logger.info(StatusCode[110].format(path))
            if fs.exists(path):
                projects = Json.load(path)
                if projects["schema"] == self.PROJECTS_SCHEMA:
                    if projects["version"] == self.PROJECTS_VERSION:
                        self._projects = projects
                    else:
                        self.error(StatusCode[212], projects["version"], path)
                else:
                    self.error(StatusCode[211], projects["schema"], path)
            else:
                self.error(StatusCode[210], path)
        return self._projects is not None

    # TODO projects.json leaf format should be change, like a ('.gitignore', 'gitignore.tpl')
    def _project_generator(self, base, dictionary, params):
        for key, value in dictionary.items():
            if isinstance(value, dict):
                path = fs.join(base, key)
                self.logger.info("CREATE DIRECTORY: {}".format(path))
                fs.make_directory(path)
                self._project_generator(path, value, params)
            elif isinstance(value, str):
                if value[-1] == "/":
                    path = fs.join(base, value[:-1])
                    self.logger.info("CREATE DIRECTORY: {}".format(path))
                    fs.make_directory(path)
                elif value[-4:] == ".tpl":
                    output_file = fs.join(base, value[:-4])
                    template_file = fs.join(GhostbotProfile.assets_templates, value)
                    self.logger.info("CREATE FILE:      {}".format(output_file))
                    self._engine.build(output_file, template_file, params)
                else:
                    self.logger.error(StatusCode[232], value)
            else:
                self.logger.error(StatusCode[233], value)

    def _find(self, target, path, dictionary):
        result = None
        for key, value in dictionary.items():
            if isinstance(value, dict):
                result = self._find(target, fs.join(path, key), value)
                if result is not None:
                    break
            elif isinstance(value, str):
                if value == target:
                    result = path
            else:
                self.logger.error(StatusCode[233], value)
        return result

    def _target_generator(self, args):
        if self._load_projects():
            if not Ghostbot.signature():
                self._repository.active_project()
            project_home = Ghostbot.project_home()
            if fs.exists(project_home):
                path = self._find(args["marker"], project_home, self._projects["projects"])
                if path:
                    if args["directory"]:
                        path = fs.join(path, args["directory"])
                        fs.make_directory(path)
                    class_name = "{}{}".format(String.pascal(args["name"]), String.pascal(args["target"].value))
                    file_name = "{}_{}.py".format(String.lower(args["name"]), String.lower(args["target"].value))
                    params = {"class_name": class_name, "file_name": file_name}
                    output_file = fs.join(path, file_name)
                    template_file = fs.join(GhostbotProfile.assets_templates, args["template"])
                    if not fs.exists(output_file):
                        signature = Ghostbot.signature()
                        self.logger.info(StatusCode[args["status"]], output_file)
                        self._engine.build(output_file, template_file, params)
                        self._repository.append_class(signature, args["target"].value, class_name, file_name)
                    else:
                        self.error(StatusCode[234], output_file)
                else:
                    self.error(StatusCode[503], args["marker"], __name__)
            else:
                self.error(StatusCode[505], project_home)
        else:
            self.error(StatusCode[201], __name__)
