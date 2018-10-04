#!/usr/bin/python
'''This file takes in date and outputs it to csv file in the directory

'''

import csv

def fileMaker(out, name):
    '''Take inforamtion and make csv file in directory

    args: out the list of data, and name the name of the file to be made
    '''
    with open(name, 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(out)
    myfile.close()

def main():
    pass

if __name__ == '__main__':
    main()
