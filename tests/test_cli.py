import minju_args_history.cli.hello_msg as msg

def test_hello():
    m = msg()
    assert m == "hello"
