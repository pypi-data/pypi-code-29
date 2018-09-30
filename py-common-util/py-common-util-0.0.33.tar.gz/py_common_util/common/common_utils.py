# -*- coding:utf-8 -*-
import csv


class CommonUtils:

    @staticmethod
    def write_csv(file_name, mode='w', write_fn=None):
        """
        write record to csv file
        :param file:
        :param mode: 'r','w'
        :param csvwrite_fn:
        :return:
        """
        with open(file_name, mode) as stream:
            csvwriter = csv.writer(stream)
            write_fn(csvwriter)

    @staticmethod
    def write_h5(file_name, mode='w', db_name='', shape=(1,), dtype='f', data=None):
        import h5py
        h5_file = h5py.File(file_name, mode)
        h5_dataset = h5_file.create_dataset(db_name, shape, data)
        return h5_file
