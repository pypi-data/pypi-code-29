import requests
from bs4 import BeautifulSoup


def get_soup(link):

    try:

        link = link.replace('\n','').strip()
        headers = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(link,headers=headers)

        if response.status_code == requests.codes.ok:
            page = response.content
            soup = BeautifulSoup(page, "lxml")

        else:
            soup = None
            print("Requests returned status_code: {0}. {1}".format(response.status_code,link))

        return soup

    except Exception as e:
        print(str(e))
        print(link)


def prepare_url(host,model_name):
    if model_name:
        url = '{0}api/{1}/update/'.format(host,model_name)
    else:
        url = '{0}api/update/_bulk'.format(host)
    return url


def prepare_headers(token,username,password,json):
    headers = {
        'Authorization': 'Token {0}'.format(token),
        'user': username,
        'password': password,
    }
    if json:
        headers['Content-Type'] = 'application/json'
    return headers


def update_or_create_model_instance(host,token,username,password,data,model_name=None,json=False):

    url = prepare_url(host,model_name)
    headers = prepare_headers(token,username,password,json)
    if json:
        payload = data
        response = requests.put(url,headers=headers,json=payload)
    else:
        response = requests.put(url,headers=headers,data=data)

    return response


def list_model_instances(host,token,username,password,data,model_name,query=None):

    url = prepare_url(host,model_name) + query
    json = None
    headers = prepare_headers(token,username,password,json)
    response = requests.put(url,headers=headers)

    return response


def get_full_name_with_capitalised_surname(raw_name):
    first_name = ''
    last_name = ''
    for word in raw_name.split():
        if word.isupper() and '.' not in word:
            last_name += '{0} '.format(word.strip())
        else:
            first_name += '{0} '.format(word.strip().capitalize())
    first_name = first_name.strip()
    last_name = last_name.strip().title()
    full_name = '{0} {1}'.format(first_name,last_name)

    d = {
        'full_name': full_name,
        'first_name': first_name,
        'last_name': last_name,
    }

    return d


def extract_full_text(contains_full_text):
    full_text = ''
    for paragraph in contains_full_text.findAll('p'):
        full_text += paragraph.text.strip()
        full_text += '\n'
    full_text = full_text.strip()
    return full_text


def get_link_from_xml_item(item):
    for element in item:
        if str(element).strip().startswith('http'):
            link = element
            return link