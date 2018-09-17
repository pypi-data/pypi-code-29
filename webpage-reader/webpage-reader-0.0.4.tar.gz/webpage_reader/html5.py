import requests
import logging
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from flatten_json import unflatten

ELEMENTS_TO_ANALYSE_FOR_LINKS = [
    {
        "selectors": ["article a", ".article a"],
        "selector_name": "article_links"
    },
    {
        "selectors": ["header a", ".header a"],
        "selector_name": "header_nav_links"
    },
    {
        "selectors": ["footer a", ".footer a"],
        "selector_name": "footer_nav_links"
    },
    {
        "selectors": ["nav a", ".nav a"],
        "selector_name": "all_nav_links"
    },
    {
        "selectors": ["aside a", ".aside a"],
        "selector_name": "aside_nav_links"
    },
    {
        "selectors": ["a"],
        "selector_name": "all_links"
    }

]

IGNORE_HTML_CATS = [
    'script',
    'styles',
    'svg',
    'form',
    'input',
    'button',
    'path',
    'textarea'
]


def clean_text(text):
    return text.strip()


def get_website(url):
    parsed_uri = urlparse(url)
    website = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
    return website


def read_page(url=None, headers=None):
    """
    this method just reads a page and returns text of the page

    :param url: url to read
    :param headers: dictionary of header data
    :return: text of the webpage
    """
    logging.debug("reading the page {}".format(url))
    if url is None:
        return None
    if headers is None:
        headers = {}
    try:
        res = requests.get(url, headers=headers)
    except:
        res = None

    if res is None:
        return None
    else:
        return res.text


def analyse_links(soup=None, analyse_elements=None, website=None):
    links = {}
    for element in analyse_elements:
        selected_elems_data = []
        for selector in element['selectors']:
            selected_elems = soup.select(selector)
            for elem in selected_elems:
                el_href = elem.get('href')
                el_title = elem.get_text()
                if el_href:
                    if el_href.startswith("#"):
                        pass
                    else:
                        if el_href.startswith("//"):  # urls starting with //code.jquery.com/something.html
                            el_href = "http:{}".format(el_href)  # TODO - http is hard coded for now
                        elif "://" not in el_href:  # urls like "example.html" or "/example.html"
                            if el_href.startswith("/"):
                                pass
                            else:
                                el_href = "/{}".format(el_href)
                            el_href = "{}{}".format(website, el_href)

                        if el_href:
                            selected_elems_data.append({
                                'url': el_href,
                                'title': clean_text(el_title)
                            })
        links[element['selector_name']] = selected_elems_data
    return links


def analyse_meta(soup=None, analyse_elements=None, website=None):
    meta_data_dict = {}
    all_meta_elems = soup.select('meta')
    for meta_elem in all_meta_elems:
        meta_property = meta_elem.get('property')
        if meta_property:
            meta_data_dict[meta_property.replace(":", "__")] = meta_elem.get('content')

    return unflatten(meta_data_dict, separator="__")


def extract_texts_list(soup=None):
    texts_list = []
    body = soup.select('body')[0]
    for el in body.find_all():
        if el.name not in IGNORE_HTML_CATS:
            texts_list.append(el.get_text())
    return texts_list


def analyse_headings(soup=None):
    headings_dict = {}
    for selector in ["h1", "h2", "h3", "h4", "h5", "h6", "h7"]:
        elems = soup.select(selector)
        data = []
        for el in elems:
            data.append(clean_text(el.get_text()).replace("\n", " "))
        headings_dict[selector] = data
    return headings_dict


def analyse(page_text=None, url=None, analyse_elements=None):
    if analyse_elements is None:
        analyse_elements = ELEMENTS_TO_ANALYSE_FOR_LINKS

    if url is None:
        raise Exception("both url and page_text should be passes to analyse() function")
    if page_text is None:
        return {
            "status": "cannot_read_page",
            "result": {}
        }
    soup = BeautifulSoup(page_text, 'html.parser')
    result = {}
    if soup.title:
        result['title'] = clean_text(soup.title.string)
    else:
        result['title'] = None
    result['url'] = url
    website = get_website(url)
    result['website'] = website
    try:
        links = analyse_links(soup=soup, analyse_elements=analyse_elements, website=website)
    except Exception as e:
        links = []
        print(e)
    result['links'] = links

    try:
        meta_data = analyse_meta(soup=soup, analyse_elements=analyse_elements, website=website)
    except Exception as e:
        meta_data = {}
        print(e)
    result['meta'] = meta_data
    result['headings'] = analyse_headings(soup=soup)
    result['texts'] = extract_texts_list(soup=soup)
    return {
        "status": "success",
        "result": result
    }
