from setuptools import setup

setup(
    name = "mrsh",
    version = "1.0.0.0",
    author = "Gioacchino Bombaci",
    author_email = "gioakbombaci@gmail.com",
    description = ("Core code for mrsh infrastructure"),
    license = "GPL",
    keywords = "mrsh's core",
    url = "http://packages.python.org/mrsh",
    packages=['mrsh','mrsh.rabbit', 'mrsh.mongo','mrsh.mongo.teacher', 'mrsh.mongo.factorizer', 'mrsh.mongo.common', 'mrsh.mongo.controller', 'mrsh.mongo.reccomender', 'mrsh.mongo.web_app', 'mrsh.mongo.news_consumer', 'mrsh.mongo.chat', 'mrsh.mongo.social_worker','mrsh.logger', 'mrsh.util','mrsh.social', 'mrsh.mongo.affinity'],
    install_requires=[
          'pika','pymongo','fluent-logger','nltk','stop-words','PyYAML'
    ],
    include_package_data=True,
    zip_safe=False
)
