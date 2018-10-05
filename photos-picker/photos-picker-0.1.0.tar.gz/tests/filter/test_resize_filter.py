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
            ((200, 25), (100, 25)),
            ((750, 150), (600, 150)),
            ((500, 250), (500, 125)),
        )

    @unittest_dataprovider.data_provider(provider_execute)
    def test_execute(self, filter_size, expected_img_size):
        """
        Test execute method

        :param tuple filter_size      : parameterized size of the filter
        :param tuple expected_img_size: expected size of the returned image
        """
        original_img = mock.Mock()
        original_img.size = (400, 100)
        original_img.format = 'JPEG'

        resized_mock = mock.Mock()
        original_img.resize.return_value = resized_mock

        sut = ResizeFilter(filter_size[0], filter_size[1])
        resized_img = sut.execute(original_img, 'myexifdata')

        original_img.resize.assert_called_once_with(
            (expected_img_size[0], expected_img_size[1]),
            Image.ANTIALIAS
        )

        self.assertEqual(resized_mock, resized_img)

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
