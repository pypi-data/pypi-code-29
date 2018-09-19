from os.path import abspath


class DelimiterPathGenerator:
    def __init__(self, identifier_mapper, delimiter):
        self.identifier_mapper = identifier_mapper
        self.delimiter = delimiter
        self.identifiers = set()
        self.init_lines = ''

    def __call__(self, input_dir, output_dir):
        for file in input_dir.iterdir():
            file_name = file.name
            if self.delimiter in file.name:
                index = file_name.index(self.delimiter)
                identifier = file_name[:index]
                mapped = self.identifier_mapper(identifier)
                mapped_file_name = mapped + file_name[index:]
                self.identifiers.add(identifier)
            else:
                mapped_file_name = file_name

            yield (
                abspath(file),
                abspath(output_dir / mapped_file_name),
            )
