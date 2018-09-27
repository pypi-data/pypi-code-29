import boto3


class s3(object):
    def __init__(self, access_key, secret_key, url, bucket):
        """
        " Connect a client to the S3 gateway.
        "
        " :attr access_key The identifier used for the connection.
        " :attr secret_key The password used for the connection.
        " :attr url The S3 gateway URL.
        " :attr bucket The S3 bucket.
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
        " Sets the bucket name for this instance and create it if necessary.
        "
        " :attr bucket The bucket name
        "
        " :return True on success. False if the bucket creation failed.
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
        " Create a S3 bucket
        "
        " :attr bucket The bucket to create
        "
        " :return True if the bucket is sucessfully created. False otherwise.
        """
        res = self.__client.create_bucket(Bucket=bucket)
        return (res['ResponseMetadata']['HTTPStatusCode'] == 200)

    def delete_bucket(self, bucket):
        """
        " Delete a S3 bucket
        "
        " :attr bucket The bucket to delete
        "
        " :return True if the bucket is sucessfully deleted. False otherwise.
        """
        res = False
        if(self.delete_all_files()):
            res_json = self.__client.delete_bucket(Bucket=bucket)
            res = (res_json['ResponseMetadata']['HTTPStatusCode'] == 204)
        return res

    def list_buckets(self):
        """
        " Call S3 to list current buckets
        """
        response = self.__client.list_buckets()
        return [bucket['Name'] for bucket in response['Buckets']]

    def list_files(self):
        """
        " Call S3 to list files in the bucket
        """
        return [key['Key']
                for key
                in self.__client.list_objects(Bucket=self.__bucket).get(
                    'Contents', [])]

    def upload_file(self, src_file):
        """
        " Upload file in a bucket
        "
        " :attr src_file The file to upload
        """
        res = False
        with open(src_file) as fh:
            file_path = fh.name
            res = self.__client.upload_file(file_path, self.__bucket, src_file)
            res = True
        return res

    def generate_url(self, s3_file):
        """
        " Generate a temporary url to the file
        "
        " :attr s3_file The s3 file to get the url from
        "
        " :return The generated url to access the file.
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
        " Delete a specific file
        "
        " :attr src_file The file to delete
        "
        " :return True if the file is successfully deleted. False otherwise.
        """
        res = self.__client.delete_object(
                Bucket=self.__bucket,
                Key=src_file)
        return (res['ResponseMetadata']['HTTPStatusCode'] == 204)

    def delete_all_files(self):
        """
        " Delete all files from the current bucket
        "
        " :return True if the files are successfully deleted. False otherwise.
        """
        res = True
        for filename in self.list_files():
            res = (res and self.delete_file(filename))
        return res
