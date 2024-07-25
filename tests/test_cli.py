#import minju_args_history.cli() import hello_msg
from minju_args_history.cli import hello_msg

def test_hello():
    m = hello_msg() 
    assert m == "hello"
