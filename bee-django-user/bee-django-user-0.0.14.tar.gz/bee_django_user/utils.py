# -*- coding:utf-8 -*-
__author__ = 'bee'

from bee_django_user.models import UserProfile
from django.conf import settings


def get_max_student_id():
    user_profile_list = UserProfile.objects.filter(student_id__isnull=False).order_by("-student_id")
    if user_profile_list.count() >= 1:
        max_student_id = user_profile_list.first().student_id

    else:
        max_student_id = 0
    return max_student_id


def get_user():
    user_list = UserProfile.objects.all()
    user_count = user_list.count()
    female_user_list = UserProfile.get_female_user_list()
    male_user_list = UserProfile.get_male_user_list()


def test():
    from  bee_django_course.models import UserLive
    from django.db.models import Count, Sum
    UserLive.objects.filter(status__in=[1, 2], record_status='10').values("user__userprofile__preuser__city").annotate(
        sum_duration=Sum("duration"), sum_user=Sum("user")).order_by('user__userprofile__preuser__city')

    # annotate(
    #     count_city=Count("user__userprofile__preuser__city")).order_by("-count_city")



