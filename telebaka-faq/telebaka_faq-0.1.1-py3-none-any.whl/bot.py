from bots.models import TelegramBot
from telegram import Update, Bot, ReplyKeyboardMarkup, KeyboardButton

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
    return dispatcher
