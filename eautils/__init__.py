import readline
from collections import OrderedDict
import eautils.date
import eautils.datafiles


def get_interactive_history():
    print('\n'.join([str(readline.get_history_item(i + 1)) for i in range(readline.get_current_history_length())]))


def dict_to_ordereddict(unordered_dict):
    sorted_keys = sorted(unordered_dict.keys())
    ordered_dict = OrderedDict()
    for key in sorted_keys:
        ordered_dict[key] = unordered_dict[key]
    return ordered_dict
