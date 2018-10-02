
import json
from collections import OrderedDict
import os
import calendar
import ast
from datetime import datetime
from azure.storage.file import FileService
import zipfile
import logging
logger = logging.getLogger('autoscaler')


class cloud():
    def __init__(self):
        pass
        # CloudWatchEventName = "Every_60_Seconds"

    def setup_settings(self, args):
        print("We are setting %s" % args['<storage_name>'])
        self.settings = {}
        self.settings["cloud"] = "azure"
        self.settings["storage_name"] = args['<storage_name>']
        self.settings["storage_key"] = args['<storage_key>']
        self.settings["fileshare"] = args['<fileshare>']
        if args['<region>'] is None:
            self.region = os.getenv('AZURE_DEFAULT_REGION', "eastus")
        else:
            self.region = args['<region>']

        self.settings['region'] = self.region

    def init_settings(self, settings):
        self.settings = settings
        self.storagename = self.settings["storage_name"]
        self.storagekey = self.settings["storage_key"]
        self.fileshare = self.settings["fileshare"]
        self.azure_file_service = FileService(
            account_name=self.storagename, account_key=self.storagekey)
        logger.debug("Azure file service setup. Storage name: {}, Storage key: {}".format(self.storagename,
                                                                                          self.storagekey))

    def download_file(self, storage_name, filename, directory, filepath):
        try:
            fileshare = self.fileshare

            is_file = self.azure_file_service.exists(
                fileshare, directory_name="AutoScaler", file_name=filename)
            if is_file:
                self.azure_file_service.get_file_to_path(
                    fileshare,  # share name
                    directory,  # directory path
                    filename,  # source file name
                    filepath)
                return True
            else:
                logger.error("File don't exist. Fileshare : {}, dir: {}, filename: {}".format(fileshare,
                                                                                              directory,
                                                                                              filename))
                return False
        except Exception as e:
            logger.exception(e)
            return False

    def download_file_json(self, storage_name, filename):
        download_directory = "/tmp/"
        local_filepath = "/tmp/" + filename
        self.download_file(
            storage_name, filename, local_filepath)
        with open(download_directory + filename) as json_data:
            return json.load(json_data, object_pairs_hook=OrderedDict)

    def upload_file(self, directory, filename, fileshare=None):
        if fileshare is None:
            fileshare = self.fileshare
        source_file = '/tmp/' + filename
        try:
            directory = directory.rstrip("/")
            self.azure_file_service.create_directory(fileshare, directory)
            self.azure_file_service.create_file_from_path(
                fileshare,  # share name
                directory,  # directory path
                filename,  # destination file name
                source_file)  # source path with name
            return True
        except Exception as e:
            logger.exception("received error putting file. fileshare {}, directory {}, filename {}, error {}".format(
                fileshare, directory, filename, e))
            return False

    def upload_file_json(self, data, bucket_name, filename):
        directory = "AutoScaler/"
        download_directory = "/tmp/"
        with open(download_directory + filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)

        self.upload_file(download_directory + filename,
                          bucket_name, directory + filename)

    def collect_all_logs(self, logsDir=None):
        """

        :return: Collects all autoscaler logs in Transit Hub
        """
        try:
            directory = "AutoScaler/"
            if logsDir is None:
                logsDir = "AutoScaler/logs"
            result_generator = self.azure_file_service.list_directories_and_files(
                self.fileshare, logsDir
            )
            localDir = os.getcwd() + "autoscaler_logs"
            for logfile in result_generator:
                if type(logfile).__name__  == "File":
                    self.download_file(self.storagename, logfile, logsDir, localDir + logfile)
                else:
                    logger.debug("Not a file {}".format(logfile))
            self.download_file(self.storagename, "munger.log", directory, localDir + "munger.log")
            return True
        except Exception as e:
            logger.exception(e)
            return False

    def zipDir(self, dirPath, zipPath):
        zipf = zipfile.ZipFile(zipPath, mode='w')
        files = [f for f in os.listdir(dirPath) if os.path.isfile(f)]
        for file in files:
            zipf.write(file)
        zipf.close()

    def collect_all_logs_zip(self):
        """

        :return: Collects all logs in Transit hub and zips it
        up as autoscaler_logs.zip file in current working dir.
        """
        try:
            logsDir = os.getcwd() + "autoscaler_logs"
            self.collect_all_logs(logsDir)
            self.zipDir(logsDir, os.getcwd())
        except Exception as e:
            logger.exception(e)
