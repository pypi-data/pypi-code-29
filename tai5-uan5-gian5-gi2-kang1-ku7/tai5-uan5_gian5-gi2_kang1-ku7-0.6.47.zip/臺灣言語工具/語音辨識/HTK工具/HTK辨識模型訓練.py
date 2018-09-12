# -*- coding: utf-8 -*-
import itertools
import os
from os.path import join
import re
import shutil
from 臺灣言語工具.語音合成.語音標仔轉換 import 語音標仔轉換
from 臺灣言語工具.語音辨識.HTK工具.HTK辨識模型 import HTK辨識模型
from 臺灣言語工具.語音辨識.HTK工具.HTK語料處理 import HTK語料處理
from 臺灣言語工具.語音辨識.HTK工具.安裝HTK語音辨識程式 import 安裝HTK語音辨識程式


class HTK辨識模型訓練(HTK語料處理):
    MLF檔開始符號 = '#!MLF!#'
    MLF檔逐音檔結束符號 = '.'
    孤音混合數 = [1, 2, 4, 8, 12, 16, 24, 32]
    三連音混合數 = [1, 2, 4, 6, 8]
    調整參數重估擺 = 20
    混合數重估擺 = 20
    混合數上尾重估擺 = 40
    上尾重估擺 = 60

    @classmethod
    def 訓練原本標音辨識模型(cls, 音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑=安裝HTK語音辨識程式.htk執行檔目錄()):
        (全部特徵檔, _全部標仔檔), (_原來音類檔, _原來音節檔, 原來聲韻類檔, 原來聲韻檔), 做好的初步模型檔 = cls._收集語料而且訓練原始音標初步模型(
            音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑
        )
        原來加混合模型 = cls._加混合數(
            執行檔路徑, 資料目錄, 全部特徵檔,
            原來聲韻類檔, 原來聲韻檔, 做好的初步模型檔,
            cls.孤音混合數, 估幾擺=cls.混合數重估擺, 上尾估幾擺=cls.混合數上尾重估擺
        )
        return HTK辨識模型(
            音節聲韻對照檔=音節聲韻對照檔, 聲韻類檔=原來聲韻類檔, 模型參數檔=原來加混合模型
        )

    @classmethod
    def 訓練拄好短恬辨識模型(cls, 音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑=安裝HTK語音辨識程式.htk執行檔目錄()):
        _全部特徵檔, _新拄好短恬音節檔, _新拄好短恬聲韻檔, 加短恬辨識模型 = cls._訓練拄好短恬辨識模型閣回傳過程(
            音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑
        )
        return 加短恬辨識模型

    @classmethod
    def 訓練三連音辨識模型(cls, 音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑=安裝HTK語音辨識程式.htk執行檔目錄()):
        (全部特徵檔, 全部標仔檔), (原來音類檔, 原來音節檔, 原來聲韻類檔, _原來聲韻檔), 做好的初步模型檔 = cls._收集語料而且訓練原始音標初步模型(
            音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑)

        加恬聲韻類檔, 拄好短恬的重估模型, 新拄好短恬聲韻檔, _新拄好短恬音節檔 = cls._加短恬而且共時間傷短的短恬提掉(
            執行檔路徑, 資料目錄, 全部特徵檔, 全部標仔檔, 音節聲韻對照檔, 原來音類檔, 原來音節檔, 原來聲韻類檔, 做好的初步模型檔)

        三連音全部縛做伙聲韻類檔, 三連音全部縛做伙模型 = cls._三連音重估縛做伙加混合佮加無看過的音(
            執行檔路徑, 資料目錄, 全部特徵檔, 音節聲韻對照檔, 新拄好短恬聲韻檔, 加恬聲韻類檔, 拄好短恬的重估模型)

        return HTK辨識模型(
            音節聲韻對照檔=音節聲韻對照檔, 聲韻類檔=三連音全部縛做伙聲韻類檔, 模型參數檔=三連音全部縛做伙模型
        )

    @classmethod
    def 快速對齊聲韻(cls, 音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑=安裝HTK語音辨識程式.htk執行檔目錄()):
        (全部特徵檔, _全部標仔檔), (_原來音類檔, _原來音節檔, 原來聲韻類檔, 原來聲韻檔), 做好的初步模型檔 = cls._收集語料而且訓練原始音標初步模型(
            音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑
        )
        快速辨識模型 = HTK辨識模型(
            音節聲韻對照檔=音節聲韻對照檔, 聲韻類檔=原來聲韻類檔, 模型參數檔=做好的初步模型檔
        )
        對齊結果資料夾 = cls._細項目錄(資料目錄, '快速對齊結果')
        return 快速辨識模型.對齊聲韻(原來聲韻檔, 全部特徵檔, 對齊結果資料夾)

    @classmethod
    def 對齊聲韻閣加短恬(cls, 音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑=安裝HTK語音辨識程式.htk執行檔目錄()):
        全部特徵檔, _新拄好短恬音節檔, 新拄好短恬聲韻檔, 加短恬辨識模型 = cls._訓練拄好短恬辨識模型閣回傳過程(
            音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑
        )
        對齊結果資料夾 = cls._細項目錄(資料目錄, '對齊結果')
        return 加短恬辨識模型.對齊聲韻(新拄好短恬聲韻檔, 全部特徵檔, 對齊結果資料夾)

    @classmethod
    def 對齊音節閣加短恬(cls, 音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑=安裝HTK語音辨識程式.htk執行檔目錄()):
        全部特徵檔, 新拄好短恬音節檔, _新拄好短恬聲韻檔, 加短恬辨識模型 = cls._訓練拄好短恬辨識模型閣回傳過程(
            音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑
        )
        對齊結果資料夾 = cls._細項目錄(資料目錄, '對齊結果')
        return 加短恬辨識模型.對齊音節(新拄好短恬音節檔, 全部特徵檔, 對齊結果資料夾)

    @classmethod
    def _訓練拄好短恬辨識模型閣回傳過程(cls, 音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑=安裝HTK語音辨識程式.htk執行檔目錄()):
        (全部特徵檔, 全部標仔檔), (原來音類檔, 原來音節檔, 原來聲韻類檔, _原來聲韻檔), 做好的初步模型檔 = cls._收集語料而且訓練原始音標初步模型(
            音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑)

        加恬聲韻類檔, 拄好短恬的重估模型, 新拄好短恬聲韻檔, 新拄好短恬音節檔 = cls._加短恬而且共時間傷短的短恬提掉(
            執行檔路徑, 資料目錄, 全部特徵檔, 全部標仔檔, 音節聲韻對照檔, 原來音類檔, 原來音節檔, 原來聲韻類檔, 做好的初步模型檔)

        短恬加混合模型 = cls._加混合數(
            執行檔路徑, 資料目錄, 全部特徵檔,
            加恬聲韻類檔, 新拄好短恬聲韻檔, 拄好短恬的重估模型,
            cls.孤音混合數, 估幾擺=cls.混合數重估擺, 上尾估幾擺=cls.混合數上尾重估擺
        )

        return 全部特徵檔, 新拄好短恬音節檔, 新拄好短恬聲韻檔, HTK辨識模型(
            音節聲韻對照檔=音節聲韻對照檔, 聲韻類檔=加恬聲韻類檔, 模型參數檔=短恬加混合模型
        )

    @classmethod
    def _收集語料而且訓練原始音標初步模型(cls, 音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄, 執行檔路徑):
        全部語料 = cls._揣全部語料(音檔目錄, 標仔目錄)

        全部特徵檔 = os.path.join(資料目錄, '全部特徵檔.scp')
        全部標仔檔 = os.path.join(資料目錄, '全部標仔檔.scp')
        os.makedirs(資料目錄, exist_ok=True)
        cls._揣特徵而且算(執行檔路徑, 資料目錄, 全部語料, 全部特徵檔)

        原始目錄 = cls._細項目錄(資料目錄, '原始標音目錄')
        原來音類檔 = os.path.join(原始目錄, '原來音類檔.list')
        原來音節檔 = os.path.join(原始目錄, '原來音節檔.mlf')
        原來聲韻類檔 = os.path.join(原始目錄, '原來聲韻類檔.list')
        原來聲韻檔 = os.path.join(原始目錄, '原來聲韻檔.mlf')

        全部標仔 = []
        for _語料名, _音檔所在, 標仔所在 in 全部語料:
            全部標仔.append(標仔所在)
        cls._陣列寫入檔案(全部標仔檔, 全部標仔)
        cls._標仔收集起來(執行檔路徑, 全部標仔檔, 原始目錄, 原來音類檔, 原來音節檔)
        cls._標仔切做聲韻(執行檔路徑, 原來音節檔, 音節聲韻對照檔, 原始目錄, 原來聲韻類檔, 原來聲韻檔)

        初步模型檔 = cls._建立初步模型(執行檔路徑, 原始目錄, 全部特徵檔, 原來聲韻類檔, 原來聲韻檔)
        做好的初步模型檔 = cls._模型重估(
            執行檔路徑, 原始目錄, 全部特徵檔,
            原來聲韻類檔, 原來聲韻檔, 初步模型檔, 估幾擺=cls.上尾重估擺
        )

        return (全部特徵檔, 全部標仔檔), (原來音類檔, 原來音節檔, 原來聲韻類檔, 原來聲韻檔), 做好的初步模型檔

    @classmethod
    def _加短恬而且共時間傷短的短恬提掉(cls,
                         執行檔路徑, 資料目錄,
                         全部特徵檔, 全部標仔檔,
                         音節聲韻對照檔, 原來音類檔, 原來音節檔, 原來聲韻類檔,
                         做好的初步模型檔):
        短恬目錄 = cls._細項目錄(資料目錄, '短恬目錄')
        加恬音節檔 = os.path.join(短恬目錄, '加恬音節檔.mlf')
        加恬音類檔 = os.path.join(短恬目錄, '加恬音類檔.list')
        加恬聲韻類檔 = os.path.join(短恬目錄, '加恬聲韻類檔.list')
        加恬聲韻檔 = os.path.join(短恬目錄, '加恬聲韻檔.mlf')

        cls._音類標仔檔加短恬(原來音類檔, 加恬音類檔)
        cls._音節標仔檔加短恬(原來音節檔, 加恬音節檔)
        cls._標仔切做聲韻(執行檔路徑, 加恬音節檔, 音節聲韻對照檔, 短恬目錄, 加恬聲韻類檔, 加恬聲韻檔)

        # 先提掉sp短恬，才閣加佮sil長恬中央仝款的模型參數
        無短恬的模型 = os.path.join(資料目錄, '提掉短恬的模型.macro')
        cls._模型提掉短恬(執行檔路徑, 短恬目錄,
                    做好的初步模型檔, 原來聲韻類檔, 無短恬的模型)
        加短恬的模型 = os.path.join(短恬目錄, '加短恬的模型.macro')
        cls._模型加短恬(無短恬的模型, 加短恬的模型)

        加短恬縛好模型 = os.path.join(短恬目錄, '加短恬縛好模型.macro')
        cls._恬音佮短恬愛縛做伙(執行檔路徑, 短恬目錄, 加短恬的模型, 加短恬縛好模型, 加恬聲韻類檔)
        加短恬的重估模型 = cls._模型重估(
            執行檔路徑, 短恬目錄, 全部特徵檔,
            加恬聲韻類檔, 加恬聲韻檔, 加短恬縛好模型, 估幾擺=cls.調整參數重估擺
        )

        加恬辨識模型 = HTK辨識模型(音節聲韻對照檔=音節聲韻對照檔, 聲韻類檔=加恬聲韻類檔, 模型參數檔=加短恬的重估模型)
        對齊音節結果目錄 = 加恬辨識模型.對齊音節(
            加恬音節檔, 全部特徵檔, 短恬目錄, 執行檔路徑=執行檔路徑
        )
        新拄好短恬全部標仔檔 = os.path.join(短恬目錄, '新拄好短恬全部標仔檔.scp')
        cls._陣列寫入檔案(新拄好短恬全部標仔檔, cls._標仔換目錄(全部標仔檔, 對齊音節結果目錄))

        _新對齊短恬音節類檔 = os.path.join(短恬目錄, '新對齊短恬音節類檔.list')
        新對齊短恬音節檔 = os.path.join(短恬目錄, '新對齊短恬音節檔.mlf')
        cls._標仔收集起來(執行檔路徑, 新拄好短恬全部標仔檔,
                    短恬目錄, _新對齊短恬音節類檔, 新對齊短恬音節檔)
        新拄好短恬音節檔 = os.path.join(短恬目錄, '新拄好短恬音節檔.mlf')
        cls._提掉傷短的短恬(新對齊短恬音節檔, 新拄好短恬音節檔)

        _新拄好短恬聲韻類檔 = os.path.join(短恬目錄, '新拄好短恬聲韻類檔.list')
        新拄好短恬聲韻檔 = os.path.join(短恬目錄, '新拄好短恬聲韻檔.mlf')
        cls._標仔切做聲韻(執行檔路徑, 新拄好短恬音節檔, 音節聲韻對照檔, 短恬目錄, _新拄好短恬聲韻類檔, 新拄好短恬聲韻檔)
        拄好短恬的重估模型 = cls._模型重估(
            執行檔路徑, 短恬目錄, 全部特徵檔,
            加恬聲韻類檔, 新拄好短恬聲韻檔, 加短恬的重估模型, 估幾擺=cls.上尾重估擺
        )

        return 加恬聲韻類檔, 拄好短恬的重估模型, 新拄好短恬聲韻檔, 新拄好短恬音節檔

    @classmethod
    def _三連音重估縛做伙加混合佮加無看過的音(cls, 執行檔路徑, 資料目錄,
                            全部特徵檔, 音節聲韻對照檔,
                            新拄好短恬聲韻檔, 加恬聲韻類檔,
                            拄好短恬的重估模型,
                            ):
        #         if 三連音:
        三連音目錄 = cls._細項目錄(資料目錄, '三連音目錄')
        三連音聲韻類檔 = os.path.join(三連音目錄, '三連音聲韻類檔.list')
        三連音聲韻檔 = os.path.join(三連音目錄, '三連音聲韻檔.mlf')
        cls._音標換三連音(執行檔路徑, 三連音目錄, 新拄好短恬聲韻檔, 三連音聲韻類檔, 三連音聲韻檔)
        三連音模型檔 = os.path.join(三連音目錄, '三連音模型檔.macro')
        cls._模型換三連音(執行檔路徑, 三連音目錄, 拄好短恬的重估模型, 加恬聲韻類檔, 三連音模型檔, 三連音聲韻類檔)
        三連音重估模型 = cls._模型重估(
            執行檔路徑, 三連音目錄, 全部特徵檔,
            三連音聲韻類檔, 三連音聲韻檔, 三連音模型檔, 估幾擺=cls.調整參數重估擺
        )
        三連音統計檔 = 三連音重估模型[:-len('.macro')] + '.sts'
        三連音縛做伙模型 = os.path.join(三連音目錄, '三連音縛做伙模型.macro')
        三連音縛做伙聲韻類檔 = os.path.join(三連音目錄, '三連音縛做伙聲韻類檔.tied')
        三連音縛做伙樹檔 = os.path.join(三連音目錄, '三連音縛做伙樹檔.tree')
        cls._模型相倚三連音縛做伙(執行檔路徑, 三連音目錄,
                        三連音模型檔, 三連音聲韻類檔, 三連音統計檔, 加恬聲韻類檔,
                        三連音縛做伙模型, 三連音縛做伙聲韻類檔, 三連音縛做伙樹檔)

        三連音加混合模型 = cls._加混合數(
            執行檔路徑, 三連音目錄, 全部特徵檔,
            三連音縛做伙聲韻類檔, 三連音聲韻檔, 三連音縛做伙模型,
            cls.三連音混合數, 估幾擺=cls.混合數重估擺, 上尾估幾擺=cls.混合數上尾重估擺
        )
        三連音全部縛做伙模型 = os.path.join(三連音目錄, '三連音全部縛做伙模型.macro')
        三連音全部縛做伙聲韻類檔 = os.path.join(三連音目錄, '三連音全部縛做伙聲韻類檔.tied')
        cls._模型加全部三連音(執行檔路徑, 三連音目錄,
                      音節聲韻對照檔, 三連音縛做伙樹檔,
                      三連音加混合模型, 三連音聲韻類檔, 三連音縛做伙聲韻類檔,
                      三連音全部縛做伙模型, 三連音全部縛做伙聲韻類檔)
        return 三連音全部縛做伙聲韻類檔, 三連音全部縛做伙模型

    @classmethod
    def _標仔換目錄(cls, 原本全部標仔檔, 新標仔目錄):
        全部標仔 = []
        for 標仔檔名 in cls._讀檔案(原本全部標仔檔):
            標仔所在 = os.path.join(新標仔目錄, os.path.basename(標仔檔名))
            if os.path.isfile(標仔所在):
                全部標仔.append(標仔所在)
        return 全部標仔

    @classmethod
    def _建立初步模型(cls, 執行檔路徑, 資料目錄, 全部特徵檔, 聲韻類檔, 聲韻檔):
        公家模型建立參數檔 = os.path.join(資料目錄, '公家模型建立參數檔.cfg')
        cls._字串寫入檔案(公家模型建立參數檔,
                    cls.特徵參數.format('ANON', 'HTK'))
        公家模型檔 = os.path.join(資料目錄, '公家模型檔')
        模型版檔 = os.path.join(資料目錄, '模型版檔')
        cls._字串寫入檔案(模型版檔, cls.模型版參數)
        公家模型指令 = [join(執行檔路徑, 'HCompV'),
                  '-A', '-C', 公家模型建立參數檔, '-m', '-f', '0.0001',
                  '-o', 公家模型檔, '-M', 資料目錄, '-I', 聲韻檔, '-S', 全部特徵檔, 模型版檔
                  ]
        cls._走指令(公家模型指令)
        公家模型 = cls._讀檔案(公家模型檔)
        公家變異數檔 = os.path.join(資料目錄, 'vFloors')
        公家變異數 = cls._讀檔案(公家變異數檔)
        初步模型資料 = [公家模型[:3], 公家變異數]
        公家狀態 = 公家模型[4:]
        聲韻名 = '~h "{0}"'
        for 聲韻 in cls._讀檔案(聲韻類檔):
            初步模型資料.append([聲韻名.format(聲韻)])
            初步模型資料.append(公家狀態)
        初步模型檔 = os.path.join(資料目錄, '初步模型檔.macro')
        cls._陣列寫入檔案(初步模型檔,
                    itertools.chain.from_iterable(初步模型資料))
        return 初步模型檔

    @classmethod
    def _模型重估(cls, 執行檔路徑, 資料目錄, 全部特徵檔, 聲韻類檔, 聲韻檔, 原來模型檔, 估幾擺):
        原來模型檔檔名 = os.path.basename(原來模型檔)
        這馬模型檔 = 原來模型檔
        基本路徑 = 原來模型檔.rsplit('.', 1)[0]
        資料夾 = 基本路徑 + '-重估'
        for 第幾擺 in range(估幾擺):
            這擺資料夾 = os.path.join(資料夾, '{0:02}'.format(第幾擺))
            os.makedirs(這擺資料夾, exist_ok=True)
            新統計檔 = os.path.join(這擺資料夾, '統計.sts')
            錯誤資訊 = []
            for 切掉路徑門檻參數 in [
                ('-t', '450.0', '150.0', '10000.0'),
                ('-t', '30.0'),
                ('-t', '2.0'),
            ]:
                重估指令 = [
                    join(執行檔路徑, 'HERest'),
                    '-A', '-T', '407',
                ] + list(切掉路徑門檻參數) + [
                    '-M', 這擺資料夾, '-H', 這馬模型檔, '-s', 新統計檔,
                    '-I', 聲韻檔, '-S', 全部特徵檔, 聲韻類檔
                ]
                try:
                    cls._走指令(重估指令)
                except Exception as 錯誤:
                    錯誤資訊.append(錯誤)
                else:
                    錯誤資訊 = None
                    break
            if 錯誤資訊 is not None:
                raise RuntimeError(錯誤資訊)
            這馬模型檔 = os.path.join(這擺資料夾, 原來模型檔檔名)
        上尾模型檔 = '{0}-重估.macro'.format(基本路徑)
        上尾統計檔 = '{0}-重估.sts'.format(基本路徑)
        shutil.copy(這馬模型檔, 上尾模型檔)
        shutil.copy(新統計檔, 上尾統計檔)
        return 上尾模型檔

    @classmethod
    def _音類標仔檔加短恬(cls, 原來音類檔, 加恬音類檔):
        音類 = set(cls._讀檔案(原來音類檔))
        音類.add(HTK語料處理.短恬)
        cls._陣列寫入檔案(加恬音類檔, 音類)

    @classmethod
    def _音節標仔檔加短恬(cls, 原來音節檔, 加恬音節檔):
        加短恬音節 = cls._音節標仔加短恬(cls._讀檔案(原來音節檔))
        cls._陣列寫入檔案(加恬音節檔, 加短恬音節)

    @classmethod
    def _音節標仔加短恬(cls, 原來標仔):
        頂一逝, *後壁資料 = 原來標仔
        if not cls._是有音標仔(頂一逝):
            加短恬音節 = [頂一逝]
        else:
            加短恬音節 = [HTK語料處理.短恬, 頂一逝]
        for 後一逝 in 後壁資料:
            頭前是音標 = cls._是有音標仔(頂一逝)
            後壁是音標 = cls._是有音標仔(後一逝)
            if 頭前是音標 and 後壁是音標:
                加短恬音節.append(HTK語料處理.短恬)
            elif cls.是MLF檔逐音檔開始符號(頂一逝) and 後壁是音標:
                加短恬音節.append(HTK語料處理.短恬)
            elif 頭前是音標 and 後一逝 == cls.MLF檔逐音檔結束符號:
                加短恬音節.append(HTK語料處理.短恬)
            加短恬音節.append(後一逝)
            頂一逝 = 後一逝
        if cls._是有音標仔(加短恬音節[-1]):
            加短恬音節.append(HTK語料處理.短恬)
        return 加短恬音節

    @classmethod
    def _是有音標仔(cls, 標仔):
        if 標仔 in (cls.MLF檔開始符號, cls.MLF檔逐音檔結束符號) or\
                cls.是MLF檔逐音檔開始符號(標仔) or cls._是恬(標仔):
            return False
        return True

    @classmethod
    def 是MLF檔逐音檔開始符號(cls, 標仔):
        return 標仔.startswith('"')

    @classmethod
    def _提掉傷短的短恬(cls, 對齊加恬聲韻檔, 新拄好短恬聲韻檔):
        新聲韻 = []
        for 一逝 in cls._讀檔案(對齊加恬聲韻檔):
            try:
                開始, 結束, 標仔 = 一逝.split()
                # 無到三个音框就提掉
                if int(結束) - int(開始) >= 300000 or 標仔 != HTK語料處理.短恬:
                    新聲韻.append(標仔)
            except ValueError:
                新聲韻.append(一逝)
        cls._陣列寫入檔案(新拄好短恬聲韻檔, 新聲韻)

    @classmethod
    def _模型提掉短恬(cls, 執行檔路徑, 資料目錄,
                原本模型, 原來有短恬的聲韻類檔, 提掉短恬的模型):
        提掉短恬的空設定 = os.path.join(資料目錄, '提掉短恬的空設定.hed')
        cls._字串寫入檔案(提掉短恬的空設定, '')
        提掉短恬的聲韻類檔 = os.path.join(資料目錄, '提掉短恬的聲韻類檔.list')
        原來聲韻類 = set(cls._讀檔案(原來有短恬的聲韻類檔))
        原來聲韻類.discard(HTK語料處理.短恬)
        cls._陣列寫入檔案(提掉短恬的聲韻類檔, 原來聲韻類)
        指令 = cls._改模型指令(執行檔路徑,
                        原本模型, 提掉短恬的模型, 提掉短恬的空設定, 提掉短恬的聲韻類檔)
        cls._走指令(指令)

    @classmethod
    def _模型加短恬(cls, 原本模型, 加短恬模型):
        恬中央狀態 = '~h \"{0}.*?\".*?<STATE> 3[ \n]*(.*?)[ \n]*<STATE> 4'\
                .format(語音標仔轉換.恬音)
        原本資料 = cls._讀檔案(原本模型)
        揣著的高斯狀態 = re.search(恬中央狀態,
                            '\n'.join(原本資料), re.DOTALL)
        短恬高斯狀態 = cls.短恬參數.format(HTK語料處理.短恬, 揣著的高斯狀態.group(1))
        原本資料.append(短恬高斯狀態)
        cls._陣列寫入檔案(加短恬模型, 原本資料)

    @classmethod
    def _恬音佮短恬愛縛做伙(cls, 執行檔路徑, 資料目錄,
                   加短恬模型, 加短恬縛好模型, 聲韻類檔):
        _恬音佮短恬愛縛做伙 = os.path.join(資料目錄, '_恬音佮短恬愛縛做伙.hed')
        指令 = '''\
AT 2 4 0.2 {{{0}.transP}}
AT 4 2 0.2 {{{0}.transP}}
TI 短恬縛恬音 {{{0}.state[3],{1}.state[2]}}\
'''	.format(語音標仔轉換.恬音, HTK語料處理.短恬)
        cls._字串寫入檔案(_恬音佮短恬愛縛做伙, 指令)
        縛做伙指令 = cls._改模型指令(
            執行檔路徑, 加短恬模型, 加短恬縛好模型, _恬音佮短恬愛縛做伙, 聲韻類檔)
        cls._走指令(縛做伙指令)

    @classmethod
    def _音標換三連音(cls, 執行檔路徑, 資料目錄,
                孤音聲韻檔, 三連音聲韻類檔, 三連音聲韻檔):
        莫跳脫聲韻 = os.path.join(資料目錄, '莫跳脫聲韻.cfg')
        cls._字串寫入檔案(莫跳脫聲韻, 'noNumEscapes = TRUE')
        換三連音 = os.path.join(資料目錄, '換三連音.led')
        cls._字串寫入檔案(換三連音, 'TC')
        短恬相關三連音聲韻檔 = os.path.join(資料目錄, '短恬相關三連音聲韻.mlf')
        短恬相關三連音聲韻類檔 = os.path.join(資料目錄, '短恬相關三連音聲韻類.list')
        換三連音指令 = [join(執行檔路徑, 'HLEd'), '-A',
                  '-C', 莫跳脫聲韻, '-l', '*', '-n', 短恬相關三連音聲韻類檔,
                  '-i', 短恬相關三連音聲韻檔,
                  換三連音, 孤音聲韻檔
                  ]
        cls._走指令(換三連音指令)

        聲韻類 = set(cls._讀檔案(短恬相關三連音聲韻類檔))
        無恬相關聲韻類 = set(cls._提掉恬的相關(聲韻類))
        無恬相關聲韻類.add(HTK語料處理.短恬)
        cls._陣列寫入檔案(三連音聲韻類檔, 無恬相關聲韻類)

        cls._陣列寫入檔案(三連音聲韻檔,
                    cls._提掉恬的相關(cls._讀檔案(短恬相關三連音聲韻檔))
                    )

    @classmethod
    def _提掉恬的相關(cls, 聲韻資料):
        無恬相關聲韻 = []
        for 聲韻 in 聲韻資料:
            主要音值 = 語音標仔轉換.提出標仔主要音值(聲韻)
            if cls._是恬(主要音值):
                無恬相關聲韻.append(主要音值)
            else:
                無恬相關聲韻.append(聲韻)
        return 無恬相關聲韻

    @classmethod
    def _是恬(cls, 音):
        if 音 in [語音標仔轉換.恬音, HTK語料處理.短恬]:
            return True
        else:
            return False

    @classmethod
    def _模型換三連音(cls, 執行檔路徑, 資料目錄,
                孤音模型, 孤音聲韻類檔, 三連音模型, 三連音聲韻類檔):
        換三連音 = os.path.join(資料目錄, '換三連音.hed')
        指令 = ['CL {0}'.format(三連音聲韻類檔)]
        for 聲韻 in cls._讀檔案(孤音聲韻類檔):
            if not cls._是恬(聲韻):
                指令.append(
                    'TI T_{0} {{({0},{0}+*,*-{0},*-{0}+*).transP}}'.format(聲韻))
        cls._陣列寫入檔案(換三連音, 指令)
        換三連音指令 = cls._改模型指令(
            執行檔路徑, 孤音模型, 三連音模型, 換三連音, 孤音聲韻類檔)
        cls._走指令(換三連音指令)

    @classmethod
    def _模型相倚三連音縛做伙(cls, 執行檔路徑, 資料目錄,
                    三連音模型檔, 三連音聲韻類檔, 三連音統計檔, 孤音聲韻類檔,
                    三連音縛做伙模型, 三連音縛做伙聲韻類檔, 三連音縛做伙樹檔):
        設定 = """\
RO 100.0 {0}
TR 0
{{0}}

TR 2
{{1}}

TR 1
AU "{1}"
CO "{2}"
ST "{3}"
SH
""".format(三連音統計檔, 三連音聲韻類檔, 三連音縛做伙聲韻類檔, 三連音縛做伙樹檔)
        問題設定 = []
        縛做伙設定 = []
        for 聲韻 in cls._讀檔案(孤音聲韻類檔):
            '有恬音做樹就好，因為因兩个縛做伙'
            問題設定.append(
                'QS "頭前是{0}" {{{0}-*}}'.format(聲韻))
            問題設定.append(
                'QS "後壁是{0}" {{*+{0}}}'.format(聲韻))
            if cls._是恬(聲韻):
                continue
            for 第幾个狀態 in range(2, 5):
                縛做伙設定.append(
                    'TB {2} "縛{0}的{1}" {{({0},{0}+*,*-{0},*-{0}+*).state[{1}]}}'
                    .format(聲韻, 第幾个狀態, 350.0))
        三連音縛做伙設定 = os.path.join(資料目錄, '三連音縛做伙設定.hed')
        cls._字串寫入檔案(三連音縛做伙設定,
                    設定.format('\n'.join(問題設定), '\n'.join(縛做伙設定)))
        三連音縛做伙指令 = cls._改模型指令(執行檔路徑,
                              三連音模型檔, 三連音縛做伙模型, 三連音縛做伙設定, 三連音聲韻類檔)
        cls._走指令(三連音縛做伙指令)

    @classmethod
    def _模型加全部三連音(cls, 執行檔路徑, 資料目錄,
                  音節聲韻對照檔, 三連音縛做伙樹檔,
                  原來模型, 原來聲韻類檔, 原來縛做伙檔,
                  全部模型檔, 全部縛做伙檔):
        '其實會當佮「三連音縛做伙」當齊做，毋過分開較知影佇創啥，親像HTS仝款加無看過的模型'
        全部三連音 = set(cls._讀檔案(原來聲韻類檔))
        全部聲韻 = set()
        for 聲韻 in 全部三連音:
            全部聲韻.add(
                語音標仔轉換.提出標仔主要音值(聲韻))
        聲韻排法 = []
        for 音節聲韻 in cls._讀檔案(音節聲韻對照檔):
            拆聲韻 = 音節聲韻.split()[1:]
            for 聲韻 in 拆聲韻:
                if 聲韻 not in 全部聲韻:
                    break
            else:
                聲韻排法.append(拆聲韻)
        家己一音 = set()
        頭一音, 頭兩音 = set(), set()
        尾一音, 尾兩音 = set(), set()
        for 聲韻組 in 聲韻排法:
            頭一音.add(tuple(聲韻組[:1]))
            尾一音.add(tuple(聲韻組[-1:]))
            if len(聲韻組) == 1:
                '予因莫食著邊仔的音'
                if not cls._是恬(聲韻組[0]):
                    家己一音.add(tuple(聲韻組))
            else:
                頭兩音.add(tuple(聲韻組[:2]))
                尾兩音.add(tuple(聲韻組[-2:]))
        for 頭前, 中央, 後壁 in [(尾兩音, [()], 頭一音),
                           (尾一音, [()], 頭兩音),
                           (尾一音, 家己一音, 頭一音)]:
            for 頭 in 頭前:
                for 中 in 中央:
                    for 後 in 後壁:
                        全部三連音.add(
                            '{0}-{1}+{2}'.format(*(頭 + 中 + 後)))
        全部三連音檔 = os.path.join(資料目錄, '全部三連音.list')
        cls._陣列寫入檔案(全部三連音檔, 全部三連音)
        設定 = """\
LT "{0}"
AU "{1}"
CO "{2}"
SH
""".format(三連音縛做伙樹檔, 全部三連音檔, 全部縛做伙檔)
        全部三連音設定檔 = os.path.join(資料目錄, '全部三連音設定.hed')
        cls._字串寫入檔案(全部三連音設定檔, 設定)
        這馬模型有的聲韻表檔 = os.path.join(資料目錄, '這馬模型有的聲韻表.list')
        這馬模型有的聲韻表 = []
        for 聲韻 in cls._讀檔案(原來縛做伙檔):
            if ' ' not in 聲韻:
                這馬模型有的聲韻表.append(聲韻)
        cls._陣列寫入檔案(這馬模型有的聲韻表檔, 這馬模型有的聲韻表)
        縛做伙指令 = cls._改模型指令(
            執行檔路徑, 原來模型, 全部模型檔, 全部三連音設定檔, 這馬模型有的聲韻表檔)
        cls._走指令(縛做伙指令)

    @classmethod
    def _加混合數(cls, 執行檔路徑, 資料目錄,
              全部特徵檔, 聲韻類檔, 聲韻檔,
              原來模型, 混合數, 估幾擺, 上尾估幾擺):
        頂一个模型 = 原來模型
        for 擺, 混合 in enumerate(混合數):
            這擺資料夾 = os.path.join(資料目錄, '加混合數', '{0:02}'.format(擺))
            os.makedirs(這擺資料夾, exist_ok=True)
            設定檔 = os.path.join(這擺資料夾, '設定檔.hed')
            加混合模型 = os.path.join(這擺資料夾, '加混合模型.macro')
            cls._陣列寫入檔案(設定檔, [
                "MU {0} {{*.state[2-4].mix}}".format(混合),
                "MU {0} {{{1}.state[2-4].mix}}".format(混合 * 2, 語音標仔轉換.恬音)])
            _加混合數指令 = cls._改模型指令(
                執行檔路徑, 頂一个模型, 加混合模型, 設定檔, 聲韻類檔)
            cls._走指令(_加混合數指令)
            頂一个模型 = cls._模型重估(執行檔路徑, 資料目錄, 全部特徵檔,
                              聲韻類檔, 聲韻檔, 加混合模型, 估幾擺=估幾擺)
        加混合了模型 = os.path.join(資料目錄, '加混合了模型.macro')
        shutil.copy(頂一个模型, 加混合了模型)
        上尾模型檔 = cls._模型重估(執行檔路徑, 資料目錄, 全部特徵檔,
                          聲韻類檔, 聲韻檔, 加混合了模型, 估幾擺=上尾估幾擺)
        return 上尾模型檔
    模型版參數 = \
        '''
~o <VecSize> 39 <MFCC_E_D_A_Z> <DiagC> <StreamInfo> 1 39
<BeginHMM>
<NUMSTATES> 5
<STATE> 2
<NUMMIXES> 1
<SWeights> 1 1
<STREAM> 1
<MIXTURE> 1 1.000000e+000
<MEAN> 39
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 \
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
<VARIANCE> 39
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 \
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0

<STATE> 3
<NUMMIXES> 1
<SWeights> 1 1
<STREAM> 1
<MIXTURE> 1 1.000000e+000
<MEAN> 39
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 \
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
<VARIANCE> 39
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 \
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0

<STATE> 4
<NUMMIXES> 1
<SWeights> 1 1
<STREAM> 1
<MIXTURE> 1 1.000000e+000
<MEAN> 39
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 \
0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0
<VARIANCE> 39
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 \
1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0

<TRANSP> 5
0.000000e+000 1.000000e+000 0.000000e+000 0.000000e+000 0.000000e+000
0.000000e+000 6.000000e-001 4.000000e-001 0.000000e+000 0.000000e+000
0.000000e+000 0.000000e+000 6.000000e-001 4.000000e-001 0.000000e+000
0.000000e+000 0.000000e+000 0.000000e+000 6.000000e-001 4.000000e-001
0.000000e+000 0.000000e+000 0.000000e+000 0.000000e+000 0.000000e+000
<ENDHMM>
'''
    短恬參數 = \
        '''
~h "{0}"
<BEGINHMM>
<NUMSTATES> 3
<STATE> 2
{1}
<TRANSP> 3
0.000000e+00 1.000000e+00 0.000000e+00
0.000000e+00 5.000000e-01 5.000000e-01
0.000000e+00 0.000000e+00 0.000000e+00
<ENDHMM>
'''

    @classmethod
    def _改模型指令(cls, 執行檔路徑, 頂一个模型, 下一个模型, 設定檔, 聲韻類檔):
        return [
            join(執行檔路徑, 'HHEd'), '-A',
            '-H', 頂一个模型, '-w', 下一个模型, 設定檔, 聲韻類檔
        ]
