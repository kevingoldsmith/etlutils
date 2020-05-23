from eautils.datafiles import *
import os

def test_get_yearly_file_path():
    assert get_yearly_file_path('data','foo',2020,'baz', False) == 'data/foo_2020.baz'
    assert get_yearly_file_path('data','foo',2020) == 'data/foo_2020.json'
    assert os.path.isdir('data')
    os.rmdir('data')
