import json
import requests
from bs4 import BeautifulSoup
from urlparse import urljoin


def get_all_attractions():
    base_url = 'https://www.liseberg.se'

    soup = BeautifulSoup(
        requests.get(urljoin(base_url, '/attraktioner')).text,
        'html.parser'
    )

    attractions = [
        json.loads(requests.get(urljoin(
            base_url,
            el.get('data-queue-api')
        )).text) for el in soup.find_all('div', {'class': 'queue js-queue'})
    ]

    return attractions
