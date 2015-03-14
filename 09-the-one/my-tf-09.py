#!/usr/bin/env python
import sys, re, operator, string

#
# The One functions for this example
#

#Takes a value and return a function that, when called, return the value
def wrap(value):
    return lambda: value;

#Take a wrapped value and a function, call the function on the application of the wrapped value
def bind(value, func):
    return func(value())

#printme(wrap(bind(wrap(sysarg), readfile), 
def printme(value):
    print value()
            


#
# The functions
#
def read_file(path_to_file):
    with open(path_to_file) as f:
        data = f.read()
    return data

def filter_chars(str_data):
    pattern = re.compile('[\W_]+')
    return pattern.sub(' ', str_data)

def normalize(str_data):
    return str_data.lower()

def scan(str_data):
    return str_data.split()

def remove_stop_words(word_list):
    with open('../stop_words.txt') as f:
        stop_words = f.read().split(',')
    # add single-letter words
    stop_words.extend(list(string.ascii_lowercase))
    return [w for w in word_list if not w in stop_words]

def frequencies(word_list):
    word_freqs = {}
    for w in word_list:
        if w in word_freqs:
            word_freqs[w] += 1
        else:
            word_freqs[w] = 1
    return word_freqs

def sort(word_freq):
    return sorted(word_freq.iteritems(), key=operator.itemgetter(1), reverse=True)

def top25_freqs(word_freqs):
    top25 = ""
    for tf in word_freqs[0:25]:
        top25 += str(tf[0]) + ' - ' + str(tf[1]) + '\n'
    return top25

#
# The main function
#
printme(wrap(bind(wrap(bind(wrap(bind(wrap(bind(wrap(bind(wrap(bind(wrap(bind(wrap(bind(wrap(sys.argv[1]), read_file)), filter_chars)), normalize)), scan)), remove_stop_words)), frequencies)), sort)), top25_freqs)))
