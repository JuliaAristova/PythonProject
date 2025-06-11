from hello import hello

def test_hello():
    # will not work as function does not return a value
    #hello("David") == "Hello, David"
    assert hello("David") == "Hello, David"

def test_default():
    assert hello() == "Hello, world"

def test_argument():
    for name in ["Hermione", "Harry", "Ron"]:
        assert hello(name) == f"Hello, {name}"
