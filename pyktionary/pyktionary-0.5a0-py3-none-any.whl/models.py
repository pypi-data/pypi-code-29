# pyktionary, simple Wiktionary scraper.
# Copyright (C) 2018 flow.gunso@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import requests
from bs4 import BeautifulSoup

TYPE_OF_WORDS = [
    "adjectifs", "adjectifs démonstratifs", "adjectifs exclamatifs", "adjectifs indéfinis",
    "adjectifs interrogatifs", "adjectifs numéraux", "adjectifs possessifs", "adverbes", "adverbes indéfinis",
    "adverbes interrogatifs", "adverbes pronominaux", "adverbes relatifs", "affixes", "articles",
    "articles définis", "articles indéfinis", "articles partitifs", "circonfixes", "classificateurs",
    "conjonctions", "conjonctions de coordination", "copules", "déterminants", "enclitiques",
    "fautes d’orthographe", "gismu", "infixes", "interfixes", "interjections", "lettres", "locutions",
    "locutions-phrases", "noms communs", "noms de famille", "noms propres", "noms scientifiques", "numéraux",
    "onomatopées", "particules", "particules numérales", "patronymes", "postpositions", "préfixes", "prénoms",
    "pré-noms", "prépositions", "pré-verbes", "proclitiques", "pronoms", "pronoms démonstratifs",
    "pronoms indéfinis", "pronoms interrogatifs", "pronoms personnels", "pronoms possessifs", "pronoms relatifs",
    "pronoms-adjectifs", "proverbes", "quantificateurs", "radicaux", "rafsi", "sinogrammes", "suffixes", "symboles",
    "variantes par contrainte typographique", "verbes"
]

class Wiktionary(object):
    """Define communication with Wiktionary."""

    def __init__(self, origin=None, language=None):
        self.origin = "fr" if origin is None else origin
        self.language = "français" if language is None else language
        self.url = "https://"+self.origin+".wiktionary.org/wiki/{}?printable=yes"
        self.soup = None

    def get_origin(self):
        """Get Wiktionary origin."""

    def set_origin(self, origin):
        """Set Wiktionary origin."""
        self.origin = origin
        self.url = "https://" + origin + ".wiktionary.org/wiki/{}?printable=yes"

    def get_language(self):
        """Get Wiktionary origin."""

    def set_language(self, language):
        """Set Wiktionary origin."""
        self.language = language

    def get_available_origin(self, language_code):
        """Get Wiktionary's available origins."""

    def get_available_language(self):
        """Get Wiktionary's available languages based upon the origin."""

    def word(self, word):
        """Fetch a word from Wiktionary."""

        # Request Wiktionary word page.
        response = requests.get(self.url.format(word))

        # Set a BeautifulSoup instance for that page.
        soup = BeautifulSoup(response.content, "html.parser")

        noarticle = soup.find('div', {'class': 'noarticletext'})
        if noarticle is not None:
            raise Exception(word + " entry does not exist.")

        # Look for the previously set language within the table of content.
        toc = soup.find('div', {'id': 'toc', 'class': 'toc'})
        if toc is None:
            raise Exception(word + " entry does not contain a table of content.")
        found = False
        for li in toc.find_all('li', {'class': 'toclevel-1'}):
            language = li.find('span', {'class': 'toctext'})
            if language.text.lower() == self.language:
                toc = li
                found = True
                break
        if not found:
            raise Exception("Language `" + self.language + "` does not exist in `" + word + "` entry.")

        # Parse the entry contents.
        entry = {}
        for li in toc.find_all('li', {'class': 'toclevel-2'}):
            section = li.find('span', {'class': 'toctext'}).text.strip()
            parsable_section = section.strip().replace(' ', '_')
            if section in ["Prononciation", "Anagrammes", "Voir aussi", "Références", "Forme de verbe"]:
                continue
            elif section != "Étymologie":
                section = "Définition"

            content = ""
            for tag in soup.find('span', {'id': parsable_section}).parent.find_next_siblings():
                if tag.name == 'h3':
                    break
                elif tag.name in ['dl', 'ol']:
                    content+=content+tag.prettify()
            content = content.replace('href="/wiki/', 'href="https://fr.wiktionary.org/wiki/')

            content = [item.strip() for item in content if str(item)]
            content = "".join(content)
            entry[section] = content

        return entry


# class Entry():
#     def __init__(self, soup):
#         self.soup = soup
#         self.word = Word()
#
# class Word():
#     def __init__(self):
#         self.