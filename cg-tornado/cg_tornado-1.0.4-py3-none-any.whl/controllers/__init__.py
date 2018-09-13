# Filename: __init__.py

from .user_files import UserFiles, UserFile
from .attachments import Attachments, FileAttachment


Registry = {
    'user_files':  {'ctrl': UserFiles, 'model': UserFile},
    'attachments':  {'ctrl': Attachments, 'model': FileAttachment},
}
