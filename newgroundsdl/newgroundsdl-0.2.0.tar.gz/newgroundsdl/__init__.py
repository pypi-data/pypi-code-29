#!/usr/bin/env python3

import urllib.request
import shutil
from bs4 import BeautifulSoup
import re
import json

name = "newgroundsdl"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"}
xmlhttpheaders = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0", "X-Requested-With": "XMLHttpRequest"}

def getSongPages(userPageURI):
    req = urllib.request.Request(userPageURI, data=None, headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read()

    soup = BeautifulSoup(html, "html.parser")

    songuris = []
    if soup.body["class"] == ["skin-userpage"]:
        # user page, stuff is hidden in scripts
        base_uri = re.sub(r'/audio.*$', '', userPageURI)
        next_page = "/audio/page/1"
        while next_page:
            req1_5 = urllib.request.Request(base_uri + next_page, data=None, headers=xmlhttpheaders)
            with urllib.request.urlopen(req1_5) as response1_5:
                jsondata = response1_5.read().decode("utf-8")
                metadata = json.loads(jsondata)
            
            for year in metadata["sequence"]:
                for song in metadata["years"][str(year)]["items"]:
                    songuris.append("https:" + re.search(r'<a href="([^"]*)"', song).group(1))
            
            next_page = metadata["more"]

    else:
        wrappers = soup("div", class_="audio-wrapper")
        for w in wrappers:
            songuris.append("https:" + w.a['href'])
    return songuris

def getSongFileURI(songPageURI):
    fileuri = ""
    req2 = urllib.request.Request(songPageURI, data=None, headers=headers)
    with urllib.request.urlopen(req2) as response2:
        soup2 = BeautifulSoup(response2.read(), "html.parser")
        pod = soup2("div", class_="pod")[0] # pod #1 is the audio info
        metadata = str(pod("script")[-2].string) # currently the 8th script in the pod contains the metadata
        fileuri = re.search(r'"url":"([^\?]*)', metadata).group(1) # I could parse json here but I don't feel like it
        # note that it strips off the parameter. I'm not really sure what it's for, but it's definitely not necessary.
        fileuri = re.sub(r'\\(.)', r'\1', fileuri) # unescape the json string
    return fileuri
