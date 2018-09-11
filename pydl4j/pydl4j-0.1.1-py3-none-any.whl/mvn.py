from .downloader import download as download_file
import requests


_cache = {}
def _read(url):
    text = _cache.get(url)
    if text is None:
        text = requests.get(url).text
        if not text:
            raise Exception('Empty response. Check connectivity.')
        _cache[url] = text
    return text


def _parse_contents(text):
    contents = text.split('<pre id="contents">')[1]
    contents = contents.split('</pre>')[0]
    contents = contents.split('<a href="')
    _ = contents.pop(0)
    link_to_parent = contents.pop(0)
    contents = list(map(lambda x: x.split('"')[0], contents))
    contents = [c[:-1] for c in contents if c[-1] == '/']  # removes meta data files
    return contents



def get_artifacts(group):
    url = ('https://search.maven.org/remotecontent?filepath=' +
          'org/{}/'.format(group))
    response = _read(url)
    return _parse_contents(response)


def get_versions(group, artifact):
    url = ('https://search.maven.org/remotecontent?filepath=' +
          'org/{}/{}/'.format(group, artifact))
    response = _read(url)
    return _parse_contents(response)


def get_latest_version(group, artifact):
    return get_versions(group, artifact)[-1]


def get_jar_url(group, artifact, version=None):
    if version is None:
        version = get_versions(group, artifact)[-1]
    url = ('http://search.maven.org/remotecontent?filepath=' + 
          'org/{}/{}/{}/{}-{}.jar'.format(group, artifact, version,
                                          artifact, version))
    return url
