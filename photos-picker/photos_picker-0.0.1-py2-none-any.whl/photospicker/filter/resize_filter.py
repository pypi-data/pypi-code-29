from photospicker.filter.abstract_filter import AbstractFilter
from PIL import Image
from io import BytesIO


class ResizeFilter(AbstractFilter):
    """Resize a photo"""

    def __init__(self, new_width, new_height):
        """
        Constructor

        :param int new_width : new width after filter execution
        :param int new_height: new height after filter execution
        """
        self._width = new_width
        self._height = new_height

    def execute(self, content):
        """
        Resize photo

        :param string content: binary content of the photo
        """
        original_img = Image.open(BytesIO(content))
        (original_width, original_height) = original_img.size

        diff_wh = self._width - self._height
        sign_diff_wh = diff_wh / abs(diff_wh)
        diff_original_wh = original_width - original_height
        sign_diff_original_wh = diff_original_wh / abs(diff_original_wh)

        if sign_diff_wh == sign_diff_original_wh:
            w = self._width
            h = self._height
        else:
            w = self._height
            h = self._width

        if original_width / original_height > w / h:
            ratio = float(w) / original_width
        else:
            ratio = float(h) / original_height

        resized_img = original_img.resize(
            (int(ratio * original_width), int(ratio * original_height)),
            Image.ANTIALIAS
        )
        b = BytesIO()
        resized_img.save(b, original_img.format)
        return b.getvalue()
