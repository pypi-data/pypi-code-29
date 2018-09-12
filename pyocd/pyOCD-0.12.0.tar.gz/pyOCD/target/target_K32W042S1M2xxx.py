"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2006-2013 ARM Limited

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
from ..flash.flash import Flash
from ..core.target import Target
from ..core.coresight_target import CoreSightTarget
from ..core.memory_map import (FlashRegion, RamRegion, RomRegion, MemoryMap)
from ..debug.svd import SVDFile
from ..coresight import ap
from ..coresight.cortex_m import CortexM
from ..utility.timeout import Timeout
import logging
import os.path
from time import sleep

SMC0_MR = 0x40020040
SMC1_MR = 0x41020040
SMC_MR_BOOTCFG_MASK = 0x3

MDM_STATUS = 0x00000000
MDM_CTRL = 0x00000004
MDM_CORE_STATUS = 0x00000050
MDM_IDR = 0x000000fc

MDM_STATUS_FLASH_MASS_ERASE_ACKNOWLEDGE = (1 << 0)
MDM_STATUS_FLASH_READY = (1 << 1)
MDM_STATUS_SYSTEM_SECURITY = (1 << 2)
MDM_STATUS_MASS_ERASE_ENABLE = (1 << 5)
MDM_STATUS_CORE_HALTED = (1 << 16)

MDM_CTRL_FLASH_MASS_ERASE_IN_PROGRESS = (1 << 0)
MDM_CTRL_DEBUG_REQUEST = (1 << 2)
MDM_CTRL_SYSTEM_RESET_REQUEST = (1 << 3)
MDM_CTRL_CORE_HOLD_RESET = (1 << 4)

MDM_CORE_STATUS_CM4_HALTED = (1 << 7)
MDM_CORE_STATUS_CM0P_HALTED = (1 << 15)

HALT_TIMEOUT = 2.0

log = logging.getLogger("target.k32w042s")

