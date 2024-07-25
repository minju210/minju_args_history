#import minju_args_history.cli() import hello_msg
from minju_args_history.db.utils import read_data
import pandas as pd

def test_read_data():
    r = read_data() 
    assert isinstance(r, pd.DataFrame)
