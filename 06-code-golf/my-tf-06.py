#!/usr/bin/env python

import re, sys, collections

stopwords, words = set(open('../stop_words.txt').read().split(',')), re.findall('[a-z]{2,}', open(sys.argv[1]).read().lower())
print "\n".join(["%s - %s" % (x[0], x[1]) for x in collections.Counter(w for w in words if w not in stopwords).most_common(25)])
