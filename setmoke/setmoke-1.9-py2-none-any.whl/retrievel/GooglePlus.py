from apiclient import discovery
from src.retrievel.Post import  Post
from src.retrievel.User import User
import moment
class GooglePlusDataRetrievel  : 

    def __init__(self, API_KEY):
        self.GPLUS = discovery.build('plus', 'v1', developerKey=API_KEY)


    def get_googleplus_data(self, keyword, limit) :

        """

        :param keyword: a keyword to search posts from google_plus
        :param limit: Number of posts to return
        :return: readable list of google plus real time data feed
        """
        postList=[]
        activity = self.GPLUS.activities().search(query=keyword, maxResults=20).execute()
        counter = 0
        while (True):


            next_token = activity['nextPageToken']
            items = activity.get('items', [])
            for data in items:
                post = ' '.join(data['title'].strip().split())
                if post:
                    post_info = Post()
                    user=User()
                    print("----------------Post Info-----------------------")
                    post_info.set_source('GooglePlus')
                    url=data["url"].split("/")
                    post_info.set_status_id(url[-1])
                    post_info.set_reshare_count(str(data["object"]["resharers"]['totalItems']))
                    post_info.set_text(data["object"]['content'])
                    # for s in data['object']:
                    #     if s == 'attachments':
                    #         attachments = data["object"]['attachments']

                    #         for attachment in attachments:
                    #             print("attachments:" + attachment["url"])
                    print("----------------User Info-----------------------")
                    user.set_user_id(data['actor']["id"])
                    user.set_display_name(data['actor']['displayName'])
                    user.set_display_picture( data['actor']['image']['url'])
                    date = moment.date(data["published"], '%Y-%m-%dT%H:%M:%SZ')
                    sql_format = date.strftime('%Y-%m-%d %H:%M:%S')
                    user.set_time(sql_format)
                    post_info.set_user(user)
                    postList.append(post_info)
                    counter = counter + 1
                    print("--------------------------------------------"+ str(counter))
                    if counter>=limit:
                        break
            if counter<limit :
             activity = self.GPLUS.activities().search(query=keyword, maxResults=20, pageToken=next_token).execute()
            else:
                break
        return postList