import eautils
from collections import OrderedDict


def test_get_interactive_history():
    eautils.get_interactive_history()


def test_dict_to_ordereddict():
    return_dict = eautils.dict_to_ordereddict( { 'foo': 'qweqw', 'bar': 'qweqwe', 'baz': 'qweqw' } )
    assert list(return_dict.keys()) == [ 'bar', 'baz', 'foo' ]

    return_dict = eautils.dict_to_ordereddict( {} )
    assert len(return_dict) == 0
