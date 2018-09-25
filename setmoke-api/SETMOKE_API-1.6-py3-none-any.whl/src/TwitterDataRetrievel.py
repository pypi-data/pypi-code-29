import  tweepy, json
from twitter import *
from SETMOK_API.entities.Mention import Mention
from SETMOK_API.entities.Retweeter import Retweeter
from SETMOK_API.entities.User import User
from datetime import datetime
import moment
class S_Twitter :

    def __init__(self, consumer_key, consumer_secret, oauth_token, oauth_token_secret):

     auth1 = tweepy.OAuthHandler(consumer_key, consumer_secret)
     auth1.set_access_token(oauth_token, oauth_token_secret)
     self.tweeter_api = tweepy.API(auth1)

     self.twitter = Twitter(auth = OAuth('2744706848-k2qvSjn2Z2RJuwuNi6nG3pUFfkV6LaQrjlPiX5C',
                               'Mg2rgYE8kqPmLDmWLEdVUka9yHybp3r4lY8Y1oEWatJ2n',
                               'cYIVpMAP9NhcEUURwYOmANLnU',
                  'qjmdfdoJpEaKAMgfjJ1WXnDRGzRzParxwfkCUh1WFvCxfRSBIu'))
    def get_data(self, tweets_list, mentionlist):

        for tweet in tweets_list:
            if(self.count<self.limit) :
                mention=Mention()
                user=User()
                # print("----------------Post Info-----------------------")
                mention.set_source("Twitter")
                mention.set_reshare_count(str(tweet["retweet_count"]))
                if tweet["retweet_count"] == 0:
                    mention.set_text(tweet['full_text'])
                    print(tweet['full_text'])
                    # print(self.analize_sentiment(tweet['full_text']))
                else:
                    mention.set_text(tweet["retweeted_status"]['full_text'])
                    print(tweet["retweeted_status"]['full_text'])
                    # print(self.analize_sentiment(tweet["retweeted_status"]['full_text']))
                # # print(json.dumps(tweet, sort_keys=True, indent=4))
                mention.set_status_id(tweet["id_str"])
                print("Tweet ID: " + tweet["id_str"])
                # print("Created at: " + tweet["created_at"])

                sql_format = datetime.strptime(tweet["created_at"], '%a %b %d %H:%M:%S %z %Y')
                user.set_time(sql_format.strftime('%Y-%m-%d %H:%M:%S'))
                # t=datetime.strptime(tweet["created_at"], '%a %b %d %H:%M:%S %z %Y')
                # t.strftime('%Y-%m-%d %H:%M:%S')
                # m = moment.date(tweet["created_at"], '%a %b %d %H:%M:%S %z %Y')
                # sql_format = m.format('YYYY-M-D H:mm:ss')
                # print(sql_format)


                # print("Tweet Language: " + tweet["lang"])


                if tweet["retweet_count"] != 0:
                    user.set_display_name(tweet["retweeted_status"]["user"]["screen_name"])
                    user.set_display_picture(tweet["retweeted_status"]['user']['profile_image_url'])

                    mention.set_status_id(str(tweet["retweeted_status"]['id']))
                    # print("----------------Retweeted User Info-----------------------")
                    user.set_user_id(tweet["retweeted_status"]["user"]["id_str"])
                    # print("User Name: " + tweet["retweeted_status"]["user"]["name"])
                    # print("User Location: " + tweet["retweeted_status"]["user"]["location"])
                    user.set_total_post( str(tweet["retweeted_status"]['user']['statuses_count']))
                    user.set_following_count(str(tweet["retweeted_status"]['user']['friends_count']))
                    user.set_follower_count( str(tweet["retweeted_status"]['user']['followers_count']))
                    user.set_total_likes(str(tweet["retweeted_status"]['user']['favourites_count']))
                    # print("fav: " + str(tweet["retweeted_status"]['favorite_count']))


                    retweets = self.twitter.statuses.retweets._id(_id=str(tweet["retweeted_status"]['id']))
                    retweeterlist = []
                    for retweet in retweets:
                        retweeter = User()
                        retweeter.set_display_name(retweet["user"]["screen_name"])

                        #dt_str = datetime.datetime.strftime(retweet["created_at"], '%Y-%m-%d %H:%M:%S')

                        retweeter.set_time(retweet["created_at"])
                        retweeter.set_display_picture(retweet["user"]["profile_image_url"])

                        retweeter.set_user_id(retweet["user"]["id_str"])
                        retweeter.set_total_post(str(retweet['user']['statuses_count']))
                        retweeter.set_following_count(str(retweet['user']['friends_count']))
                        retweeter.set_follower_count(str(retweet['user']['followers_count']))
                        retweeter.set_total_likes(str(retweet['user']['favourites_count']))
                        retweeterlist.append(retweeter)
                        # print(" - retweeted by %s" % (retweet["user"]["screen_name"]))
                        # print("retweet time:"  +retweet["created_at"] )
                    mention.set_resharer(retweeterlist)
                else:
                    # print("----------------User Info-----------------------")
                    user.set_user_id(tweet["user"]["id_str"])
                    # print("User Name: " + tweet["user"]["name"])
                    # print("User Location: " + tweet["user"]["location"])

                    user.set_display_picture(tweet['user']['profile_image_url'])
                    user.set_display_name(tweet['user']['screen_name'])
                    user.set_total_post(str(tweet['user']['statuses_count']))
                    user.set_following_count( str(tweet['user']['friends_count']))
                    user.set_follower_count( str(tweet['user']['followers_count']))
                    user.set_total_likes(str(tweet['user']['favourites_count']))

                mention.set_user(user)
                mentionlist.append(mention)
                self.count=self.count+1
                print("<---------------------"+str(self.count)+"---------------------------->")
            else:
                    return mentionlist
        return mentionlist

    def get_twitter_data(self, keyword, limit):
      self.count=0
      self.limit=limit
      count=0
      mentionList=[]
      search_hashtag = tweepy.Cursor(self.tweeter_api.search, q=keyword,tweet_mode='extended').items(50)
      tweets_list = []
      for tweet in search_hashtag:
          tweets_list.append(json.loads(json.dumps(tweet._json)))
      id_ = tweets_list[len(tweets_list) - 1]["id"]
      mentionList=self.get_data(tweets_list ,mentionList)
      while (True):
        if self.count < self.limit :
          search_hashtag = tweepy.Cursor(self.tweeter_api.search, q=keyword, since_id=id_,tweet_mode='extended').items(50)
          for tweet in search_hashtag:
              print(json.dumps(tweet._json))
              for tweet in search_hashtag:
                  tweets_list.append(json.loads(json.dumps(tweet._json)))
              id_ = tweets_list[len(tweets_list) - 1]["id"]
              mentionList=self.get_data(tweets_list, mentionList)
              count=count+1
              print(count)

        else:
            break

      return mentionList