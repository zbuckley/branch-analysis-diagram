from Bad import bad

def test_addOne():
    assert(bad.doSomething(5) == 6)

def test_buildParser():
    parser = bad.buildParser()
    assert(parser.parse_args(['.']).path == '.')