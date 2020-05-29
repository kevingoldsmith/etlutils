"""etlutils root contains utility functions that do not currently have a home
    in any submodules.
"""

import readline
from collections import OrderedDict
import etlutils.date
import etlutils.datafiles  # noqa: F401


def get_interactive_history():
    """Prints all the history from the Python interpreter"""
    print('\n'.join([str(readline.get_history_item(i + 1))
          for i in range(readline.get_current_history_length())]))


def dict_to_ordereddict(unordered_dict):
    """Converts a dict into an OrderedDict object sorrted by key

    gets the keys from the dict, sorts them and then inserts them in order into
    a new OrderedDict object

    Args:
        unordered_dict: the dictionary to sort

    Returns:
        An OrderedDict object with the keys/values from the input in key order

    """
    sorted_keys = sorted(unordered_dict.keys())
    ordered_dict = OrderedDict()
    for key in sorted_keys:
        ordered_dict[key] = unordered_dict[key]
    return ordered_dict
