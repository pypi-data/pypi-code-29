from unittest import TestCase
from kaze.Prompt import Utils
from kazecore.Fixed8 import Fixed8
from kazecore.UInt160 import UInt160
import mock
from kaze.SmartContract.ContractParameter import ContractParameter, ContractParameterType


class TestInputParser(TestCase):

    def test_utils_1(self):

        args = [1, 2, 3]

        args, kaze, stream = Utils.get_asset_attachments(args)

        self.assertEqual(args, [1, 2, 3])
        self.assertIsNone(kaze)
        self.assertIsNone(stream)

    def test_utils_2(self):

        args = []

        args, kaze, stream = Utils.get_asset_attachments(args)

        self.assertEqual(args, [])
        self.assertIsNone(kaze)
        self.assertIsNone(stream)

    def test_utils_3(self):

        args = None

        with self.assertRaises(Exception):
            Utils.get_asset_attachments(args)

    def test_utils_4(self):

        args = [1, 2, '--attach-kaze=100']

        args, kaze, stream = Utils.get_asset_attachments(args)

        self.assertEqual(args, [1, 2])
        self.assertEqual(kaze, Fixed8.FromDecimal(100))
        self.assertIsNone(stream)

    def test_utils_5(self):
        args = [1, 2, '--attach-stream=100.0003']

        args, kaze, stream = Utils.get_asset_attachments(args)

        self.assertEqual(args, [1, 2])
        self.assertEqual(stream, Fixed8.FromDecimal(100.0003))
        self.assertIsNone(kaze)

    def test_utils_6(self):
        args = [1, 2, '--attachstream=100.0003']

        args, kaze, stream = Utils.get_asset_attachments(args)

        self.assertEqual(args, [1, 2, '--attachstream=100.0003'])
        self.assertIsNone(kaze)
        self.assertIsNone(stream)

    def test_utils_7(self):
        args = [1, 2, '--attach-stream=100.0003', '--attach-kaze=5.7']

        args, kaze, stream = Utils.get_asset_attachments(args)

        self.assertEqual(args, [1, 2])
        self.assertEqual(kaze, None)
        self.assertEqual(stream, Fixed8.FromDecimal(100.0003))

    def test_utils_8(self):
        args = [1, 2, '--attach-stream=100.0003', '--attach-kaze=6']

        args, kaze, stream = Utils.get_asset_attachments(args)

        self.assertEqual(args, [1, 2])
        self.assertEqual(kaze, Fixed8.FromDecimal(6))
        self.assertEqual(stream, Fixed8.FromDecimal(100.0003))

    def test_owner_1(self):
        args = [1, 2]

        args, owners = Utils.get_owners_from_params(args)

        self.assertEqual(args, [1, 2])
        self.assertIsNone(owners)

    def test_owner_2(self):
        args = [1, 2, "--owners=['ABC','DEF',]"]

        args, owners = Utils.get_owners_from_params(args)

        self.assertEqual(args, [1, 2])
        self.assertEqual(owners, set())

    def test_owner_3(self):
        args = [1, 2, "--owners=['APRgMZHZubii29UXF9uFa6sohrsYupNAvx','AXjaFSP23Jkbe6Pk9pPGT6NBDs1HVdqaXK',]"]

        args, owners = Utils.get_owners_from_params(args)

        self.assertEqual(args, [1, 2])
        self.assertEqual(len(owners), 2)

        self.assertIsInstance(list(owners)[0], UInt160)

    def test_owner_and_assets(self):

        args = [1, 2, "--owners=['APRgMZHZubii29UXF9uFa6sohrsYupNAvx','AXjaFSP23Jkbe6Pk9pPGT6NBDs1HVdqaXK',]", '--attach-kaze=10']

        args, owners = Utils.get_owners_from_params(args)

        args, kaze, stream = Utils.get_asset_attachments(args)

        self.assertEqual(args, [1, 2])
        self.assertEqual(len(owners), 2)

        self.assertIsInstance(list(owners)[0], UInt160)

        self.assertEqual(kaze, Fixed8.FromDecimal(10))

    def test_string_from_fixed8(self):

        amount_str = Utils.string_from_fixed8(100234, 8)

        self.assertEqual(amount_str, '0.00100234')

        amount_str = Utils.string_from_fixed8(534353400234, 8)

        self.assertEqual(amount_str, '5343.53400234')

        amount_str = Utils.string_from_fixed8(534353400234, 2)

        self.assertEqual(amount_str, '5343534002.34')

    def test_parse_no_address(self):

        params = ['a', 'b', 'c']

        params, result = Utils.get_parse_addresses(params)

        self.assertEqual(params, ['a', 'b', 'c'])
        self.assertTrue(result)

        params = ['a', 'b', 'c', '--no-parse-addr']

        params, result = Utils.get_parse_addresses(params)

        self.assertEqual(params, ['a', 'b', 'c'])
        self.assertFalse(result)

    def test_gather_param(self):

        with mock.patch('kaze.Prompt.Utils.get_input_prompt', return_value='hello') as fake_prompt:

            result, abort = Utils.gather_param(0, ContractParameterType.String)

            self.assertEqual(result, 'hello')

        with mock.patch('kaze.Prompt.Utils.get_input_prompt', return_value=1) as fake_prompt:

            result, abort = Utils.gather_param(0, ContractParameterType.Integer)

            self.assertEqual(result, 1)

        with mock.patch('kaze.Prompt.Utils.get_input_prompt', return_value='1') as fake_prompt:

            result, abort = Utils.gather_param(0, ContractParameterType.Integer)

            self.assertEqual(result, 1)

        with mock.patch('kaze.Prompt.Utils.get_input_prompt', return_value=1.03) as fake_prompt:

            result, abort = Utils.gather_param(0, ContractParameterType.Integer)

            self.assertEqual(result, 1)

        with mock.patch('kaze.Prompt.Utils.get_input_prompt', return_value="bytearray(b'abc')") as fake_prompt:

            result, abort = Utils.gather_param(0, ContractParameterType.ByteArray)

            self.assertEqual(result, bytearray(b'abc'))

        with mock.patch('kaze.Prompt.Utils.get_input_prompt', return_value="b'abc'") as fake_prompt:

            result, abort = Utils.gather_param(0, ContractParameterType.ByteArray)

            self.assertEqual(result, bytearray(b'abc'))

        with mock.patch('kaze.Prompt.Utils.get_input_prompt', return_value="abc'") as fake_prompt:

            result, abort = Utils.gather_param(0, ContractParameterType.Boolean)

            self.assertEqual(result, True)

        with mock.patch('kaze.Prompt.Utils.get_input_prompt', return_value=0) as fake_prompt:

            result, abort = Utils.gather_param(0, ContractParameterType.Boolean)

            self.assertEqual(result, False)

        with mock.patch('kaze.Prompt.Utils.get_input_prompt', return_value=0) as fake_prompt:

            result, abort = Utils.gather_param(0, ContractParameterType.Boolean)

            self.assertEqual(result, False)

        with mock.patch('kaze.Prompt.Utils.get_input_prompt', return_value='AeV59NyZtgj5AMQ7vY6yhr2MRvcfFeLWSb') as fake_prompt:

            result, abort = Utils.gather_param(0, ContractParameterType.ByteArray)

            self.assertEqual(result, bytearray(b'\xf9\x1dkp\x85\xdb|Z\xaf\t\xf1\x9e\xee\xc1\xca<\r\xb2\xc6\xec'))

        with mock.patch('kaze.Prompt.Utils.get_input_prompt', return_value='["a","b","c"]') as fake_prompt:

            result, abort = Utils.gather_param(0, ContractParameterType.Array)

            self.assertEqual(result, ['a', 'b', 'c'])

        with mock.patch('kaze.Prompt.Utils.get_input_prompt', return_value='["a","b","c", [1, 3, 4], "e"]') as fake_prompt:

            result, abort = Utils.gather_param(0, ContractParameterType.Array)

            self.assertEqual(result, ['a', 'b', 'c', [1, 3, 4], 'e'])

        with mock.patch('kaze.Prompt.Utils.get_input_prompt', return_value='["a","b","c", [1, 3, 4], "e"') as fake_prompt:
            result, abort = Utils.gather_param(0, ContractParameterType.Array, do_continue=False)

            self.assertEqual(result, None)
