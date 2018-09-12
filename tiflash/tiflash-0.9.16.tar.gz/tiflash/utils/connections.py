"""
helper module for finding installed connection types


Author: Cameron Webb
Date: March 2018
Contact: webbjcam@gmail.com

"""

import os
import re

from tiflash.utils import xmlhelper

CONNECTIONS_DIR = "/ccs_base/common/targetdb/connections"


class ConnectionsError(Exception):
    """Generic Connection Error"""
    pass


def get_connections_directory(ccs_path):
    """Returns full path to connections directory

    Args:
        ccs_path (str): full path to ccs installation to use

    Returns:
        str: full path to connections directory
    """
    connections_directory = os.path.normpath(ccs_path + "/" + CONNECTIONS_DIR)

    if not os.path.exists(connections_directory):
        raise ConnectionsError("Could not find 'connections' directory.")

    return connections_directory


def get_connections(ccs_path):
    """ Returns list of installed connection names.

    Searches "<ccs_path>/ccs_base/common/targetdb/connections" directory for
    installed connection names.

    Args:
        ccs_path (str): full path to ccs installation to use

    Returns:
        list: connection names

    Raises:
        ConnectionsError: raises exception if connections directory can not
            be found

    """
    #   Set Connections directory
    connections_directory = get_connections_directory(ccs_path)

    #   Get connections xmls
    connection_xmls = get_connection_xmls(ccs_path, full_path=True)

    connection_list = list()
    for cxml in connection_xmls:
        try:    # Some xmls are not valid connection xml files
            connection = get_connection_name(cxml)
        except Exception:
            continue
        connection_list.append(connection)

    return connection_list


def get_connection_xml_path(xml_name, ccs_path):
    """Returns full path to connection xml if exists, else returns None.

    Args:
        xml_name (str): name of connection to search xmls for (i.e. TIXDS110)
        ccs_path (str): path to ccs installation to use for searching xmls

    Returns:
        str or None: full path to connection xml if exists
            otherwise returns None

    Raises:
        ConnectionsError: raises exception if connections directory can not
            be found
    """
    connection_xml = None

    if not xml_name.endswith('.xml'):
        xml_name += ".xml"

    #   Set Connections directory
    connection_xmls = get_connection_xmls(ccs_path)

    if xml_name in connection_xmls:
        connection_xml = os.path.normpath(
                            get_connections_directory(ccs_path) + "/" + xml_name)

    return connection_xml



def get_connection_xmls(ccs_path, full_path=False):
    """Gets a list of the connection xmls files

    Args:
        ccs_path (str): path to ccs installation
        full_path (boolean, optional): returns full path of each connection xml

    Returns:
        list: list of connection xml files
    """
    conn_dir = get_connections_directory(ccs_path)
    conns = [f for f in os.listdir(conn_dir) if f.endswith('.xml')]

    if full_path:
        conns = [ os.path.abspath(conn_dir + '/' + c) for c in conns ]

    return conns


def get_connection_name(conn_xml):
    """ Returns full connection name (as specified in connectionxml)

    Opens connection xml file and reads 'desc' of connection tag.

    Args:
        conn_xml (str): full path to connection xml file to parse

    Returns:
        str: connection name

    Raises:
        ConnectionsError: raises exception xml is unable to be parsed

    """
    root = __get_connection_root(conn_xml)

    if root.tag != "connection":
        raise ConnectionsError("Error parsing connection xml: %s" % conn_xml)

    connection_name = xmlhelper.get_attrib_value(root.attrib, ["desc", "id"])

    return connection_name


def find_connection(connection_name, ccs_path):
    """ Returns full connection name(s) matching 'connection_name'

    Uses regex to try to match given 'connection_name' to all installed
    connection types.

    Args:
        connection_name (str): connection name to try to match (i.e. xds110)

    Returns:
        list: list of full connection names that matched the given
        connection_name

    Raises:
        ConnectionsError: raises exception if CCS installation can not be found

    """
    connections = get_connections(ccs_path)
    match_list = list()
    connection_re = re.compile(connection_name.lower())

    for c in connections:
        if connection_re.search(c.lower()) is not None:
            match_list.append(c)

    return match_list

def __get_connection_root(connection_path):
    """Returns the root Element of the connection file

    Args:
        connection_path (str): full path to connection file to parse

    Returns:
        xml.Element: root element of connection file
    """
    if not os.path.exists(connection_path):
        raise ConnectionsError("Could not find connection xml: %s" %
            connection_path)

    root = xmlhelper.get_xml_root(connection_path)

    return root
