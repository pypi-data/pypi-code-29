#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup


class KCOJ:
    def __init__(self, url: str):
        self.__url = url
        self.__session = requests.Session()

    @property
    def courses(self) -> list:
        """
        取得課程列表
        """
        try:
            # 取得資料
            response = self.__session.get(
                self.__url + '/Login', timeout=0.5, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 取出課程名稱
            result = []
            for tag in soup.find_all('font'):
                result.append(tag.get_text())
            # 回傳結果
            return result

        except requests.exceptions.Timeout:
            return ["Timeout"]

    @property
    def active(self) -> bool:
        """
        檢查登入狀態
        """
        try:
            # 取得資料
            response = self.__session.get(
                self.__url + '/TopMenu', timeout=0.5, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 回傳是否為登入成功才看得到的網頁
            return soup.find('a').get_text().strip() == '線上考試'

        except requests.exceptions.Timeout:
            return None

    def login(self, username: str, password: str, course: int) -> requests.Response:
        """
        登入課程
        """
        try:
            # 操作所需資訊
            payload = {
                'name': username,
                'passwd': password,
                'rdoCourse': course
            }
            # 回傳嘗試登入的回應
            return self.__session.post(
                self.__url + '/Login', data=payload, timeout=0.5, verify=False)

        except requests.exceptions.Timeout:
            return None

    def get_question(self) -> dict:
        """
        取得課程中的所有題目資訊
        """
        try:
            # 取得資料
            response = self.__session.get(
                self.__url + '/HomeworkBoard', timeout=0.5, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 整理題目資訊
            questions = {}
            for tag in soup.find_all('tr'):
                # 去除標題列
                if tag.find('a') == None:
                    continue

                # 取得題號
                number = tag.find('a').get_text().strip()
                # 儲存題目資訊
                questions[number] = {
                    # 繳交期限
                    'deadline': tag.find_all('td')[3].get_text().strip(),
                    # 是否已經過期限
                    'expired': tag.find_all('td')[4].get_text().strip() == '期限已過',
                    # 是否繳交
                    'status': tag.find_all('td')[6].get_text().strip() == '已繳',
                    # 程式語言種類
                    'language': tag.find_all('td')[5].get_text().strip(),
                }
            # 回傳結果
            return questions

        except requests.exceptions.Timeout:
            return {
                "Timeout": {
                    'deadline': "Timeout",
                    'expired': False,
                    'status': False,
                    'language': "Timeout",
                }
            }

    def get_question_content(self, number: str) -> str:
        """
        取得課程中特定題目內容
        """
        try:
            # 操作所需資訊
            params = {
                'hwId': number
            }
            # 取得資料
            response = self.__session.get(
                self.__url + '/showHomework', params=params, timeout=0.5, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 處理題目內容的 \r
            result = ''
            content = soup.find('body').get_text().replace('繳交作業', '').strip()
            for line in content.split('\r'):
                result += line.strip() + '\n'
            # 回傳結果
            return result

        except requests.exceptions.Timeout:
            return "Timeout"

    def get_question_passers(self, number: str) -> list:
        """
        取得課程中特定題目通過者列表
        """
        try:
            # 操作所需資訊
            params = {
                'HW_ID': number
            }
            # 取得資料
            response = self.__session.get(
                self.__url + '/success.jsp', params=params, timeout=0.5, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 整理通過者資訊
            passers = []
            for tag in soup.find_all('tr'):
                # 取得通過者學號
                passer = tag.get_text().replace('\n', '').strip()
                # 跳過標題列
                if passer != '學號':
                    passers.append(passer)
            # 回傳結果
            return passers

        except requests.exceptions.Timeout:
            return ["Timeout"]

    def get_question_results(self, number: str, username: str) -> dict:
        """
        取得課程中特定題目指定用戶之測試結果
        """
        try:
            # 操作所需資訊
            params = {
                'questionID': number,
                'studentID': username
            }
            # 取得資料
            response = self.__session.get(
                self.__url + '/CheckResult.jsp', params=params, timeout=0.5, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 整理指定用戶之測試結果
            results = {}
            for tag in soup.find_all('tr'):
                # 取得測試結果
                result = tag.find_all('td')
                # 跳過標題列
                if result[0].get_text().strip() != '測試編號':
                    index = result[0].get_text().strip()
                    status = result[1].get_text().strip()
                    results[index] = status
            # 回傳結果
            return results

        except requests.exceptions.Timeout:
            return {'Timeout': 'Timeout'}

    def update_password(self, password: str) -> bool:
        """
        修改登入密碼
        """
        try:
            # 操作所需資訊
            payload = {
                'pass': password,
                'submit': 'sumit'
            }
            # 修改密碼
            response = self.__session.post(
                self.__url + '/changePasswd', data=payload, timeout=0.5, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 回傳結果
            return str(soup.find('body')).split()[-2].strip() == 'Success'

        except requests.exceptions.Timeout:
            return None

    def post_question_answer(self, number: str, description: str, file_path: str) -> bool:
        """
        上傳特定題目的作業
        """
        try:
            # 操作所需資訊
            params = {
                'hwId': number
            }
            data = {
                'FileDesc': description
            }
            files = {
                'hwFile': open(file_path, 'rb')
            }
            # 上傳作業
            self.__session.get(self.__url + '/upLoadHw',
                               params=params, timeout=0.5, verify=False)
            response = self.__session.post(
                self.__url + '/upLoadFile', data=data, files=files, timeout=0.5)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 回傳結果
            return soup.find('body').get_text().strip() != '您沒有上傳檔案 請重新操作'

        except requests.exceptions.Timeout:
            return False

    def delete_question_answer(self, number: str) -> bool:
        """
        刪除特定題目的作業
        """
        try:
            # 操作所需資訊
            params = {
                'title': number
            }
            # 刪除作業
            response = self.__session.get(
                self.__url + '/delHw', params=params, timeout=0.5, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 回傳結果
            return soup.find('body').get_text().replace('\n', '').strip() == 'delete success'

        except requests.exceptions.Timeout:
            return None

    def get_notice(self) -> dict:
        """
        取得公布欄訊息列表
        """
        try:
            # 取得資料
            response = self.__session.get(
                self.__url + '/MessageBoard', timeout=0.5, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 整理公布欄訊息列表
            notices = {}
            for tag in soup.find_all('tr'):
                # 跳過標題列
                if tag.find('a') != None:
                    title = tag.find('a').get_text().strip()
                    date = tag.find_all('td')[1].get_text().strip()
                    notices[date] = title
            # 回傳結果
            return notices

        except requests.exceptions.Timeout:
            return {"Timeout": "Timeout"}

    def get_notice_content(self, time: str) -> str:
        """
        取得公布欄特定訊息內容
        """
        try:
            # 取得資料
            response = self.__session.get(
                self.__url + '/showArticle?time=' + time, timeout=0.5, verify=False)
            soup = BeautifulSoup(response.text, 'html.parser')
            # 回傳結果
            return soup.find('pre').get_text().strip().replace('\r', '')

        except requests.exceptions.Timeout:
            return "Timeout"

    def get_notices(self):
        """
        [deprecated] 建議使用方法 `get_notice()` 及 `get_notice_content()`
        """
        result = []
        # 取得公布欄訊息列表
        for date, title in self.get_notice().items():
            content = self.get_notice_content(date)
            result.append([date, title, content])
        # 回傳結果
        return result

    def get_courses(self):
        """
        [deprecated] 建議使用屬性 `courses`
        """
        # 直接回傳新 API 的結果
        return self.courses

    def check_online(self):
        """
        [deprecated] 建議使用屬性 `active`
        """
        # 直接回傳新 API 的結果
        return self.active

    def list_questions(self):
        """
        [deprecated] 建議使用方法 `get_question()`
        """
        # 取得新 API 的結果
        data = self.get_question()
        # 實作相容的結構
        result = {}
        for number in data:
            # 繳交期限
            deadline = data[number]['deadline']
            # 是否已經過期限
            expired = '期限已到' if data[number]['expired'] else '期限未到'
            # 是否繳交
            status = '已繳' if data[number]['status'] else '未繳'
            # 程式語言種類
            language = data[number]['language']
            # 儲存題目資訊
            result[number] = [deadline, expired, status, language]
        # 回傳結果
        return result

    def show_question(self, number):
        """
        [deprecated] 建議使用方法 `get_question_content()`
        """
        # 直接回傳新 API 的結果
        return self.get_question_content(number)

    def list_passers(self, number):
        """
        [deprecated] 建議使用方法 `get_question_passers()`
        """
        # 直接回傳新 API 的結果
        return self.get_question_passers(number)

    def list_results(self, number, username):
        """
        [deprecated] 建議使用方法 `get_question_results()`
        """
        # 取得新 API 的結果
        data = self.get_question_results(number, username)
        # 實作相容的結構
        result = []
        for number in data:
            # 儲存題目資訊
            result += [(number, data[number])]
        # 回傳結果
        return result

    def change_password(self, password):
        """
        [deprecated] 建議使用方法 `update_password()`
        """
        # 直接回傳新 API 的結果
        return self.update_password(password)

    def delete_answer(self, number):
        """
        [deprecated] 建議使用方法 `delete_question_answer()`
        """
        # 直接回傳新 API 的結果
        return self.delete_question_answer(number)

    def upload_answer(self, number, file_path):
        """
        [deprecated] 建議使用方法 `post_question_answer()`
        """
        # 直接回傳新 API 的結果
        return self.post_question_answer(number, "Send from KCOJ_api", file_path)
