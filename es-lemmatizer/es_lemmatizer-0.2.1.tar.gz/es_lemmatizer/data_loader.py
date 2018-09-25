from collections import defaultdict
import os

_ROOT = os.path.abspath(os.path.dirname(__file__))


dictionary_names = [
  "MM.adj",
  "MM.adv",
  "MM.int",
  "MM.nom",
  "MM.tanc",
  "MM.vaux",
  "MM.verb",
]

def get_file(n):
  with open(os.path.join(_ROOT, 'data', n)) as f:
    return f.readlines()

def has_accent(form):
  intersection = {"á","é","í","ó","ú","ü"} & set(form)
  return len(intersection) > 0

def remove_accent(form):
  return form.replace("á", "a").replace("é", "e").replace("í", "i")\
    .replace("ó", "o").replace("ú", "u").replace("ü","u")

def add_entry(entries, entries_no_accent, form, lemma):
  if form not in entries:
    entries[form] = lemma
    if has_accent(form):
      entries_no_accent[remove_accent(form)] = lemma

def parse_entry(entry, lookup_tables, lookup_tables_no_accents):
  [form, lemma, tag] = entry.strip().split(" ")
  if tag.startswith('D'): # determiner
    add_entry(lookup_tables["DET"], lookup_tables_no_accents["DET"], form, lemma)
  if tag.startswith('A'): # adjective
    add_entry(lookup_tables["ADJ"], lookup_tables_no_accents["ADJ"], form, lemma)
  if tag.startswith('N'): # noun
    add_entry(lookup_tables["NOUN"], lookup_tables_no_accents["NOUN"], form, lemma)
  if tag.startswith('V'): # verb
    add_entry(lookup_tables["VERB"], lookup_tables_no_accents["VERB"], form, lemma)
    add_entry(lookup_tables["AUX"], lookup_tables_no_accents["AUX"], form, lemma)
  if tag.startswith('R'): # adverb
    add_entry(lookup_tables["ADV"], lookup_tables_no_accents["ADV"], form, lemma)
  if tag.startswith('S'): # adposition
    add_entry(lookup_tables["ADP"], lookup_tables_no_accents["ADP"], form, lemma)
  if tag.startswith('C'): # conjuntion
    add_entry(lookup_tables["CONJ"], lookup_tables_no_accents["CONJ"], form, lemma)
  if tag.startswith('P'): # pronoun
    add_entry(lookup_tables["PRON"], lookup_tables_no_accents["PRON"], form, lemma)
  if tag.startswith('I'): # interjection
    add_entry(lookup_tables["INTJ"], lookup_tables_no_accents["INTJ"], form, lemma)


def process_file(n, lookup_tables, lookup_tables_no_accents):
  entries = get_file(n)
  for entry in entries:
    parse_entry(entry, lookup_tables, lookup_tables_no_accents)

def load_lookup_tables():
  lookup_tables = defaultdict(dict)
  lookup_tables_no_accents = defaultdict(dict)
  for name in dictionary_names:
    process_file(name, lookup_tables, lookup_tables_no_accents)
  return lookup_tables, lookup_tables_no_accents
