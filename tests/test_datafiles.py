from eautils.datafiles import *
import os


def test_get_yearly_file_path():
    assert not os.path.exists('data')
    assert get_yearly_file_path('data','foo',2020,'baz', False) == 'data/foo_2020.baz'
    assert not os.path.exists('data')
    assert get_yearly_file_path('data','foo',2020) == 'data/foo_2020.json'
    assert os.path.isdir('data')
    assert get_yearly_file_path('data', '', 2020) == 'data/_2020.json'
    assert get_yearly_file_path('', '', -1) == '_-001.json'

    # cleanup
    os.rmdir('data')


def test_get_monthly_file_path():
    pass