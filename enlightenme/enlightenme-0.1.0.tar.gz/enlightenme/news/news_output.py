import click


class NewsOutput:
    def __init__(self, content):
        self._content = content

    def write_to(self, file_name: str = None) -> None:
        if file_name is None:
            self.write_to_stdout()
        else:
            self.write_to_file(file_name)

    def write_to_stdout(self):
        click.echo(self._content)

    def write_to_file(self, file_name):
        with open(file_name, 'w') as f:
            f.write(self._content)
