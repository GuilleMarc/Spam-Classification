###########################################
# Code to implement a bag of words:
import pandas as pd

## Input data:
documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

## Remove punctuation and transform to lower case only:
lower_sans_punct= [message.lower().strip('!/./?') for message in documents]

## Split each word within each list of words:
preprocessed_documents= [message.split(" ") for message in lower_sans_punct]

## Additional: if only unqiue words are needed:
unique_words= [list(set(list_words)) for list_words in preprocessed_documents]

## A counter of words
from collections import Counter
counter_words= [Counter(message) for message in unique_words]

##### Alternatively: Implement a word counter from scratch:##############
def word_counter(txt_list):
    words_dict= {}
    for word in txt_list:
        if word not in words_dict.keys():
            words_dict[word] = 1
        else:
            words_dict[word] += words_dict[word]
    return words_dict

counter_words_scratch= [word_counter(message) for message in preprocessed_documents]
#########################################################################
