import os
from os.path import abspath

from ahocorasick import Automaton


class AhoCorasickPathGenerator:
    def __init__(self, identifier_mapper, identifiers):
        self.identifier_mapper = identifier_mapper
        self.identifiers = identifiers
        self.automaton = Automaton()
        for identifier in identifiers:
            mapped = identifier_mapper(identifier)
            self.automaton.add_word(identifier, (len(identifier), mapped))
        self.automaton.make_automaton()
        self.dest_dirs = set()

    def blind_path(self, path):
        out = ''
        idx = 0
        for end_position, (length, mapped) in self.automaton.iter(path):
            end_idx = end_position + 1
            start_idx = end_idx - length
            out += path[idx:start_idx] + mapped
            idx = end_idx
        out += path[idx:]
        return out

    def __call__(self, input_dir, output_dir):
        for root, dirs, files in os.walk(input_dir):
            for name in files:
                source_file_name = os.path.join(root, name)
                relpath = os.path.relpath(
                    source_file_name,
                    start=input_dir,
                )
                dest_file_name = output_dir / self.blind_path(relpath)
                self.dest_dirs.add(abspath(dest_file_name.parent))
                yield (
                    abspath(source_file_name),
                    abspath(dest_file_name),
                )

    @property
    def init_lines(self):
        return "\n".join(
            f'mkdir -p "{dest_dir}"'
            for dest_dir in self.dest_dirs
        ) + "\n"
