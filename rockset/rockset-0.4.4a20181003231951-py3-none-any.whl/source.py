"""
Introduction
------------
Source objects represent various data sources that could be used to create
collections.

Example usage
-------------
::

    from rockset import Client, Q, F
    import os

    rs = Client()

    # create a collection from an AWS S3 bucket
    integration = rs.Integration.retrieve('aws-rockset-read-only')
    s3 = rs.Source.s3(bucket='my-s3-bucket',
        integration=integration)
    newcoll = rs.Collection.create(name='newcoll', sources=[s3])

Create AWS S3 source for a collection
-------------------------------------
AWS S3 buckets can be used as a data source for collections::

    from rockset import Client, Q, F
    import os

    rs = Client()

    # create a collection from an AWS S3 bucket
    integration = rs.Integration.retrieve('aws-rockset-read-only')
    s3 = rs.Source.s3(bucket='my-s3-bucket',
        integration=integration)
    newcoll = rs.Collection.create(name='newcoll', sources=[s3])

.. automethod :: rockset.Source.s3

"""

import csv

from rockset.integration import Integration

from rockset.query import FieldRef


class Source(object):
    def __str__(self):
        return str(vars(self))

    def __iter__(self):
        for k, v in vars(self).items():
            yield (k, v)

    @classmethod
    def s3(
        cls,
        bucket,
        prefixes=None,
        integration=None,
        mappings=None,
        data_format=None,
        csv_params=None
    ):
        """ Creates a source object to represent an AWS S3 bucket as a
        data source for a collection.

        Args:
            bucket (str): Name of the S3 bucket
            prefixes (list of str): Path prefix to only source S3 objects that
                are recursively within the given path. (optional)
            mappings (list of tuples): Each tuple has 2 fields as:
                (input_path, masking_function) of type (FieldRef, str)
            integration (rockset.integration.Integration): An Integration object (optional)
            data_format (str): oneof "json", "parquet, "xml" or "csv"
                [default: "auto_detect"]
            csv_params (CsvParams): if CSV, then specifications of the CSV format
        """
        return S3Source(
            bucket=bucket,
            prefixes=prefixes,
            mappings=mappings,
            integration=integration,
            data_format=data_format,
            csv_params=csv_params
        )

    @classmethod
    def csv_params(
        cls,
        separator=None,
        encoding=None,
        first_line_as_column_names=None,
        column_names=None,
        column_types=None
    ):
        """ Creates a object to represent options needed to parse a CSV file

        Args:
            separator (str): The separator between column values in a line
            encoding (str): The encoding format of data, one of "UTF-8",
                "UTF-16" "US_ASCII"
                [default: "US-ASCII"]
            first_line_as_column_names (boolean): Set to true if the first line
                of a data object has the names of columns to be used. If this is
                set to false, the the column names are auto generated.
                [default: False]
            column_names (list of strings): The names of columns
            column_types (list of strings): The types of columns
        """
        return CsvParams(
            separator=separator,
            encoding=encoding,
            first_line_as_column_names=first_line_as_column_names,
            column_names=column_names,
            column_types=column_types
        )

    @classmethod
    def collection(cls, name=None, query=None, mappings=None):
        """ Source object to represent a collection as a data source.

        Args:
            name (str): Name of the source collection
            query (Query): Query to filter documents in the source
                collection (optional).
            mappings (list of tuples): Each tuple has 2 fields as:
                (projection, output_field) of type (str, FieldRef)

       """
        return CollectionSource(name=name, query=query, mappings=mappings)


class S3Source(Source):
    def __init__(
        self,
        bucket,
        prefixes=None,
        mappings=None,
        integration=None,
        data_format=None,
        csv_params=None
    ):
        if isinstance(integration, Integration):
            self.integration_name = integration.name
        elif integration is not None:
            ret = 'TypeError: invalid object type {} for integration'.format(
                type(integration)
            )
            raise TypeError(ret)
        self.s3 = {
            'format': data_format,
            'bucket': bucket,
        }
        if prefixes is not None:
            self.s3['prefixes'] = prefixes

        if data_format is not None:
            self.format = data_format

        self.format_params_csv = {
            'firstLineAsColumnNames': False,
            'separator': ",",
            'encoding': "US-ASCII",
            'columnNames': [],
        }
        if csv_params is not None:
            if csv_params.separator is not None:
                self.format_params_csv['separator'] = csv_params.separator
            if csv_params.encoding is not None:
                self.format_params_csv['encoding'] = csv_params.encoding
            if csv_params.first_line_as_column_names is not None:
                self.format_params_csv['firstLineAsColumnNames'
                                      ] = csv_params.first_line_as_column_names
            if csv_params.column_names is not None:
                if not isinstance(csv_params.column_names, list):
                    raise ValueError(
                        "column names of type {} "
                        "not supported".format(type(csv_params.column_names))
                    )
                self.format_params_csv['columnNames'] = csv_params.column_names
            if csv_params.column_types is not None:
                if not isinstance(csv_params.column_types, list):
                    raise ValueError(
                        "column types of type {} "
                        "not supported".format(type(csv_params.column_types))
                    )
                self.format_params_csv['columnTypes'] = csv_params.column_types

        if mappings:
            mo = []
            for m in mappings:
                if type(m) != tuple or len(m) != 2:
                    raise ValueError(
                        "each mapping needs to be a tuple with 2 "
                        "fields as: (input_path, masking_function)"
                    )
                if not isinstance(m[0], FieldRef):
                    raise ValueError(
                        "input_path of type {} "
                        "not supported".format(type(m[0]))
                    )
                mo.append(
                    {
                        'input_path': list(m[0]),
                        'mask': {
                            'name': str(m[1])
                        }
                    }
                )

            self.s3['mappings'] = mo


class CollectionSource(Source):
    def __init__(self, name=None, query=None, mappings=None):
        self.collection = {
            'name': name,
        }

        if query:
            self.collection['query'] = str(query)

        if mappings:
            mo = []
            for m in mappings:
                if type(m) != tuple or len(m) != 2:
                    raise ValueError(
                        "each mapping needs to be a tuple with 2 "
                        "fields as: (projection, output_field)"
                    )
                if not isinstance(m[1], FieldRef):
                    raise ValueError(
                        "output_field of type {} "
                        "not supported".format(type(m[1]))
                    )
                output_field_path = list(m[1])
                if len(output_field_path) != 1:
                    raise ValueError("output_field cannot be nested")

                mo.append(
                    {
                        'projection': m[0],
                        'output_field': output_field_path[0]
                    }
                )

            self.collection['mappings'] = mo


class GmailSource(Source):
    def __init__(self, refresh_token, access_token):
        self.gmail = {
            'refresh_token': refresh_token,
            'access_token': access_token
        }


#
# Parameters needed for a CSV formatted data set
#
class CsvParams:
    def __init__(
        self, separator, encoding, first_line_as_column_names, column_names,
        column_types
    ):
        self.separator = separator
        self.encoding = encoding
        self.first_line_as_column_names = first_line_as_column_names
        self.column_names = column_names
        self.column_types = column_types
