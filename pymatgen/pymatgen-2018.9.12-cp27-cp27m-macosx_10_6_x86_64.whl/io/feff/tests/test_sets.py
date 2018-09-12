# coding: utf-8
# Copyright (c) Pymatgen Development Team.
# Distributed under the terms of the MIT License.

from __future__ import unicode_literals

import unittest

import os

from pymatgen import Structure
from pymatgen.io.feff.sets import MPXANESSet, MPELNESSet, FEFFDictSet, MPEXAFSSet
from pymatgen.io.feff.inputs import Potential, Tags, Atoms, Header
from pymatgen.io.cif import CifParser, CifFile
import shutil
import numpy as np

test_dir = os.path.join(os.path.dirname(__file__), "..", "..", "..", "..",
                        'test_files')


class FeffInputSetTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):

        cls.header_string = """* This FEFF.inp file generated by pymatgen
TITLE comment: From cif file
TITLE Source:  CoO19128.cif
TITLE Structure Summary:  Co2 O2
TITLE Reduced formula:  CoO
TITLE space group: (P6_3mc), space number:  (186)
TITLE abc:  3.297078   3.297078   5.254213
TITLE angles: 90.000000  90.000000 120.000000
TITLE sites: 4
* 1 Co     0.666667     0.333333     0.003676
* 2 Co     0.333334     0.666666     0.503676
* 3 O     0.333334     0.666666     0.121324
* 4 O     0.666667     0.333333     0.621325"""
        cif_file = os.path.join(test_dir, 'CoO19128.cif')
        cls.structure = CifParser(cif_file).get_structures()[0]
        cls.absorbing_atom = 'O'
        cls.mp_xanes = MPXANESSet(cls.absorbing_atom, cls.structure)

    def test_get_header(self):
        comment = 'From cif file'
        header = str(self.mp_xanes.header(source='CoO19128.cif', comment=comment))
        ref = self.header_string.splitlines()
        last4 = [" ".join(l.split()[2:]) for l in ref[-4:]]
        for i, l in enumerate(header.splitlines()):
            if i < 9:
                self.assertEqual(l, ref[i])
            else:
                s = " ".join(l.split()[2:])
                self.assertIn(s, last4)

    def test_getfefftags(self):
        tags = self.mp_xanes.tags.as_dict()
        self.assertEqual(tags['COREHOLE'], "FSR",
                         "Failed to generate PARAMETERS string")

    def test_get_feffPot(self):
        POT = str(self.mp_xanes.potential)
        d, dr = Potential.pot_dict_from_string(POT)
        self.assertEqual(d['Co'], 1, "Wrong symbols read in for Potential")

    def test_get_feff_atoms(self):
        atoms = str(self.mp_xanes.atoms)
        self.assertEqual(atoms.splitlines()[3].split()[4], self.absorbing_atom,
                         "failed to create ATOMS string")

    def test_to_and_from_dict(self):
        f1_dict = self.mp_xanes.as_dict()
        f2 = MPXANESSet.from_dict(f1_dict)
        self.assertEqual(f1_dict, f2.as_dict())

    def test_user_tag_settings(self):
        tags_dict_ans = self.mp_xanes.tags.as_dict()
        tags_dict_ans["COREHOLE"] = "RPA"
        tags_dict_ans["EDGE"] = "L1"
        user_tag_settings = {"COREHOLE": "RPA", "EDGE": "L1"}
        mp_xanes_2 = MPXANESSet(self.absorbing_atom, self.structure,
                                user_tag_settings=user_tag_settings)
        self.assertEqual(mp_xanes_2.tags.as_dict(), tags_dict_ans)

    def test_eels_to_from_dict(self):
        elnes = MPELNESSet(self.absorbing_atom, self.structure, radius=5.0,
                           beam_energy=100, beam_direction=[1, 0, 0],
                           collection_angle=7, convergence_angle=6)
        elnes_dict = elnes.as_dict()
        elnes_2 = MPELNESSet.from_dict(elnes_dict)
        self.assertEqual(elnes_dict, elnes_2.as_dict())

    def test_eels_tags_set(self):
        radius = 5.0
        user_eels_settings = {
            'ENERGY': '4 0.04 0.1',
            'BEAM_ENERGY': '200 1 0 1',
            'ANGLES': '2 3'}
        elnes = MPELNESSet(self.absorbing_atom, self.structure, radius=radius,
                           user_eels_settings=user_eels_settings)
        elnes_2 = MPELNESSet(self.absorbing_atom, self.structure, radius=radius,
                             beam_energy=100, beam_direction=[1, 0, 0],
                             collection_angle=7, convergence_angle=6)
        self.assertEqual(elnes.tags["ELNES"]["ENERGY"],
                         user_eels_settings["ENERGY"])
        self.assertEqual(elnes.tags["ELNES"]["BEAM_ENERGY"],
                         user_eels_settings["BEAM_ENERGY"])
        self.assertEqual(elnes.tags["ELNES"]["ANGLES"],
                         user_eels_settings["ANGLES"])
        self.assertEqual(elnes_2.tags["ELNES"]["BEAM_ENERGY"], [100, 0, 1, 1])
        self.assertEqual(elnes_2.tags["ELNES"]["BEAM_DIRECTION"], [1, 0, 0])
        self.assertEqual(elnes_2.tags["ELNES"]["ANGLES"], [7, 6])

    def test_reciprocal_tags_and_input(self):
        user_tag_settings = {"RECIPROCAL": "", "KMESH": "1000"}
        elnes = MPELNESSet(self.absorbing_atom, self.structure,
                           user_tag_settings=user_tag_settings)
        self.assertTrue("RECIPROCAL" in elnes.tags)
        self.assertEqual(elnes.tags["TARGET"], 3)
        self.assertEqual(elnes.tags["KMESH"], "1000")
        self.assertEqual(elnes.tags["CIF"], "Co2O2.cif")
        self.assertEqual(elnes.tags["COREHOLE"], "RPA")
        all_input = elnes.all_input()
        self.assertNotIn("ATOMS", all_input)
        self.assertNotIn("POTENTIALS", all_input)
        elnes.write_input()
        structure = Structure.from_file("Co2O2.cif")
        self.assertTrue(self.structure.matches(structure))
        os.remove("HEADER")
        os.remove("PARAMETERS")
        os.remove("feff.inp")
        os.remove("Co2O2.cif")

    def test_small_system_EXAFS(self):
        exafs_settings = MPEXAFSSet(self.absorbing_atom, self.structure)
        self.assertFalse(exafs_settings.small_system)
        self.assertTrue('RECIPROCAL' not in exafs_settings.tags)

        user_tag_settings = {"RECIPROCAL": ""}
        exafs_settings_2 = MPEXAFSSet(self.absorbing_atom, self.structure, nkpts=1000,
                                      user_tag_settings=user_tag_settings)
        self.assertFalse(exafs_settings_2.small_system)
        self.assertTrue('RECIPROCAL' not in exafs_settings_2.tags)

    def test_number_of_kpoints(self):
        user_tag_settings = {"RECIPROCAL": ""}
        elnes = MPELNESSet(self.absorbing_atom, self.structure, nkpts=1000,
                           user_tag_settings=user_tag_settings)
        self.assertEqual(elnes.tags["KMESH"], [12, 12, 7])

    def test_large_systems(self):
        struct = Structure.from_file(os.path.join(test_dir, "La4Fe4O12.cif"))
        user_tag_settings = {"RECIPROCAL": "", "KMESH": "1000"}
        elnes = MPELNESSet("Fe", struct, user_tag_settings=user_tag_settings)
        self.assertNotIn("RECIPROCAL", elnes.tags)
        self.assertNotIn("KMESH", elnes.tags)
        self.assertNotIn("CIF", elnes.tags)
        self.assertNotIn("TARGET", elnes.tags)

    def test_postfeffset(self):
        self.mp_xanes.write_input(os.path.join('.', 'xanes_3'))
        feff_dict_input = FEFFDictSet.from_directory(os.path.join('.', 'xanes_3'))
        self.assertTrue(feff_dict_input.tags == Tags.from_file(os.path.join('.', 'xanes_3/feff.inp')))
        self.assertTrue(str(feff_dict_input.header()) == str(Header.from_file(os.path.join('.', 'xanes_3/HEADER'))))
        feff_dict_input.write_input('xanes_3_regen')
        origin_tags = Tags.from_file(os.path.join('.', 'xanes_3/PARAMETERS'))
        output_tags = Tags.from_file(os.path.join('.', 'xanes_3_regen/PARAMETERS'))
        origin_mole = Atoms.cluster_from_file(os.path.join('.', 'xanes_3/feff.inp'))
        output_mole = Atoms.cluster_from_file(os.path.join('.', 'xanes_3_regen/feff.inp'))
        original_mole_dist = np.array(origin_mole.distance_matrix[0, :]).astype(np.float64)
        output_mole_dist = np.array(output_mole.distance_matrix[0, :]).astype(np.float64)
        original_mole_shell = [x.species_string for x in origin_mole]
        output_mole_shell = [x.species_string for x in output_mole]

        self.assertTrue(np.allclose(original_mole_dist, output_mole_dist))
        self.assertTrue(origin_tags == output_tags)
        self.assertTrue(original_mole_shell == output_mole_shell)

        shutil.rmtree(os.path.join('.', 'xanes_3'))
        shutil.rmtree(os.path.join('.', 'xanes_3_regen'))

        reci_mp_xanes = MPXANESSet(self.absorbing_atom, self.structure,
                                   user_tag_settings={"RECIPROCAL": ""})
        reci_mp_xanes.write_input('xanes_reci')
        feff_reci_input = FEFFDictSet.from_directory(os.path.join('.', 'xanes_reci'))
        self.assertTrue("RECIPROCAL" in feff_reci_input.tags)

        feff_reci_input.write_input('Dup_reci')
        self.assertTrue(os.path.exists(os.path.join('.', 'Dup_reci', 'HEADER')))
        self.assertTrue(os.path.exists(os.path.join('.', 'Dup_reci', 'feff.inp')))
        self.assertTrue(os.path.exists(os.path.join('.', 'Dup_reci', 'PARAMETERS')))
        self.assertFalse(os.path.exists(os.path.join('.', 'Dup_reci', 'ATOMS')))
        self.assertFalse(os.path.exists(os.path.join('.', 'Dup_reci', 'POTENTIALS')))

        tags_original = Tags.from_file(os.path.join('.', 'xanes_reci/feff.inp'))
        tags_output = Tags.from_file(os.path.join('.', 'Dup_reci/feff.inp'))
        self.assertTrue(tags_original == tags_output)

        stru_orig = Structure.from_file(os.path.join('.', 'xanes_reci/Co2O2.cif'))
        stru_reci = Structure.from_file(os.path.join('.', 'Dup_reci/Co2O2.cif'))
        self.assertTrue(stru_orig.__eq__(stru_reci))

        shutil.rmtree(os.path.join('.', 'Dup_reci'))
        shutil.rmtree(os.path.join('.', 'xanes_reci'))

    def test_post_distdiff(self):
        feff_dict_input = FEFFDictSet.from_directory(os.path.join(test_dir, 'feff_dist_test'))
        self.assertTrue(feff_dict_input.tags == Tags.from_file(os.path.join(test_dir, 'feff_dist_test/feff.inp')))
        self.assertTrue(
            str(feff_dict_input.header()) == str(Header.from_file(os.path.join(test_dir, 'feff_dist_test/HEADER'))))
        feff_dict_input.write_input('feff_dist_regen')
        origin_tags = Tags.from_file(os.path.join(test_dir, 'feff_dist_test/PARAMETERS'))
        output_tags = Tags.from_file(os.path.join('.', 'feff_dist_regen/PARAMETERS'))
        origin_mole = Atoms.cluster_from_file(os.path.join(test_dir, 'feff_dist_test/feff.inp'))
        output_mole = Atoms.cluster_from_file(os.path.join('.', 'feff_dist_regen/feff.inp'))
        original_mole_dist = np.array(origin_mole.distance_matrix[0, :]).astype(np.float64)
        output_mole_dist = np.array(output_mole.distance_matrix[0, :]).astype(np.float64)
        original_mole_shell = [x.species_string for x in origin_mole]
        output_mole_shell = [x.species_string for x in output_mole]

        self.assertTrue(np.allclose(original_mole_dist, output_mole_dist))
        self.assertTrue(origin_tags == output_tags)
        self.assertTrue(original_mole_shell == output_mole_shell)

        shutil.rmtree(os.path.join('.', 'feff_dist_regen'))


if __name__ == '__main__':
    unittest.main()
