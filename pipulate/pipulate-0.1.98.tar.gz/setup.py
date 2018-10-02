from distutils.core import setup
setup(
  name = 'pipulate',
  packages = ['pipulate'],
  version = '0.1.98',
  download_url = 'https://github.com/miklevin/pipulate/archive/0.1.97.tar.gz',
  description = 'Make Data Dashboards with Google Sheets and not much else.',
  long_description = open('README.rst').read(),
  author = 'Mike Levin SEO, 360i & Commodore alum, Creator of HitTail now working in NYC for J2 Ziff-Davis Mashable IGN.',
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
