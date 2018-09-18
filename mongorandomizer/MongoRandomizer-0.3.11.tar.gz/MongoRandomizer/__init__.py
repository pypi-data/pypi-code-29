import pymongo
from pymongo import WriteConcern
from ConfigParser import SafeConfigParser
import argparse
import os
from multiprocessing import Process
from os.path import expanduser
import random
from datetime import datetime
import sys
import threading
from pprint import pprint
import time
from faker import Faker
import math

# Globals
_DBNAME = "demodb"
_COLNAME = "democollection"
_THREADS = 10
_MAXBLOCKS = 1000
_BLOCKSIZE = 1000
_PAD = 0
_WC = 0
_J = False
# NYC
_LATITUDE = 40.84
_LONGITUDE = -73.87
_RADIUSKM = 150
_G = False

def cli():
    try:
        global _DBNAME, _COLNAME, _THREADS, _MAXBLOCKS, _BLOCKSIZE, _PAD, _WC, _J, _G, _LATITUDE, _LONGITUDE, _RADIUSKM

        parser = argparse.ArgumentParser(description='CLI Tool for continually writing random data to a MongoDB database for testing purposes')
        # config string
        parser.add_argument('-c', action="store", dest="cs", help="server connection string")
        parser.add_argument('-t', action="store", dest="t", help="threads to use, if left off, use 10")
        parser.add_argument('-b', action="store", dest="b", help="blocksize to use. if not inclided, use 1000")
        parser.add_argument('-m', action="store", dest="m", help="max blocks to use. if not inclided, use 1000")
        parser.add_argument('-p', action="store", dest="p", help="additional chars of padding to increase document size")

        parser.add_argument('-w', action="store", dest="wc", help="write concern to use. if blank, none used")

        # functionality 
        parser.add_argument('task', metavar='task', help="clean, insert, insertAndUpdate, read, everything")

        # flags
        parser.add_argument("-j", "--journaling", help="if omitted, false. if flag enabled, journal", action="store_true")
        parser.add_argument("-g", "--geo", help="if omitted, use customer data. if flag enabled push geographic data", action="store_true")
        parser.add_argument('-o', action="store", dest="origin", help="if using the g flag, this is the origin point. use format lat,long,radiusinkm")

        arg = parser.parse_args()
        homedir = expanduser("~")

        if (arg.cs != None):
            cp = SafeConfigParser()
            cp.add_section("mdb")
            cp.set('mdb', 'cs', arg.cs)

            with open(homedir+"/.mdbrandomizer", 'wb') as configfile:
                cp.write(configfile)

        elif (os.path.isfile(homedir+"/.mdbrandomizer")):
            cp = SafeConfigParser()
            cp.read(homedir+"/.mdbrandomizer")
        else:
            print "\nMust provide credentials or have a credential file\n"
            parser.print_help()
            exit(4)

        if(arg.t != None):
            _THREADS = int(arg.t)

        if(arg.m != None):
            _MAXBLOCKS = int(arg.m)

        if(arg.b != None):
            _BLOCKSIZE = int(arg.b)
        
        if(arg.p != None):
            _PAD = int(arg.p)

        if(arg.wc != None):
            if(arg.wc == "majority"):
                _WC = "majority"
            else:
                _WC = int(arg.wc)

        if(arg.journaling):
            _J = True

        if(arg.geo):
            _COLNAME = "geo"
            _G = True
            if(arg.origin != None):
                origin = arg.origin.split(",")
                _LATITUDE = float(origin[0])
                _LONGITUDE = float(origin[1])
                _RADIUSKM = float(origin[2])

        if (arg.task.lower() == "clean"):
            clearDB(cp)
        elif (arg.task.lower() == "insert"):
            insertDB(cp)
        elif (arg.task.lower() == "insertandupdate"):
            updateDB(cp)
        elif (arg.task.lower() == "everything"):
            everythingDB(cp)
        elif (arg.task.lower() == "read"):
            readDB(cp)
        else:
            print "\nDidn't understand any task\n"
            parser.print_help()
            exit(5)

    except KeyboardInterrupt:
        print "\n\nCompleted!\n\n"
        exit(0)

def clearDB(cp):
    global _DBNAME, _COLNAME
    try:
        conn = pymongo.MongoClient(cp.get('mdb','cs'))
        conn.drop_database(_DBNAME)
        print "DB Dropped!"
    except:
        print "Could not clear the DB!"
        print sys.exc_info()[0]
        exit(6)

