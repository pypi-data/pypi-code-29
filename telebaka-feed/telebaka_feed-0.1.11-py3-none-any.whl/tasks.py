import os
from time import sleep

import requests
import tempfile
from celery import shared_task
from dynamic_preferences.registries import global_preferences_registry
from telegram import Bot, TelegramError
from vk_api import VkApi
from raven.contrib.django.raven_compat.models import client

from bots.message_types import PhotoMessage
from telebaka_feed.models import VKFeed


global_preferences = global_preferences_registry.manager()


def get_vk_photo(attachment):
    for size in (2560, 1280, 807, 604, 130, 75):
        if f'photo_{size}' in attachment:
            return attachment[f'photo_{size}']
    return None


def get_file(url):
    fname = '?'.join(url.split('?')[:-1])
    extension = os.path.basename(fname).split('.')[-1]
    f = tempfile.NamedTemporaryFile(suffix=f'.{extension}' if extension else None)
    r = requests.get(url, stream=True)
    for chunk in r.iter_content(1024 * 1024):
        if chunk:
            f.write(chunk)
    f.seek(0)
    return f



@shared_task
def check_updates():
    vk_session = VkApi(token=global_preferences['feed__vk_api_token'], api_version='5.60')
    vk = vk_session.get_api()
    for vk_feed in VKFeed.objects.all():
        try:
            bot = Bot(vk_feed.bot.token)
            wall_data = vk.wall.get(owner_id=vk_feed.owner_id)
            for post in reversed(wall_data['items']):
                if post['id'] > vk_feed.last_id:
                    try:
                        if post['text']:
                            bot.send_message(vk_feed.chat_id, post['text'])
                        if 'attachments' in post:
                            photos = []
                            for image in filter(lambda a: 'photo' in a, post['attachments']):
                                url = get_vk_photo(image['photo'])
                                if url:
                                    photos.append(url.replace('\\', ''))
                            if photos:
                                PhotoMessage(photos, vk_feed.chat_id).send(bot)

                            for a in post['attachments']:
                                if 'audio' in a:
                                    f = get_file(a['audio']['url'])
                                    bot.send_audio(vk_feed.chat_id, f, a['audio'].get('duration'),
                                                   a['audio'].get('artist'), a['audio'].get('title'))

                        if vk_feed.send_links:
                            bot.send_message(vk_feed.chat_id, f"https://vk.com/wall{post['owner_id']}_{post['id']}",
                                             disable_web_page_preview=True)
                    except Exception:
                        client.captureException()
                    vk_feed.last_id = post['id']
            vk_feed.save()
        except Exception:
            client.captureException()
        finally:
            sleep(1)
