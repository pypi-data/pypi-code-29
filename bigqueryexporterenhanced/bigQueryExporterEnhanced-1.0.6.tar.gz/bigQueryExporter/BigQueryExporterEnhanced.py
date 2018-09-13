import random
from bigQueryExporter.BigQueryExporter import BigQueryExporter
import os
import logging
import shutil


class BigQueryExporterEnhanced(BigQueryExporter):

    def __init__(self, project_name, dataset_name, bucket_name=None, log_lambda=None, key_file_path=None):
        super().__init__(project_name, dataset_name, bucket_name, log_lambda=log_lambda, key_file_path=key_file_path)

    # Enhancement of the query_to_local function
    def query_to_local(self, query, job_name="", data_dir_path="export", keep_temp_table=False, overwrite_output_folder=True):

        temp_job_name = job_name + '%030x' % random.randrange(16**30)

        if self.bucket_name is None:
            temp_bucket_name = "temp_bucket" + temp_job_name[-6:]
            self.bucket_name = temp_bucket_name

            need_to_remove_bucket = True
        else:
            need_to_remove_bucket = False

        super().query_to_local(query, temp_job_name, data_dir_path)
        logging.info('Queried on BQ and stored in temp table %s' % temp_job_name)
        logging.info('Files saved in folder %s' % (data_dir_path + '/' + temp_job_name))

        bucket = self.storage_client.get_bucket(self.bucket_name)

        if not keep_temp_table:
            # Remove the table
            try:
                destination_table = self.bigquery_client.dataset(self.dataset_name).table(temp_job_name)
                self.bigquery_client.delete_table(destination_table)
                logging.info('Temp table %s removed' % temp_job_name)
            except BaseException:
                pass

            # Remove the exported files in the bucket
            blobs = list(bucket.list_blobs(prefix=job_name))
            for blob in blobs:
                blob.delete()

            # Remove the bucket
            if need_to_remove_bucket:
                bucket.delete()

        if overwrite_output_folder:
            if os.path.exists(os.path.join(data_dir_path, job_name)):
                shutil.rmtree(os.path.join(data_dir_path, job_name))

        try:
            # Rename the output folder
            os.rename(os.path.join(data_dir_path, temp_job_name),
                      os.path.join(data_dir_path, job_name))
            out_folder = os.path.join(data_dir_path, job_name)
        except:
            out_folder = os.path.join(data_dir_path, temp_job_name)

        return out_folder
