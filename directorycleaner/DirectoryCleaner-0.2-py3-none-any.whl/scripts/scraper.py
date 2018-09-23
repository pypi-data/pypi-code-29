from bs4 import BeautifulSoup
import requests
import json

URL = "https://www.online-convert.com/file-type"
TAG = "table"
FILE_FORMATS = []
FILE_FORMATS_DICT = {}

"""Left in to show how the data was collected."""
def scraper(url, tag):
    trs = []
    tds= []

    """Find all tables in the markup. If you're not familiar with BeautifulSoup it will
    essentially put all the tables in a list. From here once we have all the tables we can
    then find all the tags inside the tables. We only need the first two entries, being the
    name of the files extension and the second being the description of what type of file it is"""

    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    tables = soup.findAll(tag)

    for row in tables:
        trs.append(row.findAll("tr"))
    for table in trs:
        tds.append(table)
    for tr in tds:
        for i in range(0, len(tr)):
            FILE_FORMATS.append(tr[i].findAll("td")[0:2])

if __name__ == "__main__":
    scraper(URL, TAG)

    for extension in FILE_FORMATS:
        if len(extension) != 0:
            FILE_FORMATS_DICT[extension[0].text.strip("\n")] = "(" + extension[0].text.strip("\n") + ")" + extension[1].text.strip()
    with open("extensions1.json", "w") as f:
        json.dump(FILE_FORMATS_DICT, f)
