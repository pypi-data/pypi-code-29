"""
 mbed CMSIS-DAP debugger
 Copyright (c) 2017 ARM Limited

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
from __future__ import print_function
from ...core.memory_map import (MemoryRange, MemoryMap)
from .decoder import (ElfSymbolDecoder, DwarfAddressDecoder)
from elftools.elf.elffile import ELFFile
from elftools.elf.constants import SH_FLAGS
import logging
import six

##
# @brief Memory range for a section of an ELF file.
#
# Objects of this class represent sections of an ELF file. See the ELFBinaryFile class documentation
# for details of how sections are selected and how to get instances of this class.
#
# If a region in the target's memory map can be found that contains the section, it will be
# accessible via the instance's _region_ attribute. Otherwise _region_ will be `None`. A maximum of
# one associated memory region is supported, even if the section spans multiple regions.
#
# The contents of the ELF section can be read via the `data` property as a `bytearray`. The data is
# read from the file only once and cached.
class ELFSection(MemoryRange):
    def __init__(self, elf, sect):
        self._elf = elf
        self._section = sect
        self._name = self._section.name
        self._data = None

        # Look up the corresponding memory region.
        start = self._section['sh_addr']
        length = self._section['sh_size']
        regions = self._elf._memory_map.getIntersectingRegions(start=start, length=length)
        region = regions[0] if len(regions) else None

        super(ELFSection, self).__init__(start=start, length=length, region=region)

    @property
    def name(self):
        return self._name
        
    @property
    def type(self):
        return self._section['sh_type']

    @property
    def flags(self):
        return self._section['sh_flags']

    @property
    def data(self):
        if self._data is None:
            self._data = bytearray(self._section.data())
        return self._data

    @property
    def flags_description(self):
        flags = self.flags
        flagsDesc = ""
        if flags & SH_FLAGS.SHF_WRITE:
            flagsDesc += "WRITE|"
        if flags & SH_FLAGS.SHF_ALLOC:
            flagsDesc += "ALLOC|"
        if flags & SH_FLAGS.SHF_EXECINSTR:
            flagsDesc += "EXECINSTR"
        if flagsDesc[-1] == '|':
            flagsDesc = flagsDesc[:-1]
        return flagsDesc

    def __repr__(self):
        return "<ELFSection@0x{0:x} {1} {2} {3} {4} {5}>".format(
            id(self), self.name, self.type, self.flags_description, hex(self.start), hex(self.length))

##
# @brief An ELF binary executable file.
#
# Examines the ELF and provides several lists of useful data: section objects, and both used
# and unused ranges of memory.
#
# An ELFSection object is created for each of the sections of the file that are loadable code or
# data, or otherwise occupy memory. These are normally the .text, .rodata, .data, and .bss
# sections. More specifically, the list of sections contains any section with a type of
# `SHT_PROGBITS` or `SHT_NOBITS`. Also, at least one of the `SHF_WRITE`, `SHF_ALLOC`, or
# `SHF_EXECINSTR` flags must be set.
#
# The set of sections is compared with the target's memory map to produce a lists of the used
# (occupied) and unused (unoccupied) ranges of memory. Note that if the executable uses ranges
# of memory not mapped with a section of the ELF file, those ranges will not be considered in
# the used/unused lists. Also, only ranges completely contained within a region of the memory
# map are considered.
class ELFBinaryFile(object):
    def __init__(self, elf, memory_map):
        if isinstance(elf, six.string_types):
            self._file = open(elf, 'rb')
            self._owns_file = True
        else:
            self._file = elf
            self._owns_file = False
        self._elf = ELFFile(self._file)
        self._memory_map = memory_map or MemoryMap()

        self._symbol_decoder = None
        self._address_decoder = None

        self._extract_sections()
        self._compute_regions()

    ## @brief Close the ELF file if it is owned by this instance.
    def __del__(self):
        if self._owns_file:
            self.close()

    def _extract_sections(self):
        # Get list of interesting sections.
        self._sections = []
        sections = self._elf.iter_sections()
        for s in sections:
            # Skip sections not of these types.
            if s['sh_type'] not in ('SHT_PROGBITS', 'SHT_NOBITS'):
                continue

            # Skip sections that don't have one of these flags set.
            if s['sh_flags'] & (SH_FLAGS.SHF_WRITE | SH_FLAGS.SHF_ALLOC | SH_FLAGS.SHF_EXECINSTR) == 0:
                continue

            self._sections.append(ELFSection(self, s))
        self._sections.sort(key=lambda x: x.start)

    def _dump_sections(self):
        for s in self._sections:
            print("{0:<20} {1:<25} {2:<10} {3:<10}".format(
                s.name, s.flags_description, hex(s.start), hex(s.length)))

    def _compute_regions(self):
        used = []
        unused = []
        for region in self._memory_map:
            current = region.start
            for sect in self._sections:
                start = sect.start
                length = sect.length

                # Skip if this section isn't within this memory region.
                if not region.containsRange(start, length=length):
                    continue

                # Add this section as used.
                used.append(MemoryRange(start=start, length=length, region=region))

                # Add unused segment.
                if start > current:
                    unused.append(MemoryRange(start=current, length=(start - current), region=region))

                current = start + length

            # Add a final unused segment of the region.
            if region.end > current:
                unused.append(MemoryRange(start=current, end=region.end, region=region))
        self._used = used
        self._unused = unused

    def close(self):
        self._file.close()
        self._owns_file = False

    ##
    # @brief Access the list of sections in the ELF file.
    # @return A list of ELFSection objects sorted by start address.
    @property
    def sections(self):
        return self._sections

    ##
    # @brief Access the list of used ranges of memory in the ELF file.
    # @return A list of MemoryRange objects sorted by start address.
    @property
    def used_ranges(self):
        return self._used

    ##
    # @brief Access the list of unused ranges of memory in the ELF file.
    # @return A list of MemoryRange objects sorted by start address.
    @property
    def unused_ranges(self):
        return self._unused

    @property
    def symbol_decoder(self):
        if self._symbol_decoder is None:
            self._symbol_decoder = ElfSymbolDecoder(self._elf)
        return self._symbol_decoder

    @property
    def address_decoder(self):
        if self._address_decoder is None:
            self._address_decoder = DwarfAddressDecoder(self._elf)
        return self._address_decoder



