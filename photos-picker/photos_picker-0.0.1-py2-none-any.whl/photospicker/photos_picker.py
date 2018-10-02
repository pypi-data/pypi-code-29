from event.start_upload_event import StartUploadEvent
from event.end_upload_event import EndUploadEvent
from event.start_filter_event import StartFilterEvent
from event.end_filter_event import EndFilterEvent
from zope.event import notify
from photospicker.picker.abstract_picker import AbstractPicker  # noqa
from photospicker.uploader.abstract_uploader import AbstractUploader  # noqa
import ntpath


class PhotosPicker:
    """
    Select photos accorting to a chosen strategy and
    copy them to a chosen destination
    """

    def __init__(self, picker, filters, uploader):
        """
        Constructor

        :param AbstractPicker picker    : photo selection strategy
        :param tuple filters            : filters
        :param AbstractUploader uploader: upload strategy
        """
        self._picker = picker
        self._filters = filters
        self._uploader = uploader

    def run(self):
        """Run photo selection and upload"""
        self._picker.initialize()
        self._picker.scan()

        total_picked = len(self._picker.picked_file_paths)

        self._uploader.initialize()
        for key, filepath in enumerate(self._picker.picked_file_paths):
            rank = key + 1
            with open(filepath, mode='rb') as f:
                file_content = f.read()

            for photo_filter in self._filters:
                notify(StartFilterEvent(photo_filter, filepath))
                file_content = photo_filter.execute(file_content)
                notify(EndFilterEvent(photo_filter, filepath))

            notify(StartUploadEvent(filepath, rank, total_picked))
            self._uploader.increase_photo_counter()
            self._uploader.upload(file_content, ntpath.basename(filepath))
            notify(EndUploadEvent(filepath, rank, total_picked))