flash_algo = {
    'load_address' : 0x20000000,
    'instructions' : [
    0xE00ABE00, 0x062D780D, 0x24084068, 0xD3000040, 0x1E644058, 0x1C49D1FA, 0x2A001E52, 0x4770D1F2,
    0x4838b510, 0x60414936, 0x60814937, 0x22806801, 0x22204391, 0x60014311, 0x69014834, 0x0f890589,
    0xd01c2902, 0x4a322100, 0x444a2900, 0xd0087011, 0x22036901, 0x43910212, 0x69016101, 0x0f890589,
    0x482cd1fb, 0x22016841, 0x43110792, 0x482a6041, 0xf0004448, 0x2800f855, 0x2001d000, 0x2101bd10,
    0x4823e7e1, 0x78004448, 0xd00d2800, 0x6901481f, 0x02122203, 0x31ff4391, 0x310231ff, 0x69016101,
    0x0f890589, 0xd1fa2902, 0x47702000, 0xb510481a, 0x4448491a, 0xf93af000, 0x4601bd10, 0xb5104816,
    0x22104b16, 0xf0004448, 0xbd10f8e4, 0x460cb570, 0x4606460b, 0x48104601, 0x4615b084, 0xf0004448,
    0x2800f963, 0x9001d10a, 0x21019002, 0x9100480a, 0x4622462b, 0x44484631, 0xfb0bf000, 0xbd70b004,
    0xd928c520, 0x4002a000, 0x0000ffff, 0x40020000, 0x00000004, 0x4002b000, 0x00000008, 0x6b65666b,
    0xd00a2800, 0x68c949fe, 0x290f0f09, 0x4afdd007, 0x447a0049, 0x02895a51, 0x2004e003, 0x21014770,
    0xb4300509, 0x60032300, 0x21026041, 0x02cc7201, 0x49f560c4, 0x158a7a45, 0xd00c2d01, 0x40aa7b0d,
    0x7b496142, 0x61816103, 0x06c92109, 0x62016244, 0x2000bc30, 0x7b8d4770, 0x614240aa, 0xe7f17bc9,
    0xd0022800, 0x20006101, 0x20044770, 0x48e74770, 0x49e76800, 0x42880a00, 0x48e6d101, 0x48e6e000,
    0x22016801, 0x60014311, 0x8f6ff3bf, 0x8f4ff3bf, 0xb5104770, 0xf0002101, 0xbd10fb82, 0x217048df,
    0x21807001, 0x78017001, 0xd5fc0609, 0x06817800, 0x2067d501, 0x06c14770, 0x2068d501, 0x07c04770,
    0x2069d0fc, 0x28004770, 0x2004d101, 0xb5704770, 0x4ad24604, 0x605048d2, 0x428148d2, 0x206bd001,
    0x2000e000, 0xd10c2800, 0x46202100, 0xfb57f000, 0xf7ff4620, 0x4605ffd3, 0x46202101, 0xfb4ff000,
    0xbd704628, 0xd0012800, 0xd1012a00, 0x47702004, 0x2000b410, 0x60906050, 0x611060d0, 0x61906150,
    0x621061d0, 0x23ff6250, 0x061b0248, 0x0a4018cc, 0x04892101, 0x60102308, 0xd209428c, 0x4320014c,
    0x01886010, 0x60d06111, 0x60911340, 0xe0066050, 0x05002001, 0x12006110, 0x01c06050, 0x20106090,
    0x61536190, 0x61d06213, 0x62502004, 0x2000bc10, 0xb5ff4770, 0x4615b08d, 0x460e461c, 0x980daa02,
    0xffc0f7ff, 0x9000a802, 0x4631462a, 0x980d9b08, 0xfb19f000, 0xd1082800, 0x428448a2, 0x266bd001,
    0x2600e000, 0xd0022e00, 0xb0114630, 0x9c02bdf0, 0x19659f03, 0x46391e6d, 0xf0004628, 0x2900fb37,
    0x1c40d002, 0x1e454378, 0x980d2100, 0xfae7f000, 0xd81442ac, 0x20090221, 0x06000a09, 0x488f1809,
    0x980d6041, 0xff5af7ff, 0x980d4606, 0x28006900, 0x4780d000, 0xd1022e00, 0x42ac19e4, 0x2101d9ea,
    0xf000980d, 0x4630facc, 0xbdf0b011, 0xd1012800, 0x47702004, 0x4604b570, 0x48834a80, 0x48816050,
    0xd0014281, 0xe000206b, 0x28002000, 0x2100d10c, 0xf0004620, 0x4620fab4, 0xff30f7ff, 0x21014605,
    0xf0004620, 0x4628faac, 0x2800bd70, 0x2004d101, 0xb5704770, 0x4a714604, 0x60504874, 0x42814871,
    0x206bd001, 0x2000e000, 0xd10c2800, 0x46202100, 0xfa95f000, 0xf7ff4620, 0x4605ff11, 0x46202101,
    0xfa8df000, 0xbd704628, 0xd1012a00, 0x47702004, 0xb08db5ff, 0x461e4614, 0xaa02460d, 0xf7ff980d,
    0xa802ff31, 0x46329000, 0x9b074629, 0xf000980d, 0x0007fa8a, 0x2100d132, 0x980d9d02, 0xfa6ff000,
    0xd0262e00, 0x4855cc02, 0x99076081, 0xd0022904, 0xd0072908, 0x022ae00e, 0x0a122103, 0x18510649,
    0xe0076041, 0x60c1cc02, 0x2107022a, 0x06090a12, 0x60411851, 0xf7ff980d, 0x4607fed1, 0x6900980d,
    0xd0002800, 0x2f004780, 0x9807d103, 0x1a361945, 0x2101d1d8, 0xf000980d, 0x4638fa42, 0xbdf0b011,
    0xd0012800, 0xd1012a00, 0x47702004, 0x4604b570, 0x0a010608, 0x1809483e, 0x60414838, 0x60816811,
    0x60c16851, 0x46202100, 0xfa29f000, 0xf7ff4620, 0x4605fea5, 0x46202101, 0xfa21f000, 0xbd704628,
    0xb08db5ff, 0x460c980f, 0xd02a2800, 0x980daa02, 0xfec8f7ff, 0x9000a802, 0x9b094621, 0x980d9a10,
    0xfa21f000, 0x28009000, 0x9803d11c, 0x9e029001, 0x980d2100, 0xfa03f000, 0x28009810, 0x9801d06b,
    0x900c4240, 0x4270990c, 0x42404008, 0x42b02500, 0x9901d101, 0x99101840, 0x42811989, 0x1b84d904,
    0x2004e003, 0xbdf0b011, 0x2c009c10, 0x2701d049, 0x42bc02bf, 0x4627d800, 0x980f08a9, 0x18090089,
    0x463a2009, 0xf00006c0, 0x1970fa37, 0x200b0201, 0x06000a09, 0x48091809, 0x46386041, 0xe0199909,
    0x40026040, 0x00000872, 0x40023020, 0x40001000, 0x00434d30, 0xf0003034, 0xe0080034, 0x40023000,
    0x44ffffff, 0x6b65666b, 0x49ffffff, 0x4bffffff, 0x4300ffff, 0xf9faf000, 0x48f10401, 0x48f11809,
    0x980d6081, 0xfe2af7ff, 0x980d9000, 0x28006900, 0x4780d000, 0x28009800, 0x1be4d10d, 0x2c0019ed,
    0x08a9d1b5, 0x0089980f, 0x900f1808, 0x19769810, 0x90101b40, 0x2101d196, 0xf000980d, 0x9800f990,
    0xbdf0b011, 0xd0012800, 0xd1012a00, 0x47702004, 0x4614b570, 0x4adc0609, 0x4dda0a09, 0x60691889,
    0xfdfcf7ff, 0xd1032800, 0x602168a9, 0x606168e9, 0x2800bd70, 0x2900d00e, 0x48d2d00c, 0x07827880,
    0x2a020f92, 0x0980d008, 0xd0082802, 0x70082002, 0x47702000, 0x47702004, 0x70082000, 0x2001e7f8,
    0x2800e7f5, 0x2900d001, 0x2004d101, 0xb5704770, 0x23004dc4, 0x079278aa, 0x2a020f92, 0x4ac3d026,
    0x780c606a, 0x462278cb, 0x061b784c, 0x43220224, 0x0424788c, 0x431a4322, 0x0a12ba12, 0x021278cb,
    0x60aa431a, 0x79cb790c, 0x794c4622, 0x0224061b, 0x798c4322, 0x042479c9, 0x431a4322, 0x0a12ba12,
    0x430a0212, 0xf7ff60ea, 0x4603fda9, 0xbd704618, 0xd1012800, 0x47702004, 0x04094aad, 0xb5101889,
    0x60514aa8, 0xfd9af7ff, 0xb5ffbd10, 0x4614b08d, 0x460d461e, 0x980daa02, 0xfdc4f7ff, 0x9000a802,
    0x46294622, 0x980d9b09, 0xf91df000, 0xd12e2800, 0x98049d02, 0x42699000, 0x40014240, 0x42af424f,
    0x9800d101, 0x2c00183f, 0x0230d020, 0x1b7e9001, 0xd90042a6, 0x46304626, 0xf0009909, 0x022af937,
    0x0a122101, 0x18520609, 0x604a498e, 0x04009a01, 0x30ff4310, 0x980d6088, 0xfd60f7ff, 0xd1062800,
    0x1ba49800, 0x183f19ad, 0xd1e02c00, 0xb0112000, 0x2b00bdf0, 0x2004d101, 0xb5ff4770, 0x4616b08d,
    0x460c461d, 0x9f16aa02, 0xf7ff980d, 0xa802fd7b, 0x46329000, 0x9b0b4621, 0xf000980d, 0x2800f8d4,
    0x9c02d11d, 0xd01a2e00, 0x0638497a, 0x02211847, 0x0a092001, 0x18090640, 0x60414872, 0x68296087,
    0x980d60c1, 0xfd2af7ff, 0xd00a2800, 0x29009917, 0x600cd000, 0x29009918, 0x2200d001, 0xb011600a,
    0x990bbdf0, 0x08891a76, 0x194d0089, 0x190c990b, 0xd1dc2e00, 0xbdf0b011, 0xd1012800, 0x47702004,
    0x04094a65, 0xb5101889, 0x60514a5e, 0xfd06f7ff, 0x2800bd10, 0x2a00d001, 0x2004d101, 0xb5104770,
    0x290a4614, 0x000ad222, 0x7912447a, 0x44971892, 0x0d080604, 0x1513110f, 0x68c01917, 0x6840e013,
    0x7a01e011, 0xf0006840, 0xe00cf8b1, 0xe00a7a00, 0xe0086800, 0xe0062001, 0xe0046940, 0xe0026980,
    0xe0006a00, 0x60206a40, 0xbd102000, 0xbd10206a, 0x28002300, 0x2004d101, 0xb4104770, 0xd0232906,
    0x2905dc02, 0xe01fd80d, 0xd01d2909, 0x2907dc04, 0x2908d01a, 0xe017d105, 0x2920b2d4, 0x2921d005,
    0x236ad009, 0x4618bc10, 0x2a004770, 0x2a01d001, 0x7244d105, 0x2a00e7f6, 0x2a01d004, 0xbc10d002,
    0x47702077, 0xe7ed7284, 0xe7eb2376, 0xd00e2800, 0x680a482c, 0x680a61c2, 0x429a69c3, 0x684ad105,
    0x68496182, 0x42816980, 0x2069d003, 0x20044770, 0x20004770, 0x28004770, 0x2900d008, 0x4821d006,
    0x600a69c2, 0x60486980, 0x47702000, 0x47702004, 0x47702000, 0x70012100, 0x46087041, 0x29014770,
    0x481ed110, 0x491e6800, 0x42880a00, 0x481dd101, 0x481de000, 0x22016801, 0x60014311, 0x8f6ff3bf,
    0x8f4ff3bf, 0x28004770, 0x2004d101, 0xb4104770, 0x9c011e5b, 0xd1014219, 0xd002421a, 0x2065bc10,
    0x68e04770, 0xd8074288, 0x18896923, 0x428818c0, 0xbc10d302, 0x47702000, 0x2066bc10, 0x00004770,
    0x0000ffff, 0x40023000, 0x4100ffff, 0x45ffffff, 0x4000ffff, 0x00ffffff, 0x4a00ffff, 0x40001000,
    0x00434d30, 0xf0003034, 0xe0080034, 0x460bb530, 0x20004601, 0x24012220, 0x460de009, 0x429d40d5,
    0x461dd305, 0x1b494095, 0x40954625, 0x46151940, 0x2d001e52, 0xbd30dcf1, 0x430b4603, 0xd003079b,
    0xc908e009, 0xc0081f12, 0xd2fa2a04, 0x780be003, 0x1c407003, 0x1e521c49, 0x4770d2f9, 0x40023004,
    0x4002301c, 0x40023018, 0x00100008, 0x00200018, 0x00400030, 0x00800060, 0x010000c0, 0x02000180,
    0x04000300, 0x00000600, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000, 0x00000000,
    0x00000000
    ],

    'pc_init' : 0x20000021,
    'pc_unInit': 0x20000083,
    'pc_program_page': 0x200000cd,
    'pc_erase_sector': 0x200000bb,
    'pc_eraseAll' : 0x200000ad,

    'static_base' : 0x200009c8,
    'begin_stack' : 0x20000000 + 0x00001400,
    'begin_data' : 0x20000000 + 0x00002000,
    'page_size' : 0x00000200,
    'analyzer_supported' : True,
    'analyzer_address' : 0x8000000,  # Analyzer 0x8000000..0x80000600
    'page_buffers' : [0x20003000, 0x20004000],   # Enable double buffering
    'min_program_length' : 8,
};

