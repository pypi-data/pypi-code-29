import mock
from photospicker.picker.last_photos_picker import LastPhotosPicker
from unittest import TestCase


class TestLastPhotosPicker(TestCase):
    """Test class for LastPhotosPicker"""

    @mock.patch('PIL.Image.open', new_callable=mock.Mock)
    @mock.patch('os.walk')
    def test_scan(self, walk_mock, image_open_mock):
        """
        Test scan method

        :param mock.Mock walk_mock:       mock for walk method
        :param mock.Mock image_open_mock: mock for PIL Image mock method
        """

        walk_mock.return_value = [['', [], [
            'myphoto1.jpg',
            'myphoto2.jpg',
            'myphoto3.jpg',
            'myphoto4.jpg'
        ]]]

        image_mock1 = mock.Mock()
        image_mock1._getexif.return_value = {
            36865: 'myData',
            36867: '2017-05-01 23:50:00'
        }

        image_mock2 = mock.Mock()
        image_mock2._getexif.return_value = None

        image_mock3 = mock.Mock()
        image_mock3._getexif.return_value = {
            36867: '2017-05-01 23:49:50',
            36882: 'myOtherData'
        }

        image_mock4 = mock.Mock()
        image_mock4._getexif.return_value = {
            36864: 'myOtherData',
            36867: '2017-05-01 23:55:00',
            36888: 'anotherData'
        }

        image_open_mock.side_effect = [
            image_mock1,
            image_mock2,
            image_mock3,
            image_mock4
        ]

        sut = LastPhotosPicker('', 2)
        sut.initialize()
        sut.scan()

        image_open_mock.assert_has_calls([
           mock.call('myphoto1.jpg'),
           mock.call('myphoto2.jpg'),
           mock.call('myphoto3.jpg'),
           mock.call('myphoto4.jpg')
        ])

        self.assertEqual(
            ['myphoto4.jpg', 'myphoto1.jpg'],
            sut.picked_file_paths
        )
