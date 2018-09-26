"""Various utility functions for use with the DVEO API module"""

import xmltodict


def parse_xsd(xml):
    """Parses API xsd document from xml string.

    :param str xml: XSD document in string form
    :return: dict with operations: parameters
    :rtype: dict
    """
    xmldata = xmltodict.parse(xml, attr_prefix="", namespaces={"xs": None})
    output = dict()

    for oper in xmldata["schema"]["complexType"]:
        params = output.setdefault(oper["name"], [])
        if oper.get("sequence"):
            if isinstance(oper["sequence"]["element"], list):
                for param in oper["sequence"]["element"]:
                    params.append(param["name"])
            else:
                params.append(oper["sequence"]["element"]["name"])

    return output
