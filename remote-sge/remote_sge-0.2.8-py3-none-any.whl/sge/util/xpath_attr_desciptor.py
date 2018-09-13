
"""
Custom descriptor classes for special object attribute bahaviors
"""
from sge.util.serializers import (element_text)

class XPathAttr(object):
    """
    Descriptor for properties on the :class:`sge.status.JobDetail` class, to
    translate values from the XML given by qstat into more readable fashion.

    See the initializer and the getter for an understanding of the mechanics.
    """
    def __init__(self, xpath, converter=None):
        """
        Args:
            xpath (str): a relative XPath query describing where to find the
                attribute.

            converter: an object with a deserialize method, which will receive
                an XML node and return the appropriate data type.
        """
        self.xpath = xpath
        self.converter = converter

    def __get__(self, instance, _):
        """
        Looks up the appropriate node on the job detail :class:`~xml.etree.ElementTree`.
        If a converter is present, calls deserialize.

        Otherwise returns the text of the found node.
        """
        xml_element = instance.xml_node.find(self.xpath)
        if self.converter:
            return self.converter.deserialize(xml_element)
        else:
            return element_text(xml_element)

