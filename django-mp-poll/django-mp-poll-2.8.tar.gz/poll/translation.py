
from modeltranslation.translator import translator

from poll.models import Poll, PollChoice


translator.register(Poll, fields=['question'])
translator.register(PollChoice, fields=['value'])
