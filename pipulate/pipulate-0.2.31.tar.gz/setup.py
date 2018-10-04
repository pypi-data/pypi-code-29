from distutils.core import setup

version = '0.2.31'
download_url = 'https://github.com/miklevin/pipulate/archive/%s.tar.gz' % version

setup(
    name = 'pipulate',
    packages = ['pipulate'],
    version = version,
    download_url = download_url,
    description = 'Free and Open Source SEO Software (Auto-Update Google Sheets).',
    long_description = open('README.rst').read(),
    author = 'Mike Levin SEO in NYC, alum of Commodore & 360i, Creator of HitTail.com, currently with J2/Ziff-Davis/IGN/Mashable.',
    license='MIT',
    author_email = 'miklevin@gmail.com',
    url = 'https://github.com/miklevin/pipulate',
    python_requires='>=3.6',
    install_requires=['gspread', 'httplib2', 'google-api-python-client'],
    keywords = ['open source', 'seo software', 'google sheets', 'linux scheduling', 'datamaster', 'datamasterng', 'pandas', 'gspread']
)

classifiers=[
    'Development Status :: 2 - Beta',
    'Intended Audience :: Marketing',
	'Topic :: Data',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7'
]
