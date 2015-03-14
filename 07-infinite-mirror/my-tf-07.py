#!/usr/bin/env python
import re, sys, operator

# Mileage may vary. If this crashes, make it lower
RECURSION_LIMIT = 9500
# We add a few more, because, contrary to the name,
# this doesn't just rule recursion: it rules the 
# depth of the call stack
sys.setrecursionlimit(RECURSION_LIMIT+10)

def count(word_list, stopwords, wordfreqs):
    # What to do with an empty list
    if word_list == []:
        return
    # The inductive case, what to do with a list of words
    else:
        # Process the head word
        word = word_list[0]
        if word not in stopwords:
            if word in word_freqs:
                wordfreqs[word] += 1
            else:
                wordfreqs[word] = 1
        # Process the tail 
        count(word_list[1:], stopwords, wordfreqs)

def wf_print(wordfreq):
    if wordfreq == []:
        return
    else:
        (w, c) = wordfreq[0]
        print w, '-', c
        wf_print(wordfreq[1:])


# This function has been inspired by the following topic. No code has been copied, but I have to recognize 'Escualo' for providing me an idea on how to chunk the file.
# http://stackoverflow.com/questions/2988211/how-to-read-a-single-character-at-a-time-from-a-file-in-python
#HARD
def chunk_read_file(f, stop_words, left_over):
        chunk = f.read(RECURSION_LIMIT);
        if(chunk == ""):
            return
        else:
            left_over = parse_stop_words(stop_words, chunk, left_over)
            chunk_read_file(f, stop_words, left_over)
#EASY
def parse_stop_words(stop_words, chunk, word):
    if chunk == "":
        return word;
    else:
        char = chunk[0];
        if char == ",":
            stop_words.append(word)
            word = ""
        else:
            word+= chunk[0]
        parse_stop_words(stop_words, chunk[1:], word)


stop_words = []
left_over = ""
f = open('../stop_words.txt')
chunk_read_file(f, stop_words, left_over)

words = re.findall('[a-z]{2,}', open(sys.argv[1]).read().lower())
word_freqs = {}
# Theoretically, we would just call count(words, word_freqs)
# Try doing that and see what happens.
for i in range(0, len(words), RECURSION_LIMIT):
    count(words[i:i+RECURSION_LIMIT], stop_words, word_freqs)

wf_print(sorted(word_freqs.iteritems(), key=operator.itemgetter(1), reverse=True)[:25])
