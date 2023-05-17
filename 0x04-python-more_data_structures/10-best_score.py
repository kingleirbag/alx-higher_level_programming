#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    max_key = list(a_dictionary.keys())[0]
    maximum_value = a_dictionary[max_key]
    for i, j in a_dictionary.items():
        if j > maximum_value:
            maximum_value = j
            max_key = i
    return max_key
