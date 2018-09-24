from invoke import Program, Collection

from release_name_generator import tasks

program = Program(namespace=Collection.from_module(tasks),
                  version='0.0.1')
