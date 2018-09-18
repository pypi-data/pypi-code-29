import itertools
import os
import re
import warnings
from enum import Enum

import requests

from .compatible import BeautifulSoup, urlparse
from .models import MailpapaException, Response
from .parse import parse_linkedin
from .utils import ACCEPTED_PATTERNS, random_user_agent, get_domain


def search(
    company: str,
    url: str,
    pattern: str = ACCEPTED_PATTERNS.FIRSTDOTLAST,
    positions: list = None,
) -> Response:
    """Searches the web for company emails"""
    domain = get_domain(url)

    ok, results = crawl_linkedin(company, positions, pattern, domain)

    response = Response("linkedin", results, ok)

    return response


def fetch(url, method="GET", **kwargs):
    r = requests.request(method, url, headers=random_user_agent(), **kwargs)
    return r


def crawl_linkedin(company, positions, pattern, domain):
    company = company.replace(" ", "-").lower()
    url = "https://www.linkedin.com/title/{}-at-{}"

    if isinstance(positions, str):
        position = positions.replace(" ", "-").lower()
        res = fetch(url.format(position, company))
        print(res.text)
        # with open(os.path.join(os.getcwd(), "mailpapa/sample/linkedin.html"), "r") as f:
        #     res = f.read()
        # return True, parse_linkedin(res, domain, pattern) if True else []
        return res.ok, parse_linkedin(res.text, domain, pattern) if res.ok else []

    if isinstance(positions, list):
        results = []
        for position in positions:
            position = position.replace(" ", "-").lower()
            res = fetch(url.format(position, company))
            if res.ok:
                results.append(parse_linkedin(res.text, domain, pattern))
            else:
                continue
        return res.ok, list(itertools.chain.from_iterable(results))
    return results


def domain_search(query: str) -> list:
    url = f"https://autocomplete.clearbit.com/v1/companies/suggest?query={query}"
    res = requests.get(url, headers=random_user_agent())

    if res.ok:
        return res.json()
    return []
