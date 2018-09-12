#!/usr/bin/env python
from setuptools import setup
from io import open

with open('README.md', encoding='utf-8') as f:
	long_description = f.read()

setup(
	name='calendar_tg_bot',
	version='1.0.0',
	description='pyTelegramApiBot module for calendar in telegram',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='prohibitme',
	author_email='prohibitme@ya.ru',
	url="https://github.com/prohi8bitme/calendar_tg_bot.git",
	classifieres=[
		'Programming Language :: Python :: 3.5',
		'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
	],
	install_requires=['pyTelegramBotAPI']
	)