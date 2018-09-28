# Copyright 2018 Nathan Sommer and Ben Coleman
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Provides a template string to use when writing run_action.sh. The following
named placeholders must be replaced using format():

    timeout - the number of seconds before the action script is killed
    memory_limit - the memory limit for the tests, in MB
    interpreter - the interpreter to use to run the action script
    script_name - the name of the action script
"""

template = '''#!/bin/bash

GLOBAL_TIMEOUT={global_timeout}
GLOBAL_MEM_LIMIT_MB={global_memory_limit}

GLOBAL_MEM_LIMIT_KB=$(($GLOBAL_MEM_LIMIT_MB * 1024))

ulimit -v $GLOBAL_MEM_LIMIT_KB

trap 'kill -INT -$pid' INT

timeout $GLOBAL_TIMEOUT {interpreter} {script_name} "$@" &

pid=$!

wait $pid
'''