# Derive from Flash instead of Flash_Kinetis since the FCF is in IFR and not main flash.
class Flash_k32w042s(Flash):
    def __init__(self, target):
        super(Flash_k32w042s, self).__init__(target, flash_algo)

class K32W042S(Kinetis):

    memoryMap = MemoryMap(
        FlashRegion(name='flash0',      start=         0,   length=0x100000,    blocksize=0x1000, isBootMemory=True),
        FlashRegion(name='flash1',      start= 0x1000000,   length=0x40000,     blocksize=0x800),
        RamRegion(  name='m4 itcm',     start= 0x8000000,   length=0x10000),
        RomRegion(  name='boot rom',    start= 0x8800000,   length=0xc000),
        RamRegion(  name='m0p tcm',     start= 0x9000000,   length=0x20000),
        RamRegion(  name='m4 dtcm',     start=0x20000000,   length=0x30000),
        RamRegion(  name='flexram',     start=0x48000000,   length=0x1000),
        RamRegion(  name='usb ram',     start=0x48010000,   length=0x800),
        )

    def __init__(self, link):
        super(K32W042S, self).__init__(link, self.memoryMap)

        svdPath = os.path.join(os.path.dirname(__file__), "K32W042S1M2_M4.xml")
        if os.path.exists(svdPath):
            self._svd_location = SVDFile(vendor="NXP", filename=svdPath, is_local=True)

    def create_init_sequence(self):
        seq = super(K32W042S, self).create_init_sequence()

        seq.insert_after('create_cores',
            ('disable_rom_remap', self.disable_rom_remap)
            )

        return seq

    def perform_halt_on_connect(self):
        if self.halt_on_connect:
            # Prevent the target from resetting if it has invalid code
            with Timeout(HALT_TIMEOUT) as to:
                while to.check():
                    self.mdm_ap.write_reg(MDM_CTRL, MDM_CTRL_DEBUG_REQUEST | MDM_CTRL_CORE_HOLD_RESET)
                    if self.mdm_ap.read_reg(MDM_CTRL) & (MDM_CTRL_DEBUG_REQUEST | MDM_CTRL_CORE_HOLD_RESET) == (MDM_CTRL_DEBUG_REQUEST | MDM_CTRL_CORE_HOLD_RESET):
                        break
                else:
                    raise RuntimeError("Timed out attempting to set DEBUG_REQUEST and CORE_HOLD_RESET in MDM-AP")

            # We can now deassert reset.
            self.dp.assert_reset(False)

            # Enable debug
            self.aps[0].writeMemory(CortexM.DHCSR, CortexM.DBGKEY | CortexM.C_DEBUGEN)

            # Disable holding the core in reset, leave MDM halt on
            self.mdm_ap.write_reg(MDM_CTRL, MDM_CTRL_DEBUG_REQUEST)

            # Wait until the target is halted
            with Timeout(HALT_TIMEOUT) as to:
                while to.check():
                    if self.mdm_ap.read_reg(MDM_CORE_STATUS) & MDM_CORE_STATUS_CM4_HALTED != MDM_CORE_STATUS_CM4_HALTED:
                        break
                    log.debug("Waiting for mdm halt")
                    sleep(0.01)
                else:
                    raise RuntimeError("Timed out waiting for core to halt")

            # release MDM halt once it has taken effect in the DHCSR
            self.mdm_ap.write_reg(MDM_CTRL, 0)

            # sanity check that the target is still halted
            if self.getState() == Target.TARGET_RUNNING:
                raise RuntimeError("Target failed to stay halted during init sequence")

    def disable_rom_remap(self):
        # Disable ROM vector table remapping.
        self.aps[0].write32(SMC0_MR, SMC_MR_BOOTCFG_MASK)
        self.aps[0].write32(SMC1_MR, SMC_MR_BOOTCFG_MASK)

