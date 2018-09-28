import math

from datetime import date
import io
import os
import tempfile
import uuid

from PIL import Image

from telegram import Bot, Update
from telegram.error import BadRequest
from telegram.ext import MessageHandler, Filters, CommandHandler

from telebaka_stickers.models import BotUser, BotUsage


def save_user(user):
    BotUser.objects.update_or_create(user_id=user.id,
                                     defaults={
                                         'username': user.username,
                                         'name': f'{user.first_name} {user.last_name or ""}'.rstrip()
                                     })


def update_stats():
    usage, created = BotUsage.objects.get_or_create(date=date.today())
    usage.usages += 1
    usage.save()


def sticker(bot: Bot, update: Update):
    save_user(update.effective_user)
    update_stats()

    if not update.effective_user.username:
        return update.message.reply_text('You have no username.')

    sticker_set_name = f'p{update.effective_user.id}_by_{bot.username}'

    file = update.message.sticker.get_file()
    with tempfile.NamedTemporaryFile(suffix='.webp') as f:
        f.write(file.download_as_bytearray())
        f.seek(0)
        im = Image.open(f).convert('RGBA')
    with tempfile.NamedTemporaryFile(suffix='.png') as f:
        im.save(f, 'png')
        f.seek(0)

        try:
            bot.get_sticker_set(sticker_set_name)
            bot.add_sticker_to_set(update.effective_user.id, sticker_set_name, f, update.message.sticker.emoji)
            update.message.reply_text(f'Done!\nLink: https://t.me/addstickers/{sticker_set_name}', quote=True)
        except BadRequest:
            bot.create_new_sticker_set(update.effective_user.id, sticker_set_name,
                                       f'@{update.effective_user.username}\'s stickers / @{bot.username}', f,
                                       update.message.sticker.emoji)
            update.message.reply_text(f'Done! Created sticker set: https://t.me/addstickers/{sticker_set_name}')


def resize_image(bot: Bot, update: Update):
    doc = update.message.document
    if doc.mime_type == 'image/png':
        with tempfile.NamedTemporaryFile(suffix='.png') as f:
            f.write(doc.get_file().download_as_bytearray())
            f.seek(0)
            im = Image.open(f).convert('RGBA')
        width, height = im.size
        ratio = 512 / max(width, height)
        target_width, target_height = (math.floor(width * ratio), math.floor(height * ratio))
        im = im.resize((target_width, target_height))
        with tempfile.NamedTemporaryFile(suffix='.png') as f:
            im.save(f, 'png')
            f.seek(0)
            update.message.reply_document(f, caption=f'{width}x{height} -> {target_width}x{target_height}')


def setup(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.sticker, sticker))
    dispatcher.add_handler(MessageHandler(Filters.document, sticker))
    return dispatcher
