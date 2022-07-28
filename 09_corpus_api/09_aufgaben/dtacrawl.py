import json
import random 
import time 
import logging
import argparse
from urllib.parse import urlunsplit
from urllib.parse import urlsplit
from urllib.parse import urlencode
from urllib.request import urlopen

logging.basicConfig(format="%(asctime)s: %(message)s", level=logging.INFO, datefmt="%H:%M:%S")

tei_baseurl = 'https://www.deutschestextarchiv.de/book/download_xml'
query_baseurl = 'https://kaskade.dwds.de/dstar/dta/dstar.perl'
tcf_baseurl = 'https://www.deutschestextarchiv.de/book/download_fulltcf'

def tei_url(basename):
    return tei_baseurl + "/" + basename

def tcf_url(base):
    return tcf_baseurl + "/" + base 
                 
def query_url(query):
    parts = list(urlsplit(query_baseurl))
    parts[3] = urlencode(query)
    return urlunsplit(parts)

def download(url):
    secs = random.uniform(0.5, 1.5)
    time.sleep(secs)
    logging.info(f"downloading {url} after waiting {secs}s")
    with urlopen(url) as f:
        return f.read() 

def download_to(url, out):
    with open(out, 'wb') as f:
        f.write(download(url))
          
def query(q):
    return json.loads(download(query_url(q)))

def dtaids(max, q):
    ids = {}
    start = 1
    while len(ids) < max:
        q["limit"] = max 
        q["start"] = start 
        q["fmt"] = "json"
        hits = query(q)
        for hit in hits["hits_"]:
            id = hit["meta_"]["dtaid"]
            if id not in ids:
                ids[id] = hit["meta_"]["basename"]
            if len(ids) == max:
                return ids 
        start = max + start
    return ids

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='write tokens with their tags or lemmas from tcf files')
    parser.add_argument('-m', '--max', help='max number of document', type=int, default=5)
    parser.add_argument('-d', '--dir', help='max number of document', type=str, default='.')
    parser.add_argument('query', help='query', nargs=1)
    args = parser.parse_args()

    ids = dtaids(args.max, {'q': args.query[0]})
    for id in ids:
        download_to(tei_url(ids[id]), f"{args.dir}/{id}.tei.xml")
        download_to(tcf_url(id), f"{args.dir}/{id}.tcf.xml")
    