#!/usr/bin/python
'''PARSES data in to list from table information
'''

import sys


def parser(info):
    '''Return the datasets to create CSV

    args: info is the input data from the website.

    return: these are teh data sets fro each profile
    
    '''
    headings = [th.get_text() for th in info.find("tr").find_all("th")]

    datasets = []
    datasets.append(headings)
    for row in info.find_all("tr")[1:]:
        dataset = []
        for td in row.find_all("td"):
           dataset.append(td.get_text())
        datasets.append(dataset)
    return datasets

def main():
    '''Main is just a placeholder
    '''
    pass


if __name__ == '__main__':
    main()
