#!/usr/bin/env python3

import urllib.request
import xml.etree.ElementTree as ET
import argparse

class Token:
    def __init__(self, word, id, tag=None, lemma=None):
        self.word = word
        self.id = id
        self.tag = tag
        self.lemma = lemma

# url = 'https://www.deutschestextarchiv.de/book/download_fulltcf/16299'


def parse_xml(url, tags):
    with urllib.request.urlopen(url) as f:
        root = ET.fromstring(f.read())

    ns = {'tc': "http://www.dspin.de/data/textcorpus"}
    lex = {t.attrib["ID"]: Token(t.text, t.attrib["ID"]) for t in root.find('tc:TextCorpus', ns).find('tc:tokens', ns)}

    for lemma in root.find('tc:TextCorpus', ns).find('tc:lemmas', ns ):
        token = lex[lemma.attrib["tokenIDs"]]
        token.lemma = lemma.text
    for tag in root.find('tc:TextCorpus', ns ).find('tc:POStags', ns):
        token = lex[tag.attrib["tokenIDs"]]
        token.tag = tag.text
    for sent in root.find('tc:TextCorpus', ns).find('tc:sentences', ns):
        if tags:
            print(" ".join([lex[id].word + "/" + lex[id].tag for id in sent.attrib["tokenIDs"].split(" ")]))
        else:
            print(" ".join([lex[id].word + "/" + lex[id].lemma for id in sent.attrib["tokenIDs"].split(" ")]))

parser = argparse.ArgumentParser(description='write tokens with their tags or lemmas from tcf files')
parser.add_argument('-t', '--tags', help='output tokens with their tag instead of their lemma', action="store_true")
parser.add_argument('urls', help='list of urls to operate on', nargs='*')

args = parser.parse_args()
for url in args.urls:
    parse_xml(url, args.tags)
