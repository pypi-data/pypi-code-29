#!/usr/bin/env python
# encoding: utf-8

import tweepy  # https://github.com/tweepy/tweepy
import json
import urllib
import os

def twitter_OAuth_login(config_file):
    secret_dict = {'consumer_key': '',
                   'consumer_secret': '',
                   'access_key': '',
                   'access_secret': ''}
    # try open config file
    try:
        file = open(config_file, 'r')
    except:
        print("open config file fail!")
        return None
    # record key & secret mentioned above
    for line in file:
        if line[-1] == '\n':
            line = line[:-1]
        elements = line.split('=')
        if elements[0] in secret_dict.keys():
            secret_dict[elements[0]] = elements[1]
    file.close()
    # try access to twitter by OAuth
    try:
        auth = tweepy.OAuthHandler(secret_dict['consumer_key'], secret_dict['consumer_secret'])
        auth.set_access_token(secret_dict['access_key'], secret_dict['access_secret'])
        api = tweepy.API(auth)
    except tweepy.TweepError:
        print("fail to access to twitter by OAuth")
        print(secret_dict)
        return None

    return api

def download_tweets(auth_api, screen_name, tweets_count=200, save_path=None):
    if not isinstance(screen_name, str):
        raise ValueError("invalid screen name, you should pass a str")
    if auth_api is None:
        raise ValueError("invalid auth_api. please use twitter_OAuth_login() first to get auth_api")

    alltweets = []
    alltweets_json = []

    if tweets_count <= 200:
        try:
            new_tweets = auth_api.user_timeline(screen_name=screen_name, count=tweets_count, tweet_mode='extended')
            print(len(new_tweets))
            alltweets.extend(new_tweets)
        except tweepy.TweepError as e:
            print("Error when requesting tweets: %s" % e)
            return
    else:
        try:
            new_tweets = auth_api.user_timeline(screen_name=screen_name, count=200, tweet_mode='extended')
            alltweets.extend(new_tweets)
        except tweepy.TweepError as e:
            print("Error when requesting tweets: %s" % e)
            return

        while len(new_tweets) > 0:
            oldest = alltweets[-1].id - 1
            try:
                new_tweets = auth_api.user_timeline(screen_name=screen_name, count=200,
                                                    max_id=oldest, tweet_mode='extended')
            except tweepy.TweepError as e:
                print("Error when requesting tweets, %d tweets dowloaded(total:%d)" % (len(alltweets), tweets_count))
                print("Error msg: %s" % e)
                break

            alltweets.extend(new_tweets)
            if (len(alltweets) >= tweets_count):
                break
            print("...%s tweets downloaded so far" % (len(alltweets)))

    if save_path is None:
        try:
            file = open(screen_name+'_tweets.json', 'w')
        except:
            raise Exception("fail to open" + screen_name + '_tweets.json')
    else:
        try:
            file = open(save_path, 'w')
        except:
            raise Exception("fail to open" + save_path)

    print("Writing tweet objects to JSON please wait...")
    for status in alltweets:
        alltweets_json.append(status._json)

    try:
        json.dump(alltweets_json, file, sort_keys=True, indent=4)
        print("Writing Finish...")
    except Exception as e:
        print("json dump to file failed!")
        print("error msg: %s" % e)
    file.close()

def extract_images_url(file_name):
    image_urls = []
    with open(file_name) as file:
        data = json.loads(file.read())

    for tweet in data:
        if 'extended_entities' in tweet.keys():
            extended_entities = tweet['extended_entities']['media']
            for extended_entity in extended_entities:
                if 'photo' == extended_entity['type']:
                    image_urls.append(extended_entity['media_url'])

    return image_urls

def download_images(user, urls=[]):
    save_path = './download_images'
    count = 0
    # create saving path
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    save_path = os.path.join(save_path, user)
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    # start downloading...
    for url in urls:
        save_name = 'image-%05d.jpg' % count
        # try 3 times to download images
        for i in range(0, 3):
            try:
                file = open(os.path.join(save_path, save_name), 'wb')
                file.write(urllib.request.urlopen(url).read())
                count += 1
                file.close()
                break
            except IOError as e:
                print("Error when downloading image(%s)" % url)
                print("error msg: %s" % e)
        if (count % 200 == 0):
            print("...%d images downloaded so far" % count)

    print("download %d images from %d urls" % (count, len(urls)))

def get_images_from_feed(screen_name, auth_file):
    print("authorize Twitter...")
    api = twitter_OAuth_login(auth_file)
    print("start grabbing tweets...")
    # Twitter can only return maximum 3000+ tweets
    download_tweets(api, screen_name, 3500)
    print("start downloading images...")
    urls = extract_images_url(file_name=screen_name+'_tweets.json')
    download_images(screen_name, urls)
    print("..................finish")
