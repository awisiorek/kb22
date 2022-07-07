#import urllib.request
import sys
import xml.etree.ElementTree as ET 
import spacy 
from nltk import sent_tokenize


def append_text(text, str):
    if not str or str == "":
        return text 
    
    str = str.strip()
    if text == "":
        return str 
    if text[-1] == '¬':
        return text[:-1] + str 
    return text + " " + str 


def gather_text(node, text):
    text = append_text(text, node.text)
    for c in  node:
        text = gather_text(c, text)
    return append_text(text, node.tail)
    
    
# url = "https://www.deutschestextarchiv.de/book/download_xml/altmann_elementarorganismen_1890"
# url = "https://www.deutschestextarchiv.de/book/download_xml/brandes_naturlehre03_1832"
# with urllib.request.urlopen(url) as f:
#     root = ET.fromstring(f.read())
root = ET.fromstring(sys.stdin.read())    
out = ET.Element('doc')
nlp = spacy.load('de_core_news_sm')
sid = 1 
tid = 1 
text = gather_text(root, "")

for t in root.iter('{http://www.tei-c.org/ns/1.0}text'):
    text = gather_text(t, "")
    sents = sent_tokenize(text)
    for sent in sents: 
        stag = ET.SubElement(out, 's')
        stag.attrib = {'id': f"s-{sid}"}
        sid += 1
        tokens = nlp(sent)
        for token in tokens:
            ttag = ET.SubElement(stag, 'w')
            ttag.text = token.text 
            ttag.attrib = {'pos': token.pos_, 'id': f"w-{tid}"}
            tid += 1 
ET.dump(out)
