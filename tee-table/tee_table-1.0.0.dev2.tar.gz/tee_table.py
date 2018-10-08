#!python3

"""
Manage a table that keeps values in pandas and in a CSV file, and prints to the console too.
Particularly useful for keeping track of long experiment results.

AUTHOR: Erel Segal-Halevi
SINCE : 2018-08
"""

import pandas, os

class TeeTable:
    def __init__(self, columns:list, csvFileName:str):
        """

        :param columns: an ordered list of columns for this table.
        :param csvFileName: a path to a file that will be used to backup this table.
        If the file exists, it is read into the new table.
        If the file does not exist, an empty table is initialized and the file will be created when the table is "done".
        """
        self.columns = columns
        if os.path.isfile(csvFileName):
            print("reading from "+csvFileName)
            self.dataFrame = pandas.read_csv(csvFileName)
        else:
            self.dataFrame = pandas.DataFrame(columns=columns)
        print("{} rows loaded.".format(self.dataFrame.shape[0]))
        print(*columns, sep="\t")
        self.csvFileName = csvFileName
        self.csvFileNameTemp = csvFileName.replace(".csv",".temp.csv")

    def to_csv(self, filename):
        self.dataFrame.to_csv(filename, columns=self.columns, index=False)
        # index=False means to not save the automatically-added index column.
        # This is important - without it we might have problems later when adding new rows after load.

    def add(self, dataRow:dict):
        """
        Add a data-row whose values exactly match the columns in self.columns.
        """
        print(*dataRow.values(), sep="\t")
        index_of_new_row = self.dataFrame.shape[0]
        self.dataFrame.loc[index_of_new_row] = pandas.Series(dataRow) # Works only if there are no "holes" in the index (requires "index=False" in saving to csv).
        # self.dataFrame.iloc[index_of_new_row] = pandas.Series(dataRow) # IndexError: single positional indexer is out-of-bounds
        # self.dataFrame = self.dataFrame.append(pandas.Series(dataRow), ignore_index=True) # This is inefficient! It creates and returns a new dataFrame.
        self.to_csv(self.csvFileNameTemp)

    def rowCount(self, dataRow:dict)->int:
        """
        Counts the number of rows that match the given dict.

        :param dataRow a dict containing some fields (not necessarily all).
        :return The number of rows that contain these fields and values.
        """
        df = self.dataFrame
        for key in dataRow.keys():
            df = df[df[key]==dataRow[key]]
        return df.shape[0]

    def done(self):
        print("writing to " + self.csvFileName)
        self.to_csv(self.csvFileName)
        print("removing temporary CSV file " + self.csvFileNameTemp)
        os.remove(self.csvFileNameTemp)


# DEMO
if __name__ == "__main__":
    t = TeeTable(["name", "phone", "address"], "phonebook.csv")
    t.add({"name": "Alice", "phone": "1234", "address": "Haifa"})
    t.add({"name": "George", "phone": "5678", "address": "Bialik"})
    t.done()

