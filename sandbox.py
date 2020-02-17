
parsepoints = ['<th>error</th><td>IPDefinedError(', "'", 'errormsg', 'dog', 'swan', 'pig', 'goat', 'sheep']
testpos = 0
if 'dog' in parsepoints:
    print(type(parsepoints.index('dog')))
    testpos = parsepoints.index("dog") + 3
    print(parsepoints.index('dog'))
if "'" in parsepoints:
    print(parsepoints.index("'"))
if 'goat' in parsepoints:
    print(parsepoints.index('goat'))
