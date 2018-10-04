from dalloriam import filesystem, shell


def build(build_path: str, image_name: str, tag: str = 'latest') -> None:
    """
    Builds a docker image from a directory.
    """
    # TODO: Give options to log or not.

    with filesystem.location(build_path):
        image_name = f'{image_name}:{tag}'
        shell.run([
            'docker',
            'build',
            '-t',
            image_name,
            '.'
        ], silent=True)