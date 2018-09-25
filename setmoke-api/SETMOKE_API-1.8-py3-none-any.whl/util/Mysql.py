import pymysql
from datetime import datetime
import dateparser

class MySql:
    db=None
    cursor=None
    def __init__(self,host,user,password,db):

     self.db = pymysql.connect(host=host, user=user, passwd=password,db=db)

    def add_kwd(self, keyword, result, user_id, required_keyword=None, optional_keyword=None, excluded_keyword=None):
        self.cursor = self.db.cursor()
        self.cursor.execute("""INSERT INTO Keyword(alert_name, optional_keywords, required_keywords, excluded_keywords, User_id) VALUES(%s,%s,%s,%s,%s)""", (keyword, optional_keyword, required_keyword, excluded_keyword, user_id))
        self.cursor.execute("SELECT LAST_INSERT_ID(); ")
        keywordID=self.cursor.fetchone()
        for items in result:
            display_name = items.list.get_user().get_display_name()
            display_picture = items.list.get_user().get_display_picture()
            follower_count = items.list.get_user().get_follower_count()
            following_count = items.list.get_user().get_following_count()
            created_at = items.list.get_user().get_time()
            total_likes = items.list.get_user().get_total_likes()
            total_post = items.list.get_user().get_total_post()
            PostReshareCount = 0
            userID = items.list.get_user().get_user_id()
            self.cursor.execute(
                """INSERT INTO PostUser (DisplayPicture, DisplayName, FollowerCount,FollowingCount,TotalPosts,PostReshareCount,TotalLikes, UserID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                (display_picture, display_name, follower_count, following_count, total_post, PostReshareCount,
                 total_likes, userID))
            self.db.commit()
            self.cursor.execute("SELECT LAST_INSERT_ID(); ")
            postUserID = self.cursor.fetchone()
            post_content=str(items.list.get_text())

            time= items.list.get_user().get_time()
            user_id=items.list.get_user().get_user_id()
            source=items.list.get_source()
            resharer_count=items.list.get_reshare_count()
            post_id=items.list.get_status_id()
            sentiment=items.sentiment

            self.cursor.execute("""Insert into Post(Keyword_id, PostUser_id, statusID,CreatedAt, Source, ResharerCount,Sentiment,Content) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",(keywordID,postUserID,post_id,time,source,resharer_count,sentiment,post_content))
            self.db.commit()

            self.cursor.execute("SELECT LAST_INSERT_ID(); ")
            self.postID = self.cursor.fetchone()
            if resharer_count!='0':
              for user in items.list.get_resharer():
                  display_name = user.get_display_name()
                  display_picture = user.get_display_picture()
                  follower_count = user.get_follower_count()
                  following_count = user.get_following_count()
                  created_at = user.get_time()
                  total_likes = user.get_total_likes()
                  total_post = user.get_total_post()
                  PostReshareCount = 0
                  userID = user.get_user_id()
                  self.cursor.execute(
                      """INSERT INTO PostUser (DisplayPicture, DisplayName, FollowerCount,FollowingCount,TotalPosts,PostReshareCount,TotalLikes, UserID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                      (display_picture, display_name, follower_count, following_count, total_post, PostReshareCount,
                       total_likes, userID))
                  self.db.commit()
                  self.cursor.execute("SELECT LAST_INSERT_ID(); ")
                  postUserID = self.cursor.fetchone()
                  PostID=self.postID
                  self.cursor.execute(
                      """INSERT INTO Resharer (Post_id, PostUser_id) VALUES (%s,%s)""",
                      (PostID, postUserID))
                  self.db.commit()

        self.db.commit()
        #self.db.close()


    def add_to_Keyword(self, keyword, result, required_keyword=None, optional_keyword=None, excluded_keyword=None):
        self.cursor = self.db.cursor()
        self.cursor.execute("""INSERT INTO Keyword(Text, Optional, Required, Excluded) VALUES(%s,%s,%s,%s)""",
                            (keyword, optional_keyword, required_keyword, excluded_keyword))
        self.cursor.execute("SELECT LAST_INSERT_ID(); ")
        keywordID = self.cursor.fetchone()

    def read_keyword_from_db(self,user_id):
         self.cursor = self.db.cursor()
         self.cursor.execute("""SELECT alert_name, id from Keyword where user_id = %s""" ,(user_id))
         result_set = self.cursor.fetchall()
         return result_set

    def update_data_base(self, result, keyword_id,userid):
        self.cursor = self.db.cursor()

        for items in result:
            display_name = items.list.get_user().get_display_name()
            display_picture = items.list.get_user().get_display_picture()
            follower_count = items.list.get_user().get_follower_count()
            following_count = items.list.get_user().get_following_count()
            created_at = items.list.get_user().get_time()
            total_likes = items.list.get_user().get_total_likes()
            total_post = items.list.get_user().get_total_post()
            PostReshareCount = None
            userID = items.list.get_user().get_user_id()
            self.cursor.execute(
                """INSERT INTO PostUser (DisplayPicture, DisplayName, FollowerCount,FollowingCount,TotalPosts,PostReshareCount,TotalLikes, UserID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                (display_picture, display_name, follower_count, following_count, total_post, PostReshareCount,
                 total_likes, userID))
            self.db.commit()
            self.cursor.execute("SELECT LAST_INSERT_ID(); ")
            postUserID = self.cursor.fetchone()
            post_content = items.list.get_text()
            time = items.list.get_user().get_time()
            user_id = items.list.get_user().get_user_id()
            source = items.list.get_source()
            resharer_count = items.list.get_reshare_count()
            post_id = items.list.get_status_id()
            sentiment=items.sentiment


            self.cursor.execute(
                """Insert into Post(Keyword_id, PostUser_id, statusID,Content,CreatedAt, Source, ResharerCount,Sentiment) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                (keyword_id, postUserID, post_id, post_content, time, source, resharer_count,sentiment))
            self.db.commit()

            self.cursor.execute("SELECT LAST_INSERT_ID(); ")
            self.postID = self.cursor.fetchone()
            if resharer_count != '0':
                for user in items.list.get_resharer():
                    display_name = user.get_display_name()
                    display_picture = user.get_display_picture()
                    follower_count = user.get_follower_count()
                    following_count = user.get_following_count()
                    created_at = user.get_time()
                    total_likes = user.get_total_likes()
                    total_post = user.get_total_post()
                    PostReshareCount = None
                    userID = user.get_user_id()
                    self.cursor.execute(
                        """INSERT INTO PostUser (DisplayPicture, DisplayName, FollowerCount,FollowingCount,TotalPosts,PostReshareCount,TotalLikes, UserID) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""",
                        (display_picture, display_name, follower_count, following_count, total_post, PostReshareCount,
                         total_likes, userID))
                    self.db.commit()
                    self.cursor.execute("SELECT LAST_INSERT_ID(); ")
                    postUserID = self.cursor.fetchone()
                    PostID = self.postID
                    self.cursor.execute(
                        """INSERT INTO Resharer (Post_id, PostUser_id) VALUES (%s,%s)""",
                        (PostID, postUserID))
                    self.db.commit()

        self.db.commit()
        # self.db.close()
