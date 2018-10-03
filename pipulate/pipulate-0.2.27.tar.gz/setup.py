from distutils.core import setup
setup(
    name = 'pipulate',
    packages = ['pipulate'],
    version = '0.2.27',
    download_url = 'https://github.com/miklevin/pipulate/archive/0.2.25.tar.gz',
    description = 'Free and Open Source SEO Software (update Google Sheets for Data Dashboards).',
    long_description = open('./README.rst', 'r').read(),
    author = 'Mike Levin SEO in NYC, alum of Commodore & 360i, Creator of HitTail, currently with J2/Ziff-Davis/IGN/Mashable.',
    license='MIT',
    author_email = 'miklevin@gmail.com',
    url = 'https://github.com/miklevin/pipulate',
    python_requires='>=3.6',
    install_requires=['gspread', 'httplib2', 'google-api-python-client'],
    keywords = ['seo', 'google sheets', 'data', 'datamaster', 'data master', 'google', 'database', 'sheets', 'pandas', 'gspread', 'google data', 'google spreadsheets', 'google sheet', 'google spreadsheet', 'spreadsheets', 'spreadsheet', 'databases', 'datascience', 'data science']
)

classifiers=[
    'Development Status :: 2 - Beta',
    'Intended Audience :: Marketing',
	'Topic :: Data',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
]
