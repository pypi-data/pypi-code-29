# -*- coding: utf-8 -*-
#
# This file is part of ProjectBubble.
#
# (c) Giant - MouGuangyi <mouguangyi@ztgame.com>
#
# For the full copyright and license information, please view the LICENSE
# file that was distributed with this source code.
#

import os
from gxbubble import shell


class Unity:
    __path = ''

    def __init__(self, unity_path):
        self.__path = os.environ.get(unity_path, '')

    def valid(self):
        return os.path.exists(self.__path)

    def run(self, **options):
        if not self.valid():
            raise FileNotFoundError('CANNOT find Unity!')

        parameters = ' '
        for k, v in options.items():
            if v in (True, False):
                parameters += (' -' + k) if v else ''
            else:
                parameters += (' -' + k + ' ' + v)

        return shell(self.__path + parameters)

