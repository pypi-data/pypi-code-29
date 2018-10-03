import  tweepy, json, time
from twitter import *
from src.retrievel.Post import Post
from src.retrievel.User import User
from datetime import datetime


class TwitterDataRetrievel :

    def __init__(self, consumer_key, consumer_secret, oauth_token, oauth_token_secret):

     auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
     auth1.set_access_token(oauth_token, oauth_token_secret)
     self.tweeter_api = tweepy.API(auth1)

     self.twitter = Twitter(auth = OAuth(oauth_token,
                                         oauth_token_secret,
                                         consumer_key,
                                         consumer_secret))
    def parse_data(self, tweets_list, post_message_list):
        """
        get real time feed and convert into to readable list
        :param tweets_list:  real time twitter feed
        :param post_message_list: formatted list containing required fields
        :return: readable list of necessary fields
        """
        for tweet in tweets_list:
            if(self.count<self.limit) :
                post_message=Post()
                post_user=User()
                print("----------------Post Info-----------------------")
                post_message.set_source("Twitter")
                post_message.set_reshare_count(str(tweet["retweet_count"]))
                post_message.set_status_id(tweet["id_str"])
                print("Tweet ID: " + tweet["id_str"])
                sql_format = datetime.strptime(tweet["created_at"], '%a %b %d %H:%M:%S %z %Y')
                post_user.set_time(sql_format.strftime('%Y-%m-%d %H:%M:%S'))
                # print("Tweet Language: " + tweet["lang"])
                if tweet["retweet_count"] != 0:
                    post_user.set_display_name(tweet["retweeted_status"]["user"]["screen_name"])
                    post_user.set_display_picture(tweet["retweeted_status"]['user']['profile_image_url'])
                    post_message.set_status_id(str(tweet["retweeted_status"]['id']))
                    # print("------                    post_user.set_total_likes(str(tweet['user']['favourites_count']))

                post_message.set_user(post_user)
                post_message_list.append(post_message)
                self.count=self.count+1
                print("<---------------------"+str(self.count)+"---------------------------->")
            else:
                    return post_message_list
        return post_message_list

    def get_twitter_data(self, keyword, limit):
        """
         :param keyword: a keyword to search posts from google_plus
         :param limit: Number of posts to return
         :return: readable list of google plus real time data feed
         """
        self.count = 0
        self.limit = limit
        count = 0
        post_list = []
        search_hashtag = tweepy.Cursor(self.tweeter_api.search, q=keyword, tweet_mode='extended').items(50)
        tweets_list = []
        for tweet in search_hashtag:
            tweets_list.append(json.loads(json.dumps(tweet._json)))
        id_ = tweets_list[len(tweets_list) - 1]["id"]
        post_list = self.parse_data(tweets_list, post_list)
        while (True):
            if self.count < self.limit:
                search_hashtag = tweepy.Cursor(self.tweeter_api.search, q=keyword, since_id=id_,
                                               tweet_mode='extended').items(50)
                for tweet in search_hashtag:
                    print(json.dumps(tweet._json))
                    for tweet in search_hashtag:
                        tweets_list.append(json.loads(json.dumps(tweet._json)))
                    id_ = tweets_list[len(tweets_list) - 1]["id"]
                    post_list = self.parse_data(tweets_list, post_list)
                    count = count + 1
                    print(count)
                time.sleep(1)

            else:
                break

        return post_list
 