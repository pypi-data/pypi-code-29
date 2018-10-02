from unittest import TestCase
from photospicker.filter.resize_filter import ResizeFilter
from io import BytesIO
from PIL import Image
import mock
import unittest_dataprovider


class TestResizeFilter(TestCase):
    """Unit tests for ResizeFilter"""

    @staticmethod
    def provider_execute():
        """
        Data provider for test_execute

        :return: tuple
        """
        return (
            ((200, 100), (200, 50)),
            ((100, 200), (200, 50)),
            ((200, 25), (100, 25))
        )

    @unittest_dataprovider.data_provider(provider_execute)
    @mock.patch('PIL.Image.open')
    def test_execute(self, filter_size, expected_img_size, image_open_mock):
        """
        Test execute method

        :param mock.MagicMock image_open_mock   : mock for Image.open
        """
        image_open_mock.side_effect = self._image_open_side_effect

        self._original_img = mock.Mock()
        self._original_img.size = (400, 100)
        self._original_img.format = 'JPEG'

        resized_mock = mock.Mock()
        resized_mock.save.side_effect = self._image_save_side_effect
        self._original_img.resize.return_value = resized_mock

        sut = ResizeFilter(filter_size[0], filter_size[1])
        content = sut.execute('mycontent')

        self._original_img.resize.assert_called_once_with(
            (expected_img_size[0], expected_img_size[1]),
            Image.ANTIALIAS
        )

        resized_mock.save.assert_called_once()
        self.assertEqual('myresizedcontent', content)

    def _image_open_side_effect(self, bytesio):
        """
        Closure for Image.open side effect

        :param BytesIO bytesio: bytesIO instance passed to Image.open

        :return mock.Mock
        """
        self.assertIsInstance(bytesio, BytesIO)
        self.assertEqual('mycontent', bytesio.getvalue())

        return self._original_img

    def _image_save_side_effect(self, bytesio, img_format):
        """
        Closure for Image.save side effect

        :param BytesIO bytesio: bytesIO instance passed to Image.save
        :param str img_format : originam image format

        :return: BytesIO
        """
        self.assertIsInstance(bytesio, BytesIO)
        self.assertEqual('JPEG', img_format)

        bytesio.write('myresizedcontent')
