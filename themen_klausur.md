# Wichtige Themen für die Klausur:

## 1. Korpusverarbeitung mit der shell 
- Dateiverarbeitung: ls, cd etc.

- Variablen, Quoting, Globbing, Kommandozeilenargumente

- Operatoren und Pipes

- Textwerkzeuge: echo, wc, grep, tr, sort, uniq, sed, awk; Frequenzlisten

- Shell- und Python-Skripte ausführen: chmod, argparse etc.

## 2. Korpusverarbeitung in Python 
- NLTK-Preprocessing-Methoden: word_tokenize, CorpusReader

- NLTK-Resourcen: Plain-Text-Korpora, Tagged-Korpora, Treebanks, Wordlisten

- NLTK-Korpus-Statistik: Frequenzlisten mit (Conditional)FreqDist, Kollokationen/ngrams

## 3. Korpusannotation mit stanza
- Processors: Tokenization, Lemmatization, POS Tagging, Syntactic Parsing, Named Entity Recognition, Sentiment Analysis

- regelbasierte vs. statistische Annotationsmodelle

- UD-Korpora

## 4. Deskriptive Korpusanalyse mit pandas
- Arbeiten mit Dataframes

- pandas-Statistik-Methoden: mean, sum etc.

- Berechnung von Frequenzlisten mit pandas-Methoden bzw. Counter

## 5. Explorative Korpusanalyse mit scikit-learn
- Train-Test-Split

- CountVectorizer, TfidfVectorizer

- Clustering, Topic-Modeling

- Dimensionsreduktion, Scaling

## 6. Unicode und Zeichenkodierung 
- Kodierungen: ASCII, Latin/ISO-8859, UTF8

- UNIX-Kodierungstools: uconv/iconv, recode, hexdump, file

- Encoding in Python: encode/decode, unicodedata, chardet

- kombinierende Zeichen


## 7. Parsing semistrukturierter Korpusformate
- JSON-Parser, XML-Parser

- XML-Syntax: Elemente, Attribute, Entitäten

- Download von Korpusfiles: requests, urllib

- Korpus-Formate: TEI-XML, TCF-XML

## 8. Erzeugung eigener Tagger
- Mapping verschiedener Tagsets

- Training und Serialisierung/Speicherung eigener Tagger mit NLTK-Elternklasse

- Verknüpfung von Taggern über Backoff-Tagger
