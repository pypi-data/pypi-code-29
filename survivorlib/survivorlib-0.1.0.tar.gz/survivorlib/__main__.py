"""
Main module for survivorlib command line utility.
"""
from queue import Queue
from tqdm import tqdm
from urllib.parse import urlparse
import hashlib
import os
import requests
import sys
import threading
import xmltodict

archive_xml_location = \
    'https://archive.org/download/survival.library/survival.library_files.xml'
library_base_url = 'http://www.survivorlibrary.com/library/'
#logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

def do_log(message):
    print("-- " + message)

def done_log(message="Done."):
    print("   - " + message)

def validate_file(fname, md5):
    hash_md5 = hashlib.md5()
    do_log("Validating " + fname)
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    is_valid = hash_md5.hexdigest() == md5
    done_log(fname + " is valid." if is_valid else "not valid.")
    return is_valid

def download_pdfs(meta):
    while True:
        m = meta.get()
        url = library_base_url + os.path.basename(m['@name'])
        file_name = os.path.basename(urlparse(url).path)
        section = os.path.basename(os.path.dirname(m['@name']))
        file_path = os.path.join(section, file_name)
        md5 = m['md5']
        if os.path.isfile(file_path):
            if validate_file(file_path, md5):
                meta.task_done()
                continue
        try:
            os.mkdir(section)
        except FileExistsError:
            pass
        do_log("Thread {}: Getting {}".format(
            threading.current_thread().name,
            url,
            ))
        r = requests.get(url)
        do_log("Thread {}: Writing {}".format(
            threading.current_thread().name,
            file_path,
            ))
        with open(file_path+'.part', 'wb') as f:
            for data in tqdm(
                iterable=r.iter_content(),
                desc=file_path,
                ):
                f.write(data)
        if validate_file(file_path+ '.part', md5):
            os.rename(file_path+'.part', file_path)
            done_log("Thread {}: Saved {}".format(
                threading.current_thread().name,
                file_path,
                ))
        else:
            os.remove(file_path+ '.part')
            done_log("Thread {}: Failed {}: bad md5".format(
                threading.current_thread().name,
                file_path,
                ))
        meta.task_done()

def get_pdfs_meta():
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
    return pdfs_meta

def main():
    concurrent = 16
    q = Queue(concurrent * 2)
    for i in range(concurrent):
        t = threading.Thread(target=download_pdfs, name=str(i), args=(q,))
        t.setDaemon(True)
        t.start()
    try:
        for pdf_meta in get_pdfs_meta():
            q.put(pdf_meta)
    except KeyboardInterrupt:
        try:
            do_log("\nFINISHING STARTED FILES. Press 'Ctrl+C' one more time to abort all.")
            while not q.empty():
                s = q.get()
                q.task_done()
        except KeyboardInterrupt:
            do_log("Some files may be incomplete.")
            sys.exit(1)
    finally:
        q.join()
        done_log()
        sys.exit()

        
if __name__ == "__main__":
    main()


