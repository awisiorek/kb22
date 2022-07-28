import json
import random 
import time 
import logging
import os.path
import queue
import threading
import concurrent.futures
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
    secs = random.uniform(0.5, 2)
    time.sleep(secs)
    secs = 0
    logging.info(f"downloading {url} after waiting {secs}s")
    with urlopen(url) as f:
        return f.read() 

def download_to(url, out):
    with open(out, 'wb') as f:
        f.write(download(url))
          
def query(q):
    return json.loads(download(query_url(q)))

def producer(pipeline, out, max, q):
    ids = set()
    start = 1
    with pipeline as p:
        while len(ids) < max:
            q["limit"] = max 
            q["start"] = start 
            q["fmt"] = "json"
            start = max + start 
            hits = query(q)
            for hit in hits["hits_"]:
                id = hit["meta_"]["dtaid"]
                basename = hit["meta_"]["basename"]
                if id not in ids:
                    ids.add(id)
                    p.add_url(tei_url(basename), os.path.join(out, f'{id}.tei.xml'))
                    p.add_url(tcf_url(id), os.path.join(out, f'{id}.tcf.xml'))
                if len(ids) == max:
                    return 
            

def consumer(pipeline):
    while True:
        url, out, ok = pipeline.get_url()
        if not ok:
            return 
        download_to(url, out)
        
class Pipeline(queue.Queue):
    def __init__(self):
        super().__init__(maxsize=10)
        
    def close(self):
        self.put((None, None)) # insert sentry
        logging.info('pipeline closed')
        
    def add_url(self, url, out):
        self.put((url, out))

    def get_url(self):
        ret = self.get()
        if ret == (None, None):
            self.put(ret) # reinsert sentry
            return (None, None, False)
        return (ret[0], ret[1], True)
    
    def __enter__(self):
        return self 
    
    def __exit__(self, et, ev, etb):
        self.close()
        return False
    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='write tokens with their tags or lemmas from tcf files')
    parser.add_argument('-m', '--max', help='max number of document', type=int, default=5)
    parser.add_argument('-d', '--dir', help='max number of document', type=str, default='.')
    parser.add_argument('query', help='query', nargs=1)
    args = parser.parse_args()
        
    pipeline = Pipeline()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
        executor.submit(producer, pipeline, args.dir, args.max, {'q': args.query[0]})
        executor.submit(consumer, pipeline)
        executor.submit(consumer, pipeline)
        executor.submit(consumer, pipeline)


    