import boto3


class s3_local_endpoint(object):
    """
    Client to access to the S3 gateway.
    """

    def __init__(self, access_key, secret_key, url, bucket):
        """
        Connect a client to the S3 gateway.

        :param access_key: The identifier used for the connection.
        :type access_key: str
        :param secret_key: The password used for the connection.
        :type secret_key: str
        :param url: The S3 gateway URL.
        :type url: str
        :param bucket: The S3 bucket.
        :type bucket: str

        :returns: s3 -- The current object
        """
        # Connexion to s3
        self.__client = boto3.client(
            's3',
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            endpoint_url=url
        )
        self.set_bucket(bucket)

    def set_bucket(self, bucket):
        """
        Sets the bucket name for this instance and create it if necessary.

        :param bucket: The bucket name
        :type bucket: str

        :returns: bool -- True on success. False if the bucket creation failed.
        """
        res = True
        self.__bucket = bucket
        buckets = self.list_buckets()

        # Create the bucket if it does not exist.
        if self.__bucket not in buckets:
            res = self.create_bucket(bucket)

        return res

    def create_bucket(self, bucket):
        """
        Create a S3 bucket

        :param bucket: The bucket to create
        :type bucket: str

        :returns: bool -- True if the bucket is sucessfully created.
                False otherwise.
        """
        res = self.__client.create_bucket(Bucket=bucket)
        return (res['ResponseMetadata']['HTTPStatusCode'] == 200)

    def delete_bucket(self, bucket):
        """
        Delete a S3 bucket

        :param bucket: The bucket to delete
        :type bucket: str

        :returns: bool -- True if the bucket is sucessfully deleted. False
            otherwise.
        """
        res = False
        if(self.delete_all_files()):
            res_json = self.__client.delete_bucket(Bucket=bucket)
            res = (res_json['ResponseMetadata']['HTTPStatusCode'] == 204)
        return res

    def list_buckets(self):
        """
        Call S3 to list current buckets

        :returns: array -- the bucket list for the current account. An empty
            list if there is no bucket for this account.
        """
        response = self.__client.list_buckets()
        return [bucket['Name'] for bucket in response['Buckets']]

    def list_files(self):
        """
        Call S3 to list files in the bucket

        :returns: array -- the file list for the current bucket. An empty
            list if there is no file for this bucket.
        """
        return [key['Key']
                for key
                in self.__client.list_objects(Bucket=self.__bucket).get(
                    'Contents', [])]

    def upload_file(self, src_file):
        """
        Upload file in a bucket

        :param src_file: The file to upload
        :type src_file: str

        :returns: bool -- True if the file is successfuly uploaded. False
            otherwise.
        """
        res = False
        with open(src_file, 'rb') as fh:
            res = self.upload_stream(fh.name, fh)
        return res

    def upload_stream(self, file_path, stream):
        """
        Upload a stream and save it to the corresponding file in a bucket

        :param file_path: The file_path to save the data to
        :type file_path: str
        :param stream: The data to upload
        :type stream: fileobject

        :returns: bool -- True if the file is successfuly uploaded. False
            otherwise.
        """
        self.__client.upload_fileobj(stream, self.__bucket, file_path)
        return True

    def generate_url(self, s3_file):
        """
        Generate a temporary url to the file

        :param s3_file: The s3 file to get the url from
        :type s3_file: str

        :returns: str -- The generated url to access the file.
        """
        url = None
        clientMethod = 'get_object'
        params = {
                'Bucket': self.__bucket,
                'Key': s3_file,
        }
        if(s3_file.endswith(".jpg")
                or s3_file.endswith(".jpeg")):
            params['ResponseContentType'] = "image/jpeg"
        # ExpiresIn (int) -- The number of seconds the presigned url is valid
        #       for.  (default : 3600 seconds)
        expiresIn = 10000
        url = self.__client.generate_presigned_url(
                clientMethod,
                params,
                expiresIn)
        return url

    def delete_file(self, src_file):
        """
        Delete a specific file

        :param src_file: The file to delete
        :type src_file: str

        :returns: bool -- True if the file is successfully deleted. False
            otherwise.
        """
        res = self.__client.delete_object(
                Bucket=self.__bucket,
                Key=src_file)
        return (res['ResponseMetadata']['HTTPStatusCode'] == 204)

    def delete_all_files(self):
        """
        Delete all files from the current bucket

        :returns: bool -- True if the files are successfully deleted. False
            otherwise.
        """
        res = True
        for filename in self.list_files():
            res = (res and self.delete_file(filename))
        return res
