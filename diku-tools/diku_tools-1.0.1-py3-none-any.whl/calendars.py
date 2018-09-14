import math
import re
import urllib.request
from datetime import datetime, timedelta

import icalendar
from .tools import timedelta_string


class Calendar:
    current_event = None
    next_event = None
    loaded = False

    def __init__(self, username: str):
        cal_url = "https://personligtskema.ku.dk/ical.asp?objectclass=student&id=%s" % username
        cal_file = urllib.request.urlopen(cal_url)
        self.events = icalendar.Calendar.from_ical(cal_file.read())

    def load_current_next(self, now: datetime):
        self.loaded = True

        for event in self.events.walk("vevent"):
            end = event['DTEND'].dt
            if end < now:
                continue

            start = event['DTSTART'].dt
            if start.month >= now.month and start.day > now.day: break

            if start < now:
                self.current_event = LectureEvent(event)
            else:
                self.next_event = LectureEvent(event)
                break

    def get_current(self, now: datetime):
        if not self.loaded:
            self.load_current_next(now)
        return self.current_event

    def get_next(self, now: datetime):
        if not self.loaded:
            self.load_current_next(now)
        return self.next_event

    def get_day(self, year: int, month: int, day: int):
        events = []
        for event in self.events.walk("vevent"):
            start = event['DTSTART'].dt
            if start.year < year or start.month < month or start.day < day:
                continue

            end = event['DTEND'].dt
            if end.year > year:
                break
            if end.year == year:
                if end.month > month:
                    break
                if end.month == month:
                    if end.day > day:
                        break

            events.append(LectureEvent(event))
        return events


class CalendarEvent:

    def __init__(self, event: icalendar.Event):
        self.start = event['DTSTART'].dt
        self.end = event['DTEND'].dt
        self.title = event["SUMMARY"]
        self.description = event["DESCRIPTION"]

    def get_duration(self):
        return math.ceil((self.end - self.start).seconds / 3600)

    def get_start_delta(self, now: datetime):
        return timedelta_string((self.start - now) + timedelta(seconds=60*15))

    def get_end_delta(self, now: datetime):
        return timedelta_string(self.end - now)


class LectureEvent(CalendarEvent):

    def get_title(self):
        title = self.title.split(";")
        return re.sub(r' ?- ?\w+ ?$', '', title[min(1, len(title))])

    def get_type(self):
        return re.search(r' ?- ?(\w+) ?$', self.title).group(1)

    def get_room(self):
        room_match = re.search(r'Room: (.+?)\. ?\n', self.description)
        return room_match.group(1).split(":")[0] if room_match else "N/A"

    def get_prof(self):
        prof_match = re.search(r'Staff: (.+?)\. ?\n', self.description)
        if not prof_match:
            return "N/A"
        prof = prof_match.group(1).strip().split(",")
        return " ".join(list(reversed(prof))).strip()

    def to_dict(self):
        return {
            "title": self.get_title(),
            "type": self.get_type(),
            "room": self.get_room(),
            "professor": self.get_prof(),
            "start": self.start.hour,
            "duration": self.get_duration()
        }
