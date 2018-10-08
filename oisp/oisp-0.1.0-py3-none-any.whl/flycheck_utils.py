# Copyright (c) 2017-2018, Intel Corporation
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#    * Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of Intel Corporation nor the names of its contributors
#      may be used to endorse or promote products derived from this software
#      without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""Helper methods for various parts.

These methods are meant to be used within the module.
"""

import json
import time
import re

import docker
import yaml
from pygments import highlight, lexers, formatters


TABLES_QUERY = ("""psql -U postgres -d iot -t -c "SELECT table_name FROM
information_schema.tables WHERE table_type='BASE TABLE' AND
table_schema='dashboard' AND table_name <> 'user_accounts';" """)

TRUNCATE_QUERY = """psql -U postgres -d iot -t -c 'TRUNCATE {} CASCADE;' """

DELETE_USERS_QUERY = ("""psql -U postgres -d iot -t -c "DELETE FROM
dashboard.users WHERE type != 'system';" """)


def camel_to_underscore(camel_str):
    """Convert a camelCase string to underscore_notation.

    This is useful for converting JSON style variable names
    to python style variable names.
    """
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', camel_str).lower()


def underscore_to_camel(underscore_str):
    """Convert a underscore_notation string to camelCase.

    This is useful for converting python style variable names
    to JSON style variable names.
    """
    return ''.join(w.title() if i else w
                   for i, w in enumerate(underscore_str.split('_')))


def pretty_dumps(json_dict):
    """Format a json dictionary to a colorful and indented string."""
    if json_dict is None:
        return "None"
    formatted_json = json.dumps(json_dict, indent=4)
    return highlight(formatted_json,
                     lexers.find_lexer_class_by_name("JSON")(),
                     formatters.find_formatter_class("terminal")())


def pretty_print(json_dict):
    """Pretty print a JSON dictionary."""
    print(pretty_dumps(json_dict))


def timestamp_in_ms(dt=None, dtype=int):
    """Convert given datetime into UNIX timestamp.

    If dt is None, current time will be used.
    dtype is the datatype returned (int or float).
    """
    if dt is None:
        in_ms = time.time()*1e3
    else:
        in_ms = time.mktime(dt.timetuple())*1e3
    return dtype(in_ms)


def load_yaml_with_include(path):
    """Load a yaml file with custom include statements.

    This will look for #include <PATH> and replace these lines
    with the content of the file on PATH. PATH can not contain
    whitespace.

    This is not implemented as !include with PyYaml as that
    would not preserve anchors.
    """
    with open(path, "r") as inputfile:
        lines = inputfile.readlines()
        for i, line in enumerate(lines):
            if line.startswith("#include "):
                includepath = line.split()[1]
                with open(includepath, "r") as includefile:
                    lines[i] = includefile.read() + "\n"
    text = "".join(lines)
    return yaml.load(text)


def clear_db(postgres_container):
    """Reset OISP database.

    Args:
    ----------
    postgres_container: Either container name as string or container object"""
    docker_client = docker.from_env()
    if isinstance(postgres_container, str):
        postgres_container = docker_client.containers.get(postgres_container)

    code, out = postgres_container.exec_run(DELETE_USERS_QUERY)
    assert code == 0, "Failed to delete non-system users"

    code, out = postgres_container.exec_run(TABLES_QUERY)
    assert code == 0, "Failed to receive table list."
    table_list = [i for i in out.decode("utf-8").split() if i and i != "users"]
    tables = ", ".join(['dashboard."{}"'.format(t) for t in table_list])
    code, out = postgres_container.exec_run(TRUNCATE_QUERY.format(tables))
    assert code == 0, "Failed to clear database: {}".format(out)


def add_user(dashboard_container, username, password, role):
    """Add a new user.

    Args:
    ----------
    dashboard_container: Either container name as string or container object
    username: username for new user
    password: password for new user
    role: user role, see OISP documentation for details.
    """
    docker_client = docker.from_env()
    if isinstance(dashboard_container, str):
        dashboard_container = docker_client.containers.get(dashboard_container)
    code, out = dashboard_container.exec_run("""
        node /app/admin addUser {} {} {} """.format(username, password, role))
    assert code == 0, "Failed to recreate user: {}".format(out)
