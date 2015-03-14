lambda name : [x for x in map(lambda y : y.lower(), [z for z in re.split('[^a-zA-Z]+', open(name).read()) if len(z) > 0]) if x not in stops]



