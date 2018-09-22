from datetime import datetime
from typing import List

import click
import praw

from enlightenme.news.news import News
from enlightenme.sources import Source


class RedditSource(Source):
    NUMBER_OF_REDDITS = 10
    HELP = "Source: Reddit (http://reddit.com/)"

    def __init__(self, client_id: str = None,
                 client_secret: str = None) -> None:
        self._client_id = client_id
        self._client_secret = client_secret
        self.reddit = praw.Reddit(client_id=client_id,
                                  user_agent='enlightenme',
                                  client_secret=self._client_secret)

    @classmethod
    def name(cls):
        return 'reddit'

    @classmethod
    def params(cls) -> List[click.Option]:
        client_help = "See: https://github.com/reddit-archive/" + \
                      "reddit/wiki/OAuth2-Quick-Start-Example#first-steps. " \
                      "Value can also be provided via env var %s"
        client_id_env_var = 'REDDIT_CLIENT_ID'
        client_secret_env_var = 'REDDIT_CLIENT_SECRET'
        return [
            click.Option(('--client-id', '-c'),
                         envvar=client_id_env_var,
                         required=True,
                         prompt=True,
                         hide_input=True,
                         help=client_help % client_id_env_var),
            click.Option(('--client-secret', '-s'),
                         envvar=client_secret_env_var,
                         required=True,
                         prompt=True,
                         hide_input=True,
                         help=client_help % client_secret_env_var)
        ]

    def fetch(self, keywords: List = None) -> List[News]:
        subreddits = '+'.join(keywords) if keywords else 'all'
        hot_reddits = self.reddit.subreddit(subreddits). \
            hot(limit=RedditSource.NUMBER_OF_REDDITS)
        return [
            News(title=submission.title,
                 published_at=datetime.fromtimestamp(submission.created_utc),
                 body=submission.selftext,
                 url=submission.url,
                 tags=[str(submission.subreddit)],
                 source=RedditSource.name())
            for submission in hot_reddits]
