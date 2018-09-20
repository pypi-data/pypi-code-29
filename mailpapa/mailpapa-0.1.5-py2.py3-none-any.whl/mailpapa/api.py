import itertools

import requests

from .compatible import BeautifulSoup, urlparse
from .models import MailpapaException, Response
from .parse import parse_linkedin
from .utils import ACCEPTED_PATTERNS, get_domain, random_user_agent


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

    if not isinstance(positions, (str, list)):
        raise MailpapaException(
            "Expected list or string as type of 'positions' param. Instead got {}".format(
                type(positions)
            )
        )

    if isinstance(positions, str):
        position = positions.replace(" ", "-").lower()
        res = fetch(url.format(position, company))

        return res.ok, parse_linkedin(res.text, domain, pattern) if res.ok else []

    if isinstance(positions, list):
        results = []
        status = False

        for position in positions:
            position = position.replace(" ", "-").lower()
            res = fetch(url.format(position, company))

            # Backoff caught crawling
            # TODO: Backoff completely when caught at initial crawl
            if res.status_code == 999:
                continue

            if not res.ok:
                continue

            status = res.ok
            results.append(parse_linkedin(res.text, domain, pattern))

        if results:
            return status, list(itertools.chain.from_iterable(results))

        return status, []


def domain_search(query: str) -> list:
    url = f"https://autocomplete.clearbit.com/v1/companies/suggest?query={query}"
    res = requests.get(url, headers=random_user_agent())

    return res.json() if res.ok else False