def insertDB(cp):
    global _DBNAME, _COLNAME, _THREADS, _MAXBLOCKS, _BLOCKSIZE, _PAD, _WC, _J, _G

    f = Faker()

    print "\n\n================================================="
    print "About to enter data in: "
    print "\tThreads: " + str(_THREADS)
    print "\tDB: " + _DBNAME
    print "\tCollection: " + _COLNAME
    print "\tBlocksize: " + str(_BLOCKSIZE)
    print "\tMax Blocks: " + str(_MAXBLOCKS)
    print "\tWrite Concern: " + str(_WC)
    print "\tJournaling: " + str(_J)
    print "\tGeo Data?: " + str(_G)
    print "=================================================\n\n"
    print "This process will continue until you press control+c or break \n\n"

    for index in range(0, _THREADS):
        p = Process(target=r_insertRecord, args=(f, cp.get('mdb','cs'), _DBNAME, _COLNAME, _WC, _J, _MAXBLOCKS, _BLOCKSIZE, _PAD, _G))
        p.start()
        p.join()

def everythingDB(cp):
    global _DBNAME, _COLNAME, _THREADS

    # start inserting
    t = threading.Thread(target=insertDB, args=(cp,))
    t.start()

    time.sleep(5)

    readDB(cp)

def readDB(cp):
    global _DBNAME, _COLNAME, _THREADS
    conn = pymongo.MongoClient(cp.get('mdb','cs'))

    print "\n\n================================================="
    print "About to read data in: "
    print "\tThreads: " + str(_THREADS)
    print "\tDB: " + _DBNAME
    print "\tCollection: " + _COLNAME
    print "=================================================\n\n"
    print "This process will continue until you press control+c or break \n\n"

    for index in range(0, _THREADS):
        p = Process(target=r_readRecords, args=(conn[_DBNAME][_COLNAME],))
        p.start()
        p.join()
    
def r_readRecords(handle):
    for iteration in xrange(10):
        docs = handle.find()
        for doc in docs:
            temp = doc['accountNumber']
    r_readRecords(handle)

# RECURSIVE FUNCTION!
def r_insertRecord(f, connStr, dbname, colname, wc, journaling, mb, bs, padding, g):
    global _LATITUDE, _LONGITUDE, _RADIUSKM
    conn = pymongo.MongoClient(connStr, w=wc, j=journaling)
    handle = conn[dbname][colname]

    states = ("AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY")
    loc = ("Rd.", "Dr.", "Ave", "Lane", "St.")

    for i in xrange(mb):
        docs = []
        for j in xrange(bs):
            if(g):
                radDeg = _RADIUSKM * (1 / 110.54)
                lat = _LATITUDE + random.uniform(0, radDeg)
                lon = _LONGITUDE + random.uniform(0, radDeg)
                #print str(lat) + "," + str(lon)
                docs.append({
                    "padding": "a"*padding,
                    "notes": f.text(),
                    "name": f.name(),
                    "location": {"type": "Point", "coordinates": [lon, lat]}
                })
                lat = _LATITUDE - random.uniform(0, radDeg)
                lon = _LONGITUDE + random.uniform(0, radDeg)
                #print str(lat) + "," + str(lon)
                docs.append({
                    "padding": "a"*padding,
                    "notes": f.text(),
                    "name": f.name(),
                    "location": {"type": "Point", "coordinates": [lon, lat]}
                })
                lat = _LATITUDE + random.uniform(0, radDeg)
                lon = _LONGITUDE - random.uniform(0, radDeg)
                #print str(lat) + "," + str(lon)
                docs.append({
                    "padding": "a"*padding,
                    "notes": f.text(),
                    "name": f.name(),
                    "location": {"type": "Point", "coordinates": [lon, lat]}
                })
                lat = _LATITUDE - random.uniform(0, radDeg)
                lon = _LONGITUDE - random.uniform(0, radDeg)
                #print str(lat) + "," + str(lon)
                docs.append({
                    "padding": "a"*padding,
                    "notes": f.text(),
                    "name": f.name(),
                    "location": {"type": "Point", "coordinates": [lon, lat]}
                })
            else:
                presc = []
                for p in range(random.randint(1,25)):
                    presc.append(f.text(random.randint(10,30)))
                docs.append(
                    {
                        "accountNumber": random.randint(1,1000),
                        "fullname": f.name(),
                        "occupation": f.job(),
                        "address": str(random.randint(1,999))+ " " + f.last_name() + " " + random.choice(loc),
                        "state": random.choice(states),
                        "zipcode": str(random.randint(10000,99999)),
                        "singupDate": datetime.utcnow(),
                        "payment": random.randrange(50,200,5),
                        "copay": random.randrange(20,60,10),
                        "deductible": random.randrange(100,500,100),
                        "notes": f.text(),
                        "prescriptions":presc,
                        "padding": "a"*padding
                        }
                    )
        handle.insert_many(docs)
    r_insertRecord(f, connStr, dbname, colname, wc, journaling, mb, bs, padding, g)