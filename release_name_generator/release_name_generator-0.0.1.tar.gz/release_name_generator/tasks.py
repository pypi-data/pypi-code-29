from invoke import task

from release_name_generator.names_generator import NameGenerator


@task(default=True)
def generate_name_by_ref(c, ref_name):
    name_generator = NameGenerator()
    print(name_generator.generate_name_by_ref(ref_name))


@task
def generate_name_by_date(c, date_from, date_to):
    name_generator = NameGenerator()
    print(name_generator.generate_name_by_date(date_from, date_to))
