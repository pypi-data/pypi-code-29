import os
import uuid
import yaml

from playneta.service import template
from playneta.service.target import Target


def help(parser):
    parser.add_argument('config',
                        nargs='?',
                        default='service.yaml',
                        help='Service API description file')


def main(args, file_root):
    service_config = yaml.load(file(args.config, 'r'))
    service = service_config['service']

    for target_options in service_config['targets']:
        target_context = Target(file_root, target_options)

        _split(template.render(target_context, service), target_context.file_separator())


def _split(content, separator):
    current_file = None
    name_padding = len(separator)

    for line in content:
        if line.startswith(separator):
            if current_file is not None:
                current_file.flush()
                current_file.close()

            file_name = line[name_padding:]
            path, _ = os.path.split(file_name)

            if not os.path.exists(path):
                os.makedirs(path)

            current_file = open(file_name, 'w+')
        else:
            if current_file is not None:
                current_file.write(line)
                current_file.write('\n')
