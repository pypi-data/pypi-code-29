# -*- coding:utf-8 -*-
from django.dispatch import Signal

# 日志创建的信号
user_feed_created = Signal(providing_args=["feed_id"])

# 日志删除的信号
user_feed_delete = Signal(providing_args=["feed_publisher", "feed_type"])

# 美好生活审核的信号
user_album_checked = Signal(providing_args=["album_id"])

