#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# Ola Search Communication
# Phone number
# URL
# email
import re

# Predefined strings.
phone_number = "(\+?[0-9\(][0-9\- \(\)\.]{6,16}( ?e?xt?\.? ?\d+)?)"
phone_number_regex = re.compile(phone_number, re.IGNORECASE)

email = "([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
email_regex = re.compile(email, re.IGNORECASE)

url = "((https?://|ftp://|www\.|[^\s:=]+@www\.).*?[a-z_\/0-9\-\#=&])(?=(\.|,|;|\?|\!)?(\"|'|«|»|\[|\s|\r|\n|$))"
url_regex = re.compile(url, re.IGNORECASE)

def tag_phone(text):
    timex_found = []
    found = phone_number_regex.findall(text)
    found = [a[0] for a in found if len(a) > 1]
    for timex in found:
        timex_found.append(timex)

    # Tag only temporal expressions which haven't been tagged.
    for timex in timex_found:
        timex = re.escape(timex)
        text = re.sub(timex + '(?!</PHONE>)', '<PHONE>' + timex.decode('string-escape') + '</PHONE>', text)

    return text

def tag_email(text):
    timex_found = []
    found = email_regex.findall(text)
    for timex in found:
        timex_found.append(timex)
    for timex in timex_found:
        text = re.sub(timex + '(?!</EMAIL>)', '<EMAIL>' + timex + '</EMAIL>', text)

    return text

def tag_url(text):
    timex_found = []
    found = url_regex.findall(text)
    found = [a[0] for a in found if len(a) > 1]
    for timex in found:
        timex_found.append(timex)
    for timex in timex_found:
        text = re.sub(timex + '(?!</URL>)', '<URL>' + timex + '</URL>', text)

    return text
