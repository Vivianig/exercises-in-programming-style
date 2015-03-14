lambda name : [x for x in map(lambda y : y.lower(), filter(lambda z: len(z) > 0, re.split('[^a-zA-Z]+', open(name).read()))) if x not in stops]

