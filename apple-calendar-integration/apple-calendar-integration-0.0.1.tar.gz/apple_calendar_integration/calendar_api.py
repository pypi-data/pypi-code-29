from requests import Session
import json
from datetime import date, timedelta, datetime
import uuid


class ICloudCalendarAPI(object):

    def __init__(self, username, password):
        self.session = Session()
        self.calendar_url = None
        self.dsid = None
        self.session.headers.update({
            'X-Apple-Widget-Key': 'd39ba9916b7251055b22c7f910e2ea796ee65e98b2ddecea8f5dde8d9d1a815d',
            'Content-Type': 'application/json'
        })
        self.login(username, password)

    def login(self, username, password):

        data = {
            'accountName': username,
            'rememberMe': False,
            'password': password,
            'trustTokens': []
        }
        res = self.session.post('https://idmsa.apple.com/appleauth/auth/signin', data=json.dumps(data))
        if res.status_code != 200 or 'X-Apple-Session-Token' not in res.headers:
            raise Exception("Cant login: Bad credentials")

        data = {
            "dsWebAuthToken": res.headers['X-Apple-Session-Token'],
            "extended_login": True
        }

        self.session.headers.update({
            'Origin': 'https://www.icloud.com'
        })
        res = self.session.post('https://setup.icloud.com/setup/ws/1/accountLogin', data=json.dumps(data))
        if res.status_code != 200:
            raise Exception("Cant login: {}".format(res.status_code))

        res_json = res.json()
        self.calendar_url = res_json['webservices']['calendar']['url']
        self.dsid = res_json['dsInfo']['dsid']

    def get_ctag(self):
        res_json = self.make_request('get', 'Cant get ctag {}'.format,
                                     '/ca/startup'
                                     '?dsid={dsid}'
                                     '&endDate={end_date}'
                                     '&lang=en-gb'
                                     '&startDate={start_date}'
                                     '&usertz=US%2FPacific'.format(
                                         dsid=self.dsid,
                                         start_date=(date.today() - timedelta(3)).strftime('%Y-%m-%d'),
                                         end_date=(date.today() + timedelta(3)).strftime('%Y-%m-%d'))
                                     )
        for calendar in res_json['Collection']:
            if calendar['guid'] == 'home':
                return calendar['ctag']
        return

    @staticmethod
    def timestamp_to_lst(timestamp):
        if not timestamp:
            return
        date_time = datetime.fromtimestamp(timestamp)
        concat_time = "{}{}{}".format(date_time.year,
                                      date_time.month if date_time.month > 9 else "0{}".format(date_time.month),
                                      date_time.day)
        return [int(concat_time), date_time.year, date_time.month, date_time.day, date_time.hour, date_time.minute, 330]

    @staticmethod
    def check_dict(key, dic):
        if key in dic:
            return dic[key]
        if key in ["weeks", "days", "hours", "minutes", "seconds"]:
            return 0
        return

    def add_repeat(self, data, guid, repeat):
        data['Event']['recurrence'] = '{}*MME-RID'.format(guid)
        until = self.timestamp_to_lst(self.check_dict("until", repeat))
        data['Recurrence'] = [
            {
                "pGuid": guid,
                "guid": "{}*MME-RID".format(guid),
                "count": self.check_dict("count", repeat),
                "freq": self.check_dict("freq", repeat),
                "interval": 1,
                "recurrenceMaster": False,
                "until": until,
                "byDay": None,
                "frequencyDays": None,
                "weekDays": None,
                "byMonth": None
            }
        ]

    def add_alarm(self, data, guid, alarm):
        data["Event"]["alarms"] = [guid]
        data["Alarm"] = [
            {
                "guid": guid,
                "pGuid": guid,
                "measurement": {
                    "before": alarm["before"],
                    "weeks": self.check_dict("weeks", alarm),
                    "days": self.check_dict("days", alarm),
                    "hours": self.check_dict("hours", alarm),
                    "minutes": self.check_dict("minutes", alarm),
                    "seconds": self.check_dict("seconds", alarm)
                },
                "description": "Event reminder",
                "messageType": "message"
            }
        ]

    @staticmethod
    def add_invites(data, guid, invites):
        data["Event"]["invitees"] = ["{}:{}".format(guid, email) for email in invites]
        data["Invitee"] = [
            {
                "guid": "{}:{}".format(guid, email),
                "pGuid": guid,
                "role": "REQ-PARTICIPANT",
                "isOrganizer": False,
                "email": email,
                "inviteeStatus": "NEEDS-ACTION",
                "commonName": "",
                "isMyId": False
            }
            for email in invites
        ]

    @staticmethod
    def remove_invites(data, invites):
        for email in invites:
            for index, invite in enumerate(data["Invitee"]):
                if email in invite['guid']:
                    data["Invitee"][index]["inviteeStatus"] = "X-UNINVITED"
                    break

    def make_request(self, method, error_message, url, data=None):

        if method == 'get':
            res = self.session.get(self.calendar_url + url)
        else:
            res = self.session.post(self.calendar_url + url, data=data)

        if res.status_code != 200:
            raise Exception(error_message(res.json()))
        return res.json()

    def get_event_info(self, guid):
        res = self.session.get('{calendar_url}/ca/eventdetail/home/{guid}'
                               '?dsid={dsid}'
                               '&lang=en-gb'
                               '&usertz=US%2FPacific'.format(
                                calendar_url=self.calendar_url,
                                guid=guid,
                                dsid=self.dsid))
        if res.status_code != 200:
            raise Exception('Cant get {} event info: '.format(guid, res.json()))
        return res.json()

    def create_event(self, title, start_date_timestamp, end_date_timestamp, repeat=None, alarm=None, note=None,
                     url=None, add_invites=None):
        ctag = self.get_ctag()
        guid = str(uuid.uuid4()).upper()
        start_date = self.timestamp_to_lst(start_date_timestamp)
        end_date = self.timestamp_to_lst(end_date_timestamp)
        data = {
            "Event": {
                "pGuid": "home",
                "extendedDetailsAreIncluded": True,
                "title": title,
                "location": "",
                "localStartDate": start_date,
                "localEndDate": end_date,
                "startDate": start_date,
                "endDate": end_date,
                "allDay": False,
                "duration": int((end_date_timestamp - start_date_timestamp) / 60),
                "guid": guid,
                "tz": "US/Pacific",
                "isJunk": False,
                "recurrenceMaster": False,
                "recurrenceException": False,
                "icon": 0,
                "hasAttachments": False,
                "changeRecurring": "future"
            },
            "ClientState": {
                "Collection": [
                    {
                        "guid": "home",
                        "ctag": ctag
                    }
                ],
                "fullState": False,
                "userTime": 1234567890,
                "alarmRange": 60
            }
        }
        if note:
            data["Event"]["description"] = note

        if url:
            data["Event"]["url"] = url

        if add_invites:
            self.add_invites(data, guid, add_invites)

        if repeat:
            self.add_repeat(data, guid, repeat)

        if alarm:
            self.add_alarm(data, guid, alarm)

        res_json = self.make_request('post', 'Cant create event: {}'.format,
                                     '/ca/events/home/{guid}'
                                     '?dsid={dsid}'
                                     '&lang=en-gb'
                                     '&usertz=US%2FPacific'.format(
                                      guid=guid,
                                      dsid=self.dsid,
                                      ), data=json.dumps(data))
        updates = res_json['ChangeSet']['updates']
        return updates['Event'][0]['etag'], updates['Collection'][0]['ctag'], guid

    def delete_event(self, etag, ctag, guid):
        data = {"Event": {},
                "ClientState": {
                    "Collection": [
                        {
                            "guid": "home", "ctag": ctag
                        }
                    ],
                    "fullState": False,
                    "userTime": 1234567890,
                    "alarmRange": 60
                }
                }
        self.make_request('post', 'Cant delete event: {}'.format,
                          '/ca/events/home/{guid}'
                          '?dsid={dsid}'
                          '&ifMatch={etag}'
                          '&lang=en-gb'
                          '&methodOverride=DELETE'
                          '&usertz=US%2FPacific'.format(
                                calendar_url=self.calendar_url,
                                guid=guid,
                                dsid=self.dsid,
                                etag=etag), data=json.dumps(data))
        return True

    def edit_event(self, etag, ctag, guid, title=None, start_date_timestamp=None, end_date_timestamp=None,
                   repeat=None, alarm=None, note=None, url=None, add_invites=None, remove_invites=None):
        data = self.get_event_info(guid)
        data.update({'Event': self.get_event_info(guid)['Event'][0]})

        if note:
            data["Event"]["description"] = note

        if url:
            data["Event"]["url"] = url

        if title:
            data['Event']['title'] = title

        if start_date_timestamp:
            start_date = self.timestamp_to_lst(start_date_timestamp)
            data['Event']['startDate'] = start_date
            data['Event']['localStartDate'] = start_date

            date_lst = data['Event']['endDate']
            existed_end_date_timestamp = datetime(date_lst[1], date_lst[2], date_lst[3], date_lst[4], date_lst[5]).timestamp()
            data['Event']['duration'] = int((existed_end_date_timestamp - start_date_timestamp) / 60)

        if end_date_timestamp:
            end_date = self.timestamp_to_lst(end_date_timestamp)
            data['Event']['endDate'] = end_date
            data['Event']['localEndDate'] = end_date

            date_lst = data['Event']['startDate']
            existed_start_date_timestamp = datetime(date_lst[1], date_lst[2], date_lst[3], date_lst[4], date_lst[5]).timestamp()
            data['Event']['duration'] = int((end_date_timestamp - existed_start_date_timestamp) / 60)

        if repeat:
            self.add_repeat(data, guid, repeat)

        if add_invites:
            self.add_invites(data, guid, add_invites)

        if remove_invites:
            self.remove_invites(data, remove_invites)

        if alarm:
            self.add_alarm(data, guid, alarm)

        data['ClientState'] = {
            "Collection": [
                {
                    "guid": "home",
                    "ctag": ctag
                }
            ],
            "fullState": False,
            "userTime": 1234567890,
            "alarmRange": 60
        }
        data["saveToMailbox"] = False
        data['Event']['changeRecurring'] = 'future'
        error_message = "Cant edit event {}".format
        res_json = self.make_request('post', error_message,
                                     '/ca/events/home/{guid}'
                                     '?dsid={dsid}'
                                     '&ifMatch={etag}'
                                     '&lang=en-gb'
                                     '&methodOverride=PUT'
                                     '&usertz=US%2FPacific'.format(
                                      guid=guid,
                                      dsid=self.dsid,
                                      etag=etag), data=json.dumps(data))

        return res_json['ChangeSet']['updates']['Event'][0]['etag']
