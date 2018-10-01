"""
Main module for survivorlib command line utility.
"""
from queue import Queue
from termcolor import colored
from tqdm import tqdm
from urllib.parse import urlparse
import click
import hashlib
import os
import requests
import sys
import threading
import xmltodict

archive_xml_location = \
    'https://archive.org/download/survival.library/survival.library_files.xml'
library_base_url = 'https://archive.org/download/survival.library/'

def do_log(message):
    print("\n-- " + message)

def done_log(message="Done."):
    print(colored("\n   - " + message, 'green'))

def fail_log(message):
    print(colored("\n   - " + message, 'red'))

def warn_log(message):
    print(colored("\n-- " + message, 'yellow'))

def validate_file(fname, md5, prefix=""):
    hash_md5 = hashlib.md5()
    do_log(prefix + "Validating " + fname)
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    is_valid = hash_md5.hexdigest() == md5
    if is_valid:
        done_log(fname + " is valid.")
    else:
        fail_log(fname + " not valid.")
    return is_valid

def get_section(meta):
    return os.path.basename(os.path.dirname(meta['@name']))

def print_sections():
    sections = set([ get_section(x) for x in get_pdfs_meta() ])
    for x in sorted(sections):
        print(x)

def download_pdfs(meta):
    thread_name = "Thread " + threading.current_thread().name + ":"
    while True:
        m = meta.get()
        url = library_base_url + m['@name']
        file_name = os.path.basename(m['@name'])
        section = get_section(m)
        file_path = os.path.join(section, file_name)
        md5 = m['md5']
        if os.path.isfile(file_path):
            if validate_file(file_path, md5, thread_name + " "):
                meta.task_done()
                continue
            else:
                os.remove(file_path)
        try:
            os.mkdir(section)
        except FileExistsError:
            pass
        do_log("{} Getting {}".format(thread_name, url))
        r = requests.get(url)
        do_log("{} Writing {}".format(thread_name, file_path))
        if os.path.isfile(file_path + '.part'):
            os.remove(file_path + '.part')
        with open(file_path + '.part', 'wb') as f:
            for data in tqdm(
                iterable=r.iter_content(),
                desc=file_path,
                ):
                f.write(data)
        if validate_file(file_path + '.part', md5, thread_name + " "):
            os.rename(file_path + '.part', file_path)
            done_log("{} Saved {}".format(thread_name, file_path))
        else:
            os.remove(file_path + '.part')
            fail_log("{} Failed {}: bad md5".format(thread_name, file_path))
        meta.task_done()

def get_pdfs_meta(section=""):
    pdfs_meta = []
    do_log("Getting file list xml.")
    r = requests.get(archive_xml_location)
    assert(r.status_code == 200)
    done_log()
    do_log("Parsing xml.")
    files_list = xmltodict.parse(r.text)['files']['file']
    done_log()
    do_log("Extracting pdf meta.")
    pdfs_meta = [ x for x in files_list if x['format'].endswith('PDF') ]
    done_log("Extracted {} pdf meta's.".format(len(pdfs_meta)))
    if section:
        return [ x for x in pdfs_meta if get_section(x) == section ]
    return pdfs_meta

@click.command()
@click.option('-w', '--workers', default=4, show_default=True,
    help="Number of workers that download pdf's.")
@click.option('-l', '--list-sections', is_flag=True,
    help="List available sections and exit.")
@click.option('-s', '--section', default="",
    help="Specify single section to download.")
def main(workers, list_sections, section):
    if list_sections:
        print_sections()
        sys.exit(0)
    q = Queue(workers)
    for i in range(workers):
        t = threading.Thread(target=download_pdfs, name=str(i), args=(q,))
        t.setDaemon(True)
        t.start()
    do_log('Starting with {} workers.'.format(workers))
    try:
        for pdf_meta in get_pdfs_meta(section):
            q.put(pdf_meta)
    except KeyboardInterrupt:
        try:
            warn_log("FINISHING DOWNLOADS. Press 'Ctrl+C' again to abort.")
            q.join()
        except KeyboardInterrupt:
            do_log("Some files may be incomplete.")
            raise
    finally:
        q.join()
        sys.exit()

if __name__ == "__main__":
    main()

