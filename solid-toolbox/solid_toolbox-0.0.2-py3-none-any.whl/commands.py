#!/usr/bin/env python3

from pathlib import Path
import click


class FolderType(click.ParamType):
    name = 'Folder'

    def __init__(self):
        self.converter = click.Path(
            exists=False,
            file_okay=False,
            dir_okay=True,
            writable=True,
            readable=True,
            resolve_path=True,
        )

    def convert(self, value, param, ctx):
        return Path(self.converter.convert(value, param, ctx))


@click.group()
def run():
    """Utilities for manipulating SolidPython and OpenSCAd code"""
    pass


@run.command()
@click.argument('project_path',
                type=FolderType())
def new(project_path):
    """Generates a new project located at the given path"""
    name = project_path.name
    generate_out_path = project_path / 'generated'
    model_generator_path = project_path / f'{name}.py'

    project_path.mkdir(parents=True, exist_ok=True)
    generate_out_path.mkdir(parents=True, exist_ok=True)
    model_generator_path.write_text(TEMPLATE.format(name=name))


TEMPLATE = '''#!/usr/bin/env python3

from solid import *
from solid.utils import *
from solid_toolbox import *


def generate_model():
    return rotate(60, x_axis)(
        cube(Vec(3, 3, 3), center=True),
    )


if __name__ == '__main__':
    model = generate_model()
    scad_render_to_file(
        model,
        'generated/{name}.scad',
        include_orig_code=False,
    )
'''
