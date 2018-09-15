from bots.models import TelegramBot
from functools import partial
from telegram import Bot, Update
from telegram.ext import Filters, MessageHandler


def message_handler(bot: Bot, update: Update, bot_instance: TelegramBot):
    chat_id = bot_instance.settings.get('chat_id')
    owner_ids = bot_instance.settings.get('owners', [])
    if update.message.chat_id not in owner_ids:
        return
    m = update.effective_message
    if hasattr(m, 'audio') and m.audio:
        a = m.audio
        r = bot.send_audio(chat_id, a.file_id, a.duration, a.performer, a.title)
    elif hasattr(m, 'document') and m.document:
        d = m.document
        r = bot.send_document(chat_id, d.file_id, d.file_name)
    elif hasattr(m, 'photo') and m.photo:
        p = m.photo
        r = bot.send_photo(chat_id, p[-1].file_id)
    elif hasattr(m, 'sticker') and m.sticker:
        s = m.sticker
        r = bot.send_sticker(chat_id, s.file_id)
    elif hasattr(m, 'video') and m.video:
        v = m.video
        r = bot.send_video(chat_id, v.file_id, v.duration)
    elif hasattr(m, 'voice') and m.voice:
        v = m.voice
        r = bot.send_voice(chat_id, v.file_id, v.duration)
    elif hasattr(m, 'video_note') and m.video_note:
        vn = m.video_note
        r = bot.send_video_note(chat_id, vn.file_id, vn.duration, vn.length)
    elif hasattr(m, 'contact') and m.contact:
        c = m.contact
        r = bot.send_contact(chat_id, c.phone_number, c.first_name, c.last_name)
    elif hasattr(m, 'location') and m.location:
        l = m.location
        r = bot.send_location(chat_id, l.latitude, l.longitude)
    elif hasattr(m, 'venue') and m.venue:
        v = m.venue
        r = bot.send_venue(chat_id, v.location.latitude, v.location.longitude, v.title, v.address, v.foursquare_id)
    elif hasattr(m, 'text') and m.text:
        r = bot.send_message(chat_id, m.text_html, 'html')


def setup(dispatcher):
    message_handler_callback = partial(message_handler, bot_instance=dispatcher.bot_instance)
    dispatcher.add_handler(MessageHandler(Filters.all, message_handler_callback))
    return dispatcher
