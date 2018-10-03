import logging
from concurrent.futures import ThreadPoolExecutor
import os

from .google_storage import StorageBucket

logger = logging.getLogger(__name__)


class BlobDownloader(object):

	def __init__(self, src_root, dst_root, storage_bucket=None, storage_prefix=None):
		"""
		Downloads Blobs from a Google Storage Bucket.
		:param storage_bucket: Default = None. StorageBucket instance can be passed in, otherwise a new connection
		will be created automatically
		:param storage_prefix: Provide a subpath in the storage bucket to constrain the blobs that are downloaded
		"""
		self.src_root = src_root
		self.dst_root = dst_root
		self.bucket = self.__get_storage_bucket(storage_bucket)
		self.prefix = storage_prefix
		self.blobs = self.__list_blobs()

	def __get_storage_bucket(self, storage_bucket):
		"""
		Returns an existing StorageBucket instance if provided, otherwise instatiates a new one
		:param storage_bucket:
		:return: StorageBucket instance
		"""
		return StorageBucket() if not storage_bucket else storage_bucket

	def __list_blobs(self):
		"""
		Generates a list of all the blob paths in the connected bucket. Constrained by the sub_folder if provided
		:return: List of blob paths
		"""
		return self.bucket.list_blobs(self.prefix)

	def download_blobs(self):
		"""
		Downloads all files from the remote storage bucket to the local filesystem
		:param src_root: Sets the root in the remote path to match against the dst_root
		:param dst_root: Sets the base directory in which files are saved
		:return: None

		eg. src_root = "data", dst_root = "home/user/data"
		blob name: "bucket/data/raw/uuid.jpg"       saved to: "home/user/data/raw/uuid.jpg"
		blob name: "bucket/data/raw/other/uuid.jpg" saved to: "home/user/data/raw/other/uuid.jpg"
		blob name: "bucket/data/uuid.jpg"           saved to: "home/user/data/uuid.jpg"

		Use of ThreadPoolExecutor with 8 workers (max) reduced d/l time from 57s to 8s :-)
		"""
		with ThreadPoolExecutor(max_workers=8) as pool:
			for idx, blob in enumerate(self.blobs):
				pool.submit(self.download_blob, blob)

	def download_blob(self, blob):
		try:
			if blob.size > 0:
				blob_path = blob.name
				blob_path_components = blob_path.split("/")
				src_root_idx = blob_path_components.index(self.src_root)
				path_addendum = "/".join(blob_path_components[src_root_idx + 1:])
				dst_file_path = "/".join([self.dst_root, path_addendum])
				if not os.path.exists(dst_file_path):
					self.bucket.download_from_storage(blob_path, dst_file_path)
		except:
			logger.info("Failed to download {}".format(blob.name))
