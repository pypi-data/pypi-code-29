from bots.models import TelegramBot
from functools import partial
from telegram import Update, Bot, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import MessageHandler, Filters

from telebaka_faq.models import FAQSection


def get_keyboard(bot):
    sections = FAQSection.objects.filter(bot=bot, hidden=False)
    markup = ReplyKeyboardMarkup([KeyboardButton(s.title) for s in sections])
    return markup


def command(bot: Bot, update: Update, bot_instance: TelegramBot):
    markup = get_keyboard(bot)
    text = update.message.text
    try:
        if text.startswith('/'):
            section = FAQSection.objects.get(command=text[1:])
        else:
            section = FAQSection.objects.get(title=text)
    except FAQSection.DoesNotExist:
        return update.message.reply_text('Раздел не найден', reply_markup=markup)
    return update.message.reply_text(section.text, reply_markup=markup)


def setup(dispatcher):
    command_callback = partial(command, bot_instance=dispatcher.bot_instance)
    dispatcher.add_handler(MessageHandler(Filters.text, command_callback))
    return dispatcher
