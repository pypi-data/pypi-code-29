from datetime import date # builtin module
import json
import sys

'''
This is a utility module with few useful functions

Author: Vinod <vinod@vinod.co>
Date: 3/10/2018
'''

# long factorial(int num) {
# }

def factorial(num):
    '''
    Returns the factorial of the input number. Factorial of a number less than or equals to 1 will be returned as 1
    '''
    if num<1:
        print('Input must be >= 1')
        
    f = 1
    while num > 1:
        f = f * num
        num = num - 1
    
    return f

def is_leap(year):
    # year % 4 ==0 && year % 100 !=0
    # year % 400 == 0

    # if year % 400 == 0 or (year % 4 ==0 and year % 100 !=0): return True
    # else: return False

    return year % 400 == 0 or (year % 4 ==0 and year % 100 !=0)

def max_days(month, year):
    if month == 2:
        # return 29 if is_leap(year) else 28
        if is_leap(year):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31

# custom function that makes use of a builtin function
def day_of_week(day, month, year): 
    dow = date(year, month, day).weekday() + 1
    return dow if dow<=6 else 0
    

def print_calendar(month = None, year = None):
    if month==None: month = date.today().month
    if year==None: year = date.today().year

    md = max_days(month, year)
    dow = day_of_week(1, month, year)

    print("Su Mo Tu We Th Fr Sa")
    print("--------------------")
    print("   "*dow, end='')
    # print "   " * dow,
    for d in range(1, md+1):
        print("{:2} ".format(d), end='')
        if (d+dow)%7==0: print()
        # print("%2d " % d, end='')
        # print "%2d " % d, 
    print()

# dunder functions are supposed to be private to the module
# and should be used by any code outside of this module
def __in_words__(num):
    '''this function receives a 2 digit number and returns 
    a string equivalent of the same'''

    lst1 = ',one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty'.split(',')

    lst2 = ',,twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety'.split(',')

    if num<=20: return lst1[num]
    else:
        n1 = num%10
        n2 = num//10
        return lst2[n2] + ' ' + lst1[n1]

def num2words(num = None):
    if type(num) != int: raise TypeError('Only int allowed')
    if num==None: num = int(input('Enter a number: '))
    if num>999999999: raise ValueError('Max value is 999999999')

    
def csv2json(filename, indent=4):
    '''This method accepts a readable CSV filename as input,
    and returns a string representing the data in JSON format
    '''

    if type(filename) != str: raise TypeError('filename must be a str')

    try:
        with open(filename, encoding='utf-8') as file:
            headers = file.readline().strip().split(',')
            lst = []
            for line in file: # process the second line onwards
                values = line.strip().split(',')
                data = dict(zip(headers, values))
                lst.append(data)
            return json.dumps(lst, indent=indent)
    except:
        raise ValueError('Invalid filename: ' + filename)

# this function overrides (re-writes) the above function 
# with the same name
def csv2json(filename, indent=4):
    '''This method accepts a readable CSV filename as input,
    and returns a string representing the data in JSON format
    '''

    if type(filename) != str: raise TypeError('filename must be a str')

    try:
        with open(filename, encoding='utf-8') as file:
            headers = file.readline().strip().split(',')
            
            lst = [
                dict(zip(headers,line.strip().split(','))) 
                for line in file]

            return json.dumps(lst, indent=indent)
    except:
        raise ValueError('Invalid filename: ' + filename)

if __name__=='__main__': 
    month = int(sys.argv[1]) if len(sys.argv)>1 else None
    year = int(sys.argv[2]) if len(sys.argv)>2 else None
    print_calendar(month, year)