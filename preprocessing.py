import os
import nltk
import re
import pickle
import numpy as np
import pandas as pd

from spacy.en import English
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from stop_words import get_stop_words

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.preprocessing import normalize

import matplotlib.pyplot as plt


def _read_dump_to_lookup(data_dump):
    """
    reads from a list of file names and creates a dictionary in which
    keys are file names and values are the content of those files.
    File names are unique and are http addresses of the original source.

    included brute error handling to manage corrupt data

    :param data_dump: list<str>
    :return: dict<str, str>
    """
    lookup = {}
    for i, dump in enumerate(data_dump):
        file_name = data_dump[i]
        try:
            with open(file_name, 'r') as f:
                lookup[file_name] = f.read()
        except:
            pass
    return lookup


def _ensure_all_fields_present(dicts):
    """
    reads from a list of dictionaries where keys are html addresses and values
    are html content and returns a list of dictionaries with keys are shared
    between all of them. In the case of this data set, only < 1 % of keys is
    discarded.

    :param dicts: list<dict>
    :return: list<dict>
    """
    common_keys = {key for key in dicts[0].keys()
                   if all((key in d.keys() for d in dicts[1:]))}

    def filter_dict(old_dict):
        return {key: old_dict[key] for key in common_keys}

    return [filter_dict(dictionary) for dictionary in dicts]


p_stemmer = PorterStemmer()
tokenizer = RegexpTokenizer(r'\w+[a-z]')
en_stop = get_stop_words('en')


def _tokenizing_stemming(curatorial_description):
    """
    function to tokenize and stem long descriptions

    input: string (single curatorial description)
    output: list of strings (stemmed tokens)
    """

    # TOKENIZING
    stringed = str(curatorial_description)
    tokens = tokenizer.tokenize(stringed)
    raw = stringed.lower()
    tokens = tokenizer.tokenize(raw)

    # REMOVING STOP WORDS
    # create English stop words list
    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]

    # STEMMING
    # stem token
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
    stemmed_tokens = ' '.join(stemmed_tokens)

    return stemmed_tokens


# TO DO: remove words such as "span" "div" "british museum" and maybe also first and last names

def _cleaning_images_finding_http(images_text):
    '''
    function which pulls out the http address for image corresponding to description

    input: string (long string from a website)
    output: string (http address pointing to an image)
    '''
    if images_text != "None":
        pull_out_http = re.split(" ", images_text)
        # print pull_out_http
        http_address = re.findall(
            'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
            pull_out_http[3])
        http_address = http_address[0]
    else:
        http_address = "None"
    return http_address


def _cleaning_htmltags_whitespace(text):
    """
    function to strip html from tags (e.g. '\n'), extra spaces and unicode

    input: string (long html)
    output: sting (only description)
    """
    new_text = re.sub(r"</?[a-zA-Z]*>", ' ', text)

    no_newlines = re.sub(r'\n', ' ', new_text)
    no_unicode = re.sub(r'[^\x00-\x7F]+', ' ', no_newlines)
    # print no_unicode
    no_extraspaces = re.sub(r"\s{2,}", ' ', no_unicode)
    no_search = re.sub(r"None", '', no_extraspaces)

    return no_search


def _spacy_tokenizer_lemmatizer(text):
    """
    Take a unicode string of text and return a list containing the lemmatized tokens
    Output: list of lemmatized tokens
    """
    parsed_data = parser(text)
    list_of_lemmatized_tokens = [token.lemma_ for token in parsed_data]
    return list_of_lemmatized_tokens

def _pulling_out_of_dictionary(dictionary):
    """

    :param dictionary:
    :return:
    """
    not_cleaned_description_pairs = []
    for link, curatorial_desription in physical_descriptions_lookup.iteritems():
        try:
            not_cleaned_description_pairs.append(
                (link, curatorial_desription))
        except Exception as e:
            print e.message

    return [pair[1] for pair in not_cleaned_description_pairs]

