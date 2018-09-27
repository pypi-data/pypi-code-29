""" core schema viewer app settings
"""
import os

from django.conf import settings

if not settings.configured:
    settings.configure()

BASE_DIR_CORE_SCHEMA_VIEWER_APP = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
