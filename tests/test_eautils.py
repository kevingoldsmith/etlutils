import etlutils


def test_get_interactive_history():
    etlutils.get_interactive_history()


def test_dict_to_ordereddict():
    return_dict = etlutils.dict_to_ordereddict({'foo': 'qweqw',
                                                'bar': 'qweqwe',
                                                'baz': 'qweqw'})
    assert list(return_dict.keys()) == ['bar', 'baz', 'foo']

    return_dict = etlutils.dict_to_ordereddict({})
    assert len(return_dict) == 0
