#!/usr/bin/python3


def best_score(a_dictionary):
    """
    A func that returns a key w the biggets integer value
    """
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        score = 0
        leader = ""
        for i in my_list:
            if a_dictionary[i] > score:
                score = a_dictionary[i]
                leader = i
        return leader
           
