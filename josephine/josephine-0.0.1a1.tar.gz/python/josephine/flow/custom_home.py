

from kabaret import flow

from kabaret.app.actors.flow.generic_home_flow import (
    AbstractHomeRoot, Home, ProjectsMap, CreateProjectAction
)


banner = '<H1>Welcome to Josephine</H1>'


class CreateJosephineProjectAction(CreateProjectAction):
    '''
    This overrides the default CreateProjectAction
    with an hidden project_type value that returns
    our flow.
    '''
    project_type = flow.Param(
        'josephine.flow.josephine_project.JosephineProject',
        None
    ).ui(hidden=True)

    def get_buttons(self):
        return super(CreateJosephineProjectAction, self).get_buttons()[-1:]


class SimpleProjectsMap(ProjectsMap):

    # Override the create_project action with our simpler one:
    create_project = flow.Child(CreateJosephineProjectAction).ui(group='Admin')


# Hide the toggle_project_type action, we have only one project type:
SimpleProjectsMap.toggle_project_type.ui(hidden=True)


class JosephineHome(Home):

    banner = flow.Label(banner)

    projects = flow.Child(SimpleProjectsMap)


class JosephineHomeRoot(AbstractHomeRoot):

    Home = flow.Child(JosephineHome)
