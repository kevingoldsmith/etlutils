from etlutils.datafiles import *
import os
import pytest
import shutil
import tempfile
import json


@pytest.fixture
def cleandir():
    old_cwd = os.getcwd()
    newpath = tempfile.mkdtemp()
    os.chdir(newpath)
    yield
    os.chdir(old_cwd)
    shutil.rmtree(newpath)


def test_get_yearly_file_path(cleandir):
    assert not os.path.exists('data')
    assert get_yearly_file_path('data','foo',2020,'baz', False) == 'data/foo_2020.baz'
    assert not os.path.exists('data')
    assert get_yearly_file_path('data','foo',2020) == 'data/foo_2020.json'
    assert os.path.isdir('data')
    assert get_yearly_file_path('data', '', 2020) == 'data/2020.json'
    assert get_yearly_file_path('', '', -1) == '-001.json'


def test_get_monthly_file_path(cleandir):
    assert not os.path.exists('data')
    assert get_monthly_file_path('data', 'foo', 2020, 5, 'baz', False) == 'data/2020/foo_2020-05.baz'
    assert not os.path.exists('data')
    assert get_monthly_file_path('data', 'foo', 2020, 5) == 'data/2020/foo_2020-05.json'
    assert os.path.exists('data/2020')
    assert get_monthly_file_path('', '',  -2, -2) == '-002/-002--2.json'
    assert os.path.isdir('-002')


def test_get_daily_file_path(cleandir):
    assert not os.path.exists('data')
    assert get_daily_file_path('data', 'foo', 2020, 5, 1, 'baz', False) == 'data/2020/2020-05-01/foo.baz'
    assert not os.path.exists('data')
    assert get_daily_file_path('data', 'foo', 2020, 5, 1) == 'data/2020/2020-05-01/foo.json'
    assert os.path.exists('data/2020/2020-05-01')
    assert get_daily_file_path('', '', -2, -2, -2) == '-002/-002--2--2/.json'


def test_dump_to_monthly_json_file(cleandir):
    assert not os.path.exists('data')
    assert dump_to_monthly_json_file('data', 2020, 5, {'foo':'bar'}, 'blah') == 'data/2020/blah_2020-05.json'
    assert os.path.exists('data/2020/blah_2020-05.json')
    with open('data/2020/blah_2020-05.json', 'r') as f:
        data = json.load(f)
    assert data == {'foo':'bar'}

    assert dump_to_monthly_json_file('data', 2020, 5, {'bar':'baz'}) == 'data/2020/2020-05.json'
    assert os.path.exists('data/2020/2020-05.json')
    with open('data/2020/2020-05.json', 'r') as f:
        data = json.load(f)
    assert data == {'bar':'baz'}


def test_find_newest_saved_month(cleandir):
    assert find_newest_saved_month('data', 2010) == (None, None)
    os.mkdir('data')
    assert find_newest_saved_month('data', 2010) == (None, None)
    os.mkdir('data/2009')
    assert find_newest_saved_month('data', 2010) == (None, None)
    dump_to_monthly_json_file('data', 2009, 5, {'foo':'bar'})
    assert find_newest_saved_month('data', 2010) == (None, None)
    assert find_newest_saved_month('data', 2009) == (None, None)
    assert find_newest_saved_month('data', 2008) == (2009, 5)
    dump_to_monthly_json_file('data', 2011, 4, {'foo':'bar'}, 'file')
    assert find_newest_saved_month('data', 2008) == (2009, 5)
    assert find_newest_saved_month('data', 2008, 'file') == (2011, 4)
