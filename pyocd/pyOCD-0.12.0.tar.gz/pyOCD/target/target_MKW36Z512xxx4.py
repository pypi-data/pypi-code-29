"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2017-2018 ARM Limited

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
"""

from .family.target_kinetis import Kinetis
from .family.flash_kinetis import Flash_Kinetis
from ..core.memory_map import (FlashRegion, RamRegion, AliasRegion, MemoryMap)
from ..debug.svd import SVDFile
import logging

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0x4937b510, 0x60082000, 0x78414836, 0x0f890649, 0xd0152902, 0x4a342100, 0x444a2900, 0xd0077011,
    0x229f7841, 0x70414011, 0x06497841, 0xd1fb0f89, 0x4448482e, 0xf85ef000, 0xd0002800, 0xbd102001,
    0xe7e82101, 0x44484828, 0x28007800, 0x4825d00a, 0x229f7841, 0x31404011, 0x78417041, 0x0f890649,
    0xd1fa2902, 0x47702000, 0xb5104820, 0x44484920, 0xf89df000, 0xd1042800, 0x2100481c, 0xf0004448,
    0xbd10fb06, 0x4c19b570, 0x444c4605, 0x4b184601, 0x68e24620, 0xf8c7f000, 0xd1052800, 0x46292300,
    0x68e24620, 0xfb00f000, 0xb570bd70, 0x460b460c, 0x46014606, 0xb084480d, 0x44484615, 0xf92af000,
    0xd10a2800, 0x90029001, 0x48082101, 0x462b9100, 0x46314622, 0xf0004448, 0xb004fb2e, 0x0000bd70,
    0x40048100, 0x4007e000, 0x00000004, 0x00000008, 0x6b65666b, 0xd00b2800, 0x68c949fe, 0x0f090109,
    0xd007290f, 0x00494afc, 0x5a51447a, 0xe0030289, 0x47702004, 0x04c92101, 0x2300b410, 0x60416003,
    0x72012102, 0x60c10289, 0x7a0c49f4, 0x40a2158a, 0x7ac96142, 0x61816103, 0x06892105, 0x21016201,
    0x62410349, 0x2000bc10, 0x28004770, 0x6101d002, 0x47702000, 0x47702004, 0x680148e9, 0x02922201,
    0x60014311, 0x8f6ff3bf, 0x8f4ff3bf, 0x48e44770, 0x22016801, 0x43110292, 0xf3bf6001, 0xf3bf8f6f,
    0x47708f4f, 0x217048df, 0x21807001, 0x78017001, 0xd5fc0609, 0x06817800, 0x2067d501, 0x06c14770,
    0x2068d501, 0x07c04770, 0x2069d0fc, 0x28004770, 0x2004d101, 0xb5104770, 0x4ad24604, 0x605048d2,
    0x428148d2, 0x206bd001, 0x2000e000, 0xd1072800, 0xf7ff4620, 0x4603ffd7, 0xf7ff4620, 0x4618ffc8,
    0x2800bd10, 0x2004d101, 0xb5104770, 0x22004614, 0x60626022, 0x60e260a2, 0x61626122, 0x61e261a2,
    0x1a896802, 0x68c16021, 0x7a016061, 0xf0006840, 0x60a0fd7b, 0x60e02008, 0x61606120, 0x200461a0,
    0x200061e0, 0xb5ffbd10, 0x4615b089, 0x466a460c, 0xf7ff9809, 0x462affd6, 0x9b044621, 0xf0009809,
    0x0007fd3b, 0x9c00d130, 0x19659e01, 0x46311e6d, 0xf0004628, 0x2900fd59, 0x1c40d002, 0x1e454370,
    0xd81d42ac, 0x20090221, 0x06000a09, 0x48a51809, 0x49a66041, 0x4288980c, 0x206bd001, 0x2000e000,
    0xd1112800, 0xf7ff9809, 0x4607ff7d, 0x69009809, 0xd0002800, 0x2f004780, 0x19a4d102, 0xd9e142ac,
    0xf7ff9809, 0x4638ff64, 0xbdf0b00d, 0xd1012800, 0x47702004, 0x4604b510, 0x48954a92, 0x48936050,
    0xd0014281, 0xe000206b, 0x28002000, 0x4620d107, 0xff58f7ff, 0x46204603, 0xff49f7ff, 0xbd104618,
    0xd1012800, 0x47702004, 0x4604b510, 0x48894a85, 0x48866050, 0xd0014281, 0xe000206b, 0x28002000,
    0x4620d107, 0xff3ef7ff, 0x46204603, 0xff2ff7ff, 0xbd104618, 0xd1012a00, 0x47702004, 0xb089b5ff,
    0x461e4614, 0x466a460d, 0xf7ff9809, 0x4632ff5a, 0x9b034629, 0xf0009809, 0x0007fcbf, 0x9d00d12d,
    0xd0262e00, 0x486fcc02, 0x99036081, 0xd0022904, 0xd0072908, 0x022ae00e, 0x0a122103, 0x18510649,
    0xe0076041, 0x60c1cc02, 0x2107022a, 0x06090a12, 0x60411851, 0xf7ff9809, 0x4607ff05, 0x69009809,
    0xd0002800, 0x2f004780, 0x9803d103, 0x1a361945, 0x9809d1d8, 0xfeebf7ff, 0xb00d4638, 0x2800bdf0,
    0x2a00d001, 0x2004d101, 0xb5104770, 0x06084604, 0x48590a01, 0x49531808, 0x68106048, 0x68506088,
    0x462060c8, 0xfedef7ff, 0x46204603, 0xfecff7ff, 0xbd104618, 0xb08bb5ff, 0x460c980d, 0xd0242800,
    0x980b466a, 0xfefdf7ff, 0x9b054621, 0x980b9a0e, 0xfc62f000, 0x28009008, 0x9801d118, 0x980e9009,
    0x28009e00, 0x9809d05d, 0x900a4240, 0x4270990a, 0x42404008, 0x42b02500, 0x9909d101, 0x990e1840,
    0x42811989, 0x1b84d904, 0x2004e003, 0xbdf0b00f, 0x2c009c0e, 0x2701d03b, 0x42bc02bf, 0x4627d800,
    0x980d08a9, 0x18090089, 0x463a2005, 0xf0000680, 0x1970fc71, 0x200b0201, 0x06000a09, 0x48291809,
    0x46386041, 0xf0009905, 0x0401fc4f, 0x1809482b, 0x60814824, 0xf7ff980b, 0x9008fe85, 0x6900980b,
    0xd0002800, 0x98084780, 0xd00c2800, 0x6801481c, 0x02922201, 0x60014311, 0x8f6ff3bf, 0x8f4ff3bf,
    0xb00f9808, 0x1be4bdf0, 0x2c0019ed, 0x08a9d1c3, 0x0089980d, 0x900d1808, 0x1976980e, 0x900e1b40,
    0x980bd1a4, 0xfe53f7ff, 0xb5ffe7ea, 0x9809b089, 0x461d9f12, 0x460e4614, 0xd0242800, 0xd0222c00,
    0xf7ff466a, 0x9806fe7e, 0x1e40463a, 0xd1184206, 0xe0154205, 0x40048040, 0x00000c54, 0x40020020,
    0xf000300c, 0x40020000, 0x44ffffff, 0x6b65666b, 0x49ffffff, 0x4bffffff, 0x4300ffff, 0x0000ffff,
    0x2065d004, 0x2004e021, 0xbdf0b00d, 0x20001971, 0x2a011e49, 0x2f00d002, 0xe003d006, 0xd1012e08,
    0xd0122d08, 0xe0102004, 0x02922201, 0xd30c4291, 0x42960212, 0x4afed302, 0xd9064291, 0x05db2301,
    0xd3ef429e, 0x42914afb, 0x2800d8ec, 0x2d00d1dc, 0x49f9d0da, 0x18470638, 0x20030231, 0x06000a09,
    0x48f61809, 0x98066041, 0xd0022804, 0xd0032808, 0x48f2e004, 0xe00160c7, 0x608748f0, 0xf7ff9809,
    0x2800fdf1, 0x49edd1c0, 0xc404688a, 0x2a089a06, 0x68c9d101, 0x9906c402, 0x1a6d198e, 0xb00dd1dc,
    0x2800bdf0, 0x2a00d001, 0x2004d101, 0xb5704770, 0x06094614, 0x0a094ae2, 0x18894de0, 0xf7ff6069,
    0x2800fdd1, 0x68a9d103, 0x68e96021, 0xbd706061, 0xd00e2800, 0xd00c2900, 0x788048d8, 0x0f920782,
    0xd0082a02, 0x28020980, 0x2002d008, 0x20007008, 0x20044770, 0x20004770, 0xe7f87008, 0xe7f52001,
    0xd0012800, 0xd1012900, 0x47702004, 0x4dcbb570, 0x78aa2300, 0x0f920792, 0xd0262a02, 0x606a4ac9,
    0x78cb780c, 0x784c4622, 0x0224061b, 0x788c4322, 0x43220424, 0xba12431a, 0x78cb0a12, 0x431a0212,
    0x790c60aa, 0x462279cb, 0x061b794c, 0x43220224, 0x79c9798c, 0x43220424, 0xba12431a, 0x02120a12,
    0x60ea430a, 0xfd7ef7ff, 0x46184603, 0x2800bd70, 0x2004d101, 0x4ab44770, 0x18890409, 0x4aafb510,
    0xf7ff6051, 0xbd10fd6f, 0xb08bb5ff, 0x461e4614, 0x466a460d, 0xf7ff980b, 0x4622fd94, 0x9b054629,
    0xf000980b, 0x2800faf9, 0x466ad133, 0x980b4629, 0xfd87f7ff, 0x98029d00, 0x42699008, 0x40014240,
    0x42af424f, 0x9808d101, 0x2c00183f, 0x0230d020, 0x1b7e9009, 0xd90042a6, 0x46304626, 0xf0009905,
    0x022afb03, 0x0a122101, 0x18520609, 0x604a4993, 0x04009a09, 0x30ff4310, 0x980b6088, 0xfd32f7ff,
    0xd1062800, 0x1ba49808, 0x183f19ad, 0xd1e02c00, 0xb00f2000, 0x2b00bdf0, 0x2004d101, 0xb5ff4770,
    0x4616b089, 0x460c461d, 0x9f12466a, 0xf7ff9809, 0x4632fd48, 0x9b074621, 0xf0009809, 0x2800faad,
    0x9c00d11d, 0xd01a2e00, 0x0638497b, 0x02211847, 0x0a092001, 0x18090640, 0x60414878, 0x68296087,
    0x980960c1, 0xfcfef7ff, 0xd00a2800, 0x29009913, 0x600cd000, 0x29009914, 0x2200d001, 0xb00d600a,
    0x9907bdf0, 0x08891a76, 0x194d0089, 0x190c9907, 0xd1dc2e00, 0xbdf0b00d, 0xd1012800, 0x47702004,
    0x04094a6a, 0xb5101889, 0x60514a64, 0xfcdaf7ff, 0x2b00bd10, 0x2004d101, 0xb5f04770, 0xb0ad461d,
    0x460c4616, 0x23084607, 0xfa66f000, 0xd1782800, 0xd00c2f00, 0x90019000, 0x683a9002, 0x92006879,
    0x92022220, 0x42910292, 0x0949d903, 0x2004e003, 0x2101e002, 0x91010289, 0x28004684, 0x19a0d161,
    0x9b012100, 0x434b9e00, 0x008e18f3, 0x5193aa03, 0x1c499b02, 0xd2f4428b, 0x4f482200, 0x2b00ae24,
    0xe027d802, 0xd2042a08, 0x40d17c39, 0x0fc907c9, 0x4611e01b, 0x29083908, 0x7c7bd205, 0x07d940cb,
    0x54b10fc9, 0x4611e012, 0x29083910, 0x7cbbd205, 0x07d940cb, 0x54b10fc9, 0x4611e008, 0x29083918,
    0x7cfbd208, 0x07d940cb, 0x54b10fc9, 0x1c529902, 0xd8d74291, 0x460b2100, 0x4284460a, 0x008ed21b,
    0x59bfaf03, 0xd80c42a7, 0x19f6af03, 0x42a66876, 0xae24d907, 0x1c5b5c76, 0xd1002e00, 0x9e011c52,
    0x1c491934, 0xd3ea4284, 0xd0042a00, 0xd105429a, 0xe0042001, 0x2000e005, 0xe0017028, 0x70282002,
    0xb02d4660, 0x2b00bdf0, 0x2004d101, 0xb5f04770, 0xb085461f, 0x460c4616, 0x23084605, 0xf9dcf000,
    0xd1572800, 0xd0372d00, 0x90019000, 0x68289002, 0x69689000, 0x69a89001, 0x20009002, 0x28009003,
    0x9801d148, 0x424019a6, 0x42714602, 0x40224008, 0x25001880, 0x99014240, 0xf9e6f000, 0x42b49004,
    0x9800d232, 0x1a209901, 0xf9def000, 0xe00f2820, 0x000403ff, 0x008003ff, 0x00ffffff, 0x40020000,
    0x4100ffff, 0x45ffffff, 0x4000ffff, 0x4a00ffff, 0x49dfd204, 0xe00769c9, 0xe7cf2004, 0x42819902,
    0x49dbd90b, 0x38206989, 0x40822201, 0xd000438a, 0x98011c6d, 0x42b41904, 0x2d00d3d3, 0x9804d004,
    0xd2044285, 0xe0032002, 0x70382000, 0x2001e001, 0x98037038, 0xbdf0b005, 0xd00d2800, 0xd00b2a00,
    0xd222290a, 0x447b000b, 0x18db791b, 0x0806449f, 0x110f0d0a, 0x19171513, 0x47702004, 0xe01168c0,
    0xe00f6840, 0x08406840, 0x7a00e00c, 0x6800e00a, 0x2001e008, 0x6940e006, 0x6980e004, 0x6a00e002,
    0x6a40e000, 0x20006010, 0x206a4770, 0x46034770, 0x2b002000, 0x2905d005, 0xdc04d01b, 0xd80e2904,
    0x2004e017, 0x29084770, 0xdc04d013, 0xd0102906, 0xd1042907, 0x2909e00d, 0x2921d00b, 0x206ad001,
    0x2a004770, 0x2a01d003, 0x2077d001, 0x729a4770, 0x20764770, 0xb5704770, 0x0003461c, 0x2c00d005,
    0x0748d003, 0x2065d003, 0x2004bd70, 0x6858bd70, 0x42880840, 0x2001d904, 0x1a080280, 0xd801280f,
    0xbd702075, 0xd01f2a01, 0xd01d2a02, 0xd01b2a04, 0xd0192a08, 0xd0172a10, 0x28002004, 0x0208d1f1,
    0x0a002123, 0x4d920649, 0x60681840, 0x06104991, 0x60a81840, 0xf7ff4618, 0x7aa9fb65, 0x7a697021,
    0x7a297061, 0xbd7070a1, 0xe7e62000, 0x2000b5f7, 0x43c0b08c, 0xab019001, 0x990d2208, 0xf7ff980c,
    0x2800ffba, 0x990ed115, 0xd00b2901, 0x79094669, 0xd27d2906, 0x447a000a, 0x18927912, 0x1c154497,
    0x08857f36, 0x79004668, 0xd0042805, 0xd0052800, 0xb00f2074, 0x2000bdf0, 0xbdf0b00f, 0x2210ab01,
    0x980c990d, 0xff97f7ff, 0xab01e06f, 0x990d2201, 0xf7ff980c, 0xe068ff90, 0x23082100, 0x9c0d9100,
    0xaa02980c, 0xf7ff03d9, 0x2800fcc0, 0x4669d105, 0x00c98909, 0xd000428c, 0x28002075, 0xab01d1dc,
    0x990d2202, 0xf7ff980c, 0xe04eff76, 0x9000980c, 0x25086840, 0x980d0841, 0x180caa02, 0x900a485e,
    0x98004621, 0xfb2df7ff, 0x4621462a, 0x98009b06, 0xf892f000, 0xd1380007, 0x9e039c02, 0x46311de5,
    0xf0004628, 0x2900f8b1, 0x1c40d002, 0x1e454370, 0xd81f42ac, 0x20090221, 0x06000a09, 0x484c1809,
    0x494d6041, 0x4288980a, 0x206bd001, 0x2000e000, 0xd11a2800, 0xf7ff9800, 0x4607fad5, 0x69009800,
    0xd0002800, 0x2f004780, 0x19a4d104, 0xe00042ac, 0xd9dfe017, 0xf7ff9800, 0x4638faba, 0xab01e005,
    0x990d2204, 0xf7ff980c, 0x2800ff26, 0x4669d184, 0x29047909, 0xe75ed000, 0x2900990e, 0xb00fd1fb,
    0x2004bdf0, 0xbdf0b00f, 0xd0082800, 0x680a4830, 0x68096102, 0x42816900, 0x2069d003, 0x20044770,
    0x20004770, 0x28004770, 0x2900d006, 0x4828d004, 0x60086900, 0x47702000, 0x47702004, 0x68032201,
    0x03d24926, 0xd00c1c5b, 0x4393680b, 0x6842600b, 0x03802001, 0x680a2a00, 0x4382d00c, 0x2000600a,
    0x68404770, 0xd0032800, 0x43106808, 0xe7f66008, 0x47702078, 0xe7f14302, 0x60012100, 0x49186041,
    0x4a1868c9, 0xd502040b, 0x60426002, 0x0449e002, 0x6042d400, 0x47702000, 0xd1012800, 0x47702004,
    0x1e5bb410, 0xd1014219, 0xd002421a, 0x2065bc10, 0x68034770, 0xd807428b, 0x18896840, 0x42881818,
    0xbc10d302, 0x47702000, 0x2066bc10, 0x00004770, 0x40020000, 0x00ffffff, 0x6b65666b, 0xf000300c,
    0xf0003000, 0xffffffff, 0x460bb530, 0x20004601, 0x24012220, 0x460de009, 0x429d40d5, 0x461dd305,
    0x1b494095, 0x40954625, 0x46151940, 0x2d001e52, 0xbd30dcf1, 0x430b4603, 0xd003079b, 0xc908e009,
    0xc0081f12, 0xd2fa2a04, 0x780be003, 0x1c407003, 0x1e521c49, 0x4770d2f9, 0x40020004, 0x40020010,
    0x00100008, 0x00200018, 0x00400030, 0x00800060, 0x010000c0, 0x02000180, 0x04000300, 0x00000600,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000
    ],

    'pc_init' : 0x20000021,
    'pc_unInit': 0x20000065,
    'pc_program_page': 0x200000CB,
    'pc_erase_sector': 0x200000A5,
    'pc_eraseAll' : 0x20000089,

    'static_base' : 0x20000000 + 0x00000020 + 0x00000da0,
    'begin_stack' : 0x20000000 + 0x00001000,
    'begin_data' : 0x20000000 + 0x00001000,
    'page_size' : 0x00000200,
    'page_buffers' : [0x20001000, 0x20002000],   # Enable double buffering
    'min_program_length' : 8,
    'analyzer_supported' : True,
    'analyzer_address' : 0x1fffc000
};

class Flash_kw36z4(Flash_Kinetis):
    def __init__(self, target):
        super(Flash_kw36z4, self).__init__(target, flash_algo)

class KW36Z4(Kinetis):

    _dflash = \
        FlashRegion(name="Dflash",       start=0x10040000,  length=0x40000,      blocksize=0x800)
    memoryMap = MemoryMap(
        FlashRegion(name="Pflash",       start=0,           length=0x40000,      blocksize=0x800, isBootMemory=True),
        AliasRegion(name="Dflash alias", start=0x00040000,  length=0x40000,      blocksize=0x800, aliasOf=_dflash),
        _dflash,
        RamRegion(  name="FlexRAM",      start=0x14000000,  length=0x2000),
        RamRegion(  name="SRAM",         start=0x1fffc000,  length=0x10000)
        )

    def __init__(self, transport):
        super(KW36Z4, self).__init__(transport, self.memoryMap)
        self._svd_location = SVDFile(vendor="Freescale", filename="MKW36Z4.svd")

