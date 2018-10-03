from SETMOKE_API.util.ConfigurationParser import ConfigurationParser
from SETMOKE_API.retrievel.GooglePlus import GooglePlusDataRetrievel
from SETMOKE_API.retrievel.Twitter import TwitterDataRetrievel
import sys


class SETMOKE_API:


    def __init__(self, keyword=None, configpath=None,limit=2):
        """
        Keyword based search for fetching real time social media posts
        :param keyword: keyword to search
        :param configpath: contains API credentials for google and twitter
        :param limit: an optional parameter for setting the number of posts to get
        :param source: an optional parameter for getting the data either from twitter or google plus
        """

        self.set_keyword(keyword)
        self.set_config_path(configpath)
        self.set_limit(limit)

    def set_limit(self, limit):
        self.limit = limit

    def set_keyword(self,keyword):
        self.keyword = keyword
        if self.get_keyword()== None:
            sys.exit("Please provide a keyword to search")

    def set_config_path(self, config_path):
        self.config_path = config_path
        if self.get_config_path()==None :
            sys.exit("config_path is empty.Please provide config file path")



    def get_limit(self):
        return self.limit

    def get_keyword(self):
        return self.keyword

    def get_config_path(self):
        return self.config_path




    def get_googleplus_data(self):
        """
        Get the google api credential and pass it to the google api
        :return: list of posts and its sharer informations
        """

        obj = ConfigurationParser(self.get_config_path())
        gp_api_credentials = obj.get("googlePlus_credentials")
        api_key = gp_api_credentials["api_key"]
        googlePlusDataRetrievel = GooglePlusDataRetrievel(api_key)
        googlePlus_post_list = googlePlusDataRetrievel.get_googleplus_data(self.keyword, self.limit)
       # print(googlePlus_post_list)
        return googlePlus_post_list



    def get_Twitter_data(self):
        """
        Get the twitter api credential and pass it to the api
        :return: list of tweets and its sharer and resharers informations
        """

        obj = ConfigurationParser(self.get_config_path())
        twitter_api_credentials = obj.get("twitter_credentials")
        consumer_key = twitter_api_credentials["consumer_key"]
        consumer_secret = twitter_api_credentials["consumer_secret"]
        oauth_token = twitter_api_credentials["oauth_token"]
        oauth_token_secret = twitter_api_credentials["oauth_token_secret"]
        twitterDataRetrievel = TwitterDataRetrievel(consumer_key, consumer_secret, oauth_token, oauth_token_secret)
        tweets_list = twitterDataRetrievel.get_twitter_data(self.keyword, self.limit)
        return tweets_list


    def get_social_media_data(self):
        """
        Get the social media feed on the basis of social media retrievel
        :return: list of social media post containing keyword we provided for search
        """
        google_data = self.get_googleplus_data()
        twitter_data = self.get_Twitter_data()
        data = google_data + twitter_data
        return data
