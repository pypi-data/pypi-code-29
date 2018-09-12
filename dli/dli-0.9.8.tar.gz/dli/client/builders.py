
class DatasetBuilder:
    """
    Dataset is grouping of related datafiles. It provides user with metadata required to consume and use the data.

    This builder object sets sensible defaults and exposes
    helper methods on how to configure its storage options.

    See description for each parameter, and whether they are optional or mandatory.

    :param str package_id: Mandatory. Package ID to which the dataset belongs to.
    :param str name: Mandatory. A descriptive name of a dataset. It should be unique within the package.
    :param str description: Mandatory. A short description of a package.
    :param str content_type: Mandatory. A way for the data steward to classify the type of data in the dataset (e.g. pricing).
    :param str data_format: Mandatory. The format of the data: csv, parquet, etc.
    :param str publishing_frequency: Mandatory. The internal on which data is published (e.g. daily, monthly, etc.)
    :param list[str] keywords: Optional. User-defined comma separated keywords that can be used to find this dataset through the search interface.
    :param str naming_convention: Optional. Key for how to read the dataset name.
    :param str documentation: Optional. Documentation about this dataset in markdown format.

    """
    def __init__(
        self,
        package_id,
        name,
        description,
        content_type,
        data_format,
        publishing_frequency,
        keywords=None,
        naming_convention=None,
        documentation=None
    ):
        self.payload = {
            "packageId": package_id,
            "name": name,
            "description": description,
            "keywords": keywords,
            "contentType": content_type,
            "location": None,
            "dataFormat": {"type": data_format},
            "publishingFrequency": publishing_frequency,
            "namingConvention": naming_convention,
            "documentation": documentation
        }

    def with_data_lake_storage(self, bucket_name):
        """
        Indicate that this package's datasets will be stored
        in a data-lake owned S3 bucket.

        :param bucket_name: A unique representative name for this bucket.
                            Data Lake buckets share a common prefix which will be
                            appended to this name if the creation is successful.
        :type bucket_name: str

        :rtype: dli.client.builders.DatasetBuilder

        - **Sample**

        .. code-block:: python

                from dli.client.builders import DatasetBuilder

                builder = DatasetBuilder(
                                package_id="package-id",
                                name="my test dataset",
                                description="My dataset description",
                                content_type="Pricing",
                                data_format="CSV",
                                publishing_frequency="Weekly"
                        )
                builder = builder.with_data_lake_storage("data-lake-bucket-name")
                dataset = dl.register_dataset(builder)
        """
        self.payload["location"] = {
            "type": "S3",
            "owner": "DataLake",
            "bucket": bucket_name
        }
        return self

    def with_external_s3_storage(
        self,
        bucket_name,
        aws_account_id
    ):
        """
        Indicate that this package's datasets will be stored
        in a self-managed S3 bucket outside of the Data Lake.

        :param bucket_name: Name of the bucket you want to link to this package
        :type bucket_name: str

        :param str aws_account_id: The AWS account id where this bucket currently resides.
                                   This account needs to be registed on the data lake previously
                                   and your account should have permissions to use it.

        :rtype: dli.client.builders.DatasetBuilder

        - **Sample**

        .. code-block:: python

                from dli.client.builders import DatasetBuilder

                builder = DatasetBuilder(
                                package_id="package-id",
                                name="my test dataset",
                                description="My dataset description",
                                content_type="Pricing",
                                data_format="CSV",
                                publishing_frequency="Weekly"
                        )
                builder = builder.with_external_s3_storage(
                    bucket_name="external-s3-bucket-name",
                    aws_account_id=123456789
                )
                package = dl.register_Dataset(builder)
        """
        self.payload["location"] = {
            "type": "S3",
            "owner": {
                "awsAccountId": str(aws_account_id)
            },
            "bucket": bucket_name
        }
        return self

    def with_external_storage(self, location):
        """
        Allows specifying a non S3 location where
        the package's datasets reside.

        The location will be kept for informational purposes only.

        :param location: a connection string or identifier
                         where this package resides.
        :type location: str

        :rtype: dli.client.builders.DatasetBuilder

        - **Sample**

        .. code-block:: python

                from dli.client.builders import DatasetBuilder

                builder = DatasetBuilder(
                                package_id="package-id",
                                name="my test dataset",
                                description="My dataset description",
                                content_type="Pricing",
                                data_format="CSV",
                                publishing_frequency="Weekly"
                        )
                builder = builder.with_external_storage("external-storage-location")
                package = dl.register_dataset(builder)
        """
        self.payload["location"] = {
            "type": "Other",
            "source": location
        }
        return self

    def build(self):
        if not self.payload["location"]:
            raise Exception(
                "No storage option was specified. Please use one of the following methods: "
                "`with_data_lake_storage`, `with_external_s3_storage`, `with_external_storage`"
            )

        # clean not set entries
        payload = {k: v for k, v in self.payload.items() if v is not None}
        return payload
