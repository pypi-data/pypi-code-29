#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 13:04:32 2018

@author: andrew
"""

import os
import glob
import align

def src_filter(location):
    source_loc = location + '/sources'
    source_files = glob.glob(source_loc + '/*.txt')
    for file in source_files:
        with open(file, 'r') as fl:
            data = fl.readlines()
            fl.close()
        data = [str(file[len(source_loc)+1:-4]) + '\n'] + data
        data.append("\n\n\n")
        with open(source_loc + '/sources.txt', 'a+') as s:
            s.writelines(data)
            s.close()
        os.remove(file)
        
    #filter source file by spread_model
    del_lin = []
    source = glob.glob(source_loc + '/*.txt')
    with open(source[0], 'r') as src:
        lines = src.readlines()
        src.close()
        
    for lin in lines:
        parse = lin.split()
        if parse != []:
            try:
                int(parse[0])
                if float(parse[-1]) < 0 or float(parse[-1]) > 0.1:
                    del_lin.append(lin)
            except ValueError or IndexError:
                pass
            
    lines = [a for a in lines if a not in del_lin]
    
    with open(source[0], 'w+') as src:
        src.writelines(lines)
        src.close()
    
    for l in lines:
        print(l)

#%%
#runs SExtractor on all residual images in a directory
def sextractor(location):
    x = 0
    sources = location + "/sources"
    residuals = location + "/residuals"
    check = os.path.exists(sources)
    length = len(residuals) + 1
    if check == False:
        os.system("mkdir %s" % (sources))
    images = glob.glob(residuals + "/*.fits")
    config_loc = os.path.dirname(align.__file__) + '/config/default.sex'
    with open(config_loc, 'r') as config:
        data = config.readlines()
        config.close()
    data[9] = "PARAMETERS_NAME" + "        " + os.path.dirname(align.__file__) + "/config/default.param" + "\n"
    data[20] = "FILTER_NAME" + "        " + os.path.dirname(align.__file__) + "/config/default.conv" + "\n"
    with open(config_loc, 'w') as config:
        config.writelines(data)
        config.close()
    print("\n-> SExtracting images...")
    for i in images:
        name = i[length:-5]
        with open(config_loc, 'r') as config:
            data = config.readlines()
            config.close()
        data[104] = "PSF_NAME" + "        " + location + "/psf/" + name[:-9] + ".psf" + "\n"
        with open(config_loc, 'w') as config:
            config.writelines(data)
            config.close()
        os.system("sextractor %s> %s/%s.txt -c %s" % (i, sources, name, config_loc))
        x += 1
        per = float(x)/float(len(images)) * 100
        print("-> %.1f%% sextracted..." % (per))
    print("-> SExtracted %d images, catalogues placed in 'sources' directory\n" % (len(images)))
    print("-> Filtering source catalogs...\n")
    src_filter(location)

def sextractor_test(location):
    x = 0
    sources = location + "/sources"
    residuals = location + "/residuals"
    check = os.path.exists(sources)
    length = len(residuals) + 1
    if check == False:
        os.system("mkdir %s" % (sources))
    images = glob.glob(residuals + "/*.fits")
    config_loc = os.path.dirname(align.__file__) + '/test_config/default.sex'
    with open(config_loc, 'r') as config:
        data = config.readlines()
        config.close()
    data[9] = "PARAMETERS_NAME" + "        " + os.path.dirname(align.__file__) + "/test_config/default.param" + "\n"
    data[20] = "FILTER_NAME" + "        " + os.path.dirname(align.__file__) + "/test_config/default.conv" + "\n"
    with open(config_loc, 'w') as config:
        config.writelines(data)
        config.close()
    print("\n-> SExtracting images...")
    for i in images:
        name = i[length:-5]
        with open(config_loc, 'r') as config:
            data = config.readlines()
            config.close()
        data[104] = "PSF_NAME" + "        " + location + "/psf/" + name[:-9] + ".psf" + "\n"
        with open(config_loc, 'w') as config:
            config.writelines(data)
            config.close()
        os.system("sextractor %s> %s/%s.txt -c %s" % (i, sources, name, config_loc))
        x += 1
        per = float(x)/float(len(images)) * 100
        print("-> %.1f%% sextracted..." % (per))
    print("-> SExtracted %d images, catalogues placed in 'sources' directory\n" % (len(images)))
    print("-> Filtering source catalogs...\n")
    src_filter(location)
    
def sextractor_psf(location):
    x = 0
    psf_loc = location + "/psf"
    data = location + "/data"
    check = os.path.exists(psf_loc)
    length = len(data) + 1
    if check == False:
        os.system("mkdir %s" % (psf_loc))
    images = glob.glob(data + "/*.fits")
    config_loc = os.path.dirname(align.__file__) + '/config/psf.sex'
    with open(config_loc, 'r') as config:
        data = config.readlines()
        config.close()
    data[9] = "PARAMETERS_NAME" + "        " + os.path.dirname(align.__file__) + "/config/default.psfex" + "\n"
    data[20] = "FILTER_NAME" + "        " + os.path.dirname(align.__file__) + "/config/default.conv" + "\n"
    with open(config_loc, 'w') as config:
        config.writelines(data)
        config.close()
    print("\n-> SExtracting images...")
    for i in images:
        name = i[length:-5]
        with open(config_loc, 'r') as config:
            data = config.readlines()
            config.close()
        data[6] = "CATALOG_NAME" + "        " + psf_loc + "/" + name + ".cat" + "\n"
        with open(config_loc, 'w') as config:
            config.writelines(data)
            config.close()
        os.system("sextractor %s -c %s" % (i, config_loc))
        x += 1
        per = float(x)/float(len(images)) * 100
        print("-> %.1f%% sextracted..." % (per))
    print("-> SExtracted %d images, catalogues placed in 'psf' directory\n" % (len(images)))

def sextractor_test_psf(location):
    x = 0
    psf_loc = location + "/psf"
    data = location + "/data"
    check = os.path.exists(psf_loc)
    length = len(data) + 1
    if check == False:
        os.system("mkdir %s" % (psf_loc))
    images = glob.glob(data + "/*.fits")
    config_loc = os.path.dirname(align.__file__) + '/test_config/psf.sex'
    with open(config_loc, 'r') as config:
        data = config.readlines()
        config.close()
    data[9] = "PARAMETERS_NAME" + "        " + os.path.dirname(align.__file__) + "/test_config/default.psfex" + "\n"
    data[20] = "FILTER_NAME" + "        " + os.path.dirname(align.__file__) + "/test_config/default.conv" + "\n"
    with open(config_loc, 'w') as config:
        config.writelines(data)
        config.close()
    print("\n-> SExtracting images...")
    for i in images:
        name = i[length:-5]
        with open(config_loc, 'r') as config:
            data = config.readlines()
            config.close()
        data[6] = "CATALOG_NAME" + "        " + psf_loc + "/" + name + ".cat" + "\n"
        with open(config_loc, 'w') as config:
            config.writelines(data)
            config.close()
        os.system("sextractor %s -c %s" % (i, config_loc))
        x += 1
        per = float(x)/float(len(images)) * 100
        print("-> %.1f%% sextracted..." % (per))
    print("-> SExtracted %d images, catalogues placed in 'psf' directory\n" % (len(images)))
    
