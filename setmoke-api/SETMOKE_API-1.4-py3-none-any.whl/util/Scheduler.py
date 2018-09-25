from SETMOK_API.util.Mysql import MySql
from SETMOK_API.SETMOKE_API import SETMOKE_API

class Schedule:
    def __init__(self,host, database_user, database_password, database_name):

       self.db= MySql(host, database_user, database_password, database_name)

    def read_and_update_database(self):
        result_set=self.db.read_keyword_from_db()
        for row in result_set:
         keyword=str(row[0])
         keyword_id=str(row[1])
         data_fetch=SETMOKE_API(keyword,"/home/rehab/PycharmProjects/SETMOK_API/conf/config.ini")
         mentionlist=data_fetch.get_data()
         self.db.update_data_base(mentionlist, keyword_id)


