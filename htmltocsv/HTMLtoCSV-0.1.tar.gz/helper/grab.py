#!/usr/bin/python
''' This program takes in a url and outputs information of the table on the website to be used for documentation.

'''

import urllib
from bs4 import BeautifulSoup


def getIt(url):
    '''This method grabs a webpage and converts it into usable information.
    
    args: url, a website url converted to string.
    
    return: returns a list of the website table to be used

    Raises: No exceptions
    '''
    webpage = urllib.urlopen(url)
    soup = BeautifulSoup(webpage, 'html.parser')
    table = soup.find("table", attrs={"id":"profiles"})
    return table

def main():
    '''This main is a place holder
    
    '''
    pass

if __name__ == '__main__':
	main()
  
