from google.cloud import storage
import os


class StorageBucket(object):
    """
	StorageBucket establishes, holds & represents connections to Google Storage buckets and provides
	methods for commonly-used interactions with the contents of the bucket.
	"""

    def __init__(self, bucket_name, credentials=None):
        if credentials:
            GOOGLE_APPLICATION_CREDENTIALS=credentials
        self.bucket = self.__connect_to_storage_bucket(bucket_name)

    def __connect_to_storage_bucket(self, bucket):
        """
		Returns a Client connection to the requested Google Cloud Storage bucket
		:param bucket: str - The name of the Storage bucket that you wish to connect to
		:return: Client instance with connection to the requested bucket
		"""
        client = storage.Client()
        return client.get_bucket(bucket)

    def get_blob(self, blob_path, raise_ex=True):
        if self.blob_exists(blob_path):
            return self.bucket.get_blob(blob_path)
        elif raise_ex:
            raise FileNotFoundError(
                "No blob was found in bucket {bucket} with name {blob}".format(bucket=self.bucket.name, blob=blob_path)
            )
        else:
            return False

    def blob_exists(self, blob_path):
        return True if self.bucket.get_blob(blob_path) else False

    def rename_blob(self, current_path, new_path):
        blob = self.get_blob(current_path)
        return self.bucket.rename_blob(blob, new_path)

    def delete_blob(self, blob_path):
        blob = self.get_blob(blob_path, raise_ex=False)
        if blob: blob.delete()

    def list_blobs(self, prefix_path=None):
        """
		Returns an iterator over all 'blobs' in the requested bucket (constrained by prefix_path if included)
		:param prefix_path: Prefix to include on bucket path before listing contents
		:return: blob objects iterator
		"""
        return list(self.bucket.list_blobs(prefix=prefix_path)) if prefix_path else list(self.bucket.list_blobs())

    def download_from_storage(self, blob_path, dst_file_path):
        """
		Download the object on blob_path from the specified storage bucket to the local file path at dst_file_path
		:param blob_path:
		:param dst_file_path:
		:return: None
		"""
        blob = storage.Blob(blob_path, self.bucket)
        if not os.path.exists(os.path.dirname(dst_file_path)):
            os.makedirs(os.path.dirname(dst_file_path))
        with open(dst_file_path, 'wb') as file_obj:
            blob.download_to_file(file_obj)

    def upload_to_storage(self, src_path, dst_path, overwrite=False):
        """
		Uploads a file from the local filesystem (path given by src_path) to a Google Storage Bucket (path given by
		dst_path). If the upload fails, the blob will be deleted.
		:param src_path: str Path on local filesystem to the file to be uploaded
		:param dst_path: str Destination path where storage blob will be saved
		:return: Bool status indicating whether the upload was completed successfully, None if a file already exists
		at the remote path and overwrite=False
		"""
        if os.path.exists(src_path):
            if not self.blob_exists(dst_path) or overwrite == True:
                try:
                    blob = self.bucket.blob(dst_path)
                    blob.upload_from_filename(src_path)
                    return True
                except:
                    self.delete_blob(dst_path)
                    return False
            else:
                return None
        else:
            raise FileNotFoundError("File {} could not be found".format(src_path))
