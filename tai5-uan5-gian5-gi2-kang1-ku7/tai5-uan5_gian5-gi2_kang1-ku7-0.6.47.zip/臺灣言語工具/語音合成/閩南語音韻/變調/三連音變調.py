# -*- coding: utf-8 -*-
from 臺灣言語工具.語音合成.閩南語音韻.變調.規則變調 import 規則變調


class 三連音變調(規則變調):
    喉入聲變調規則 = {'4': '2', '8': '9'}
    入聲變調規則 = {'4': '8', '8': '9'}
    變調規則 = {'1': '9', '2': '1', '3': '2', '5': '9', '7': '9'}
