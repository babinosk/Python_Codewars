# Inverted values
# 8 kyu
#
# Given a set of numbers, return the additive inverse of each.
# Each positive becomes negatives, and the negatives become positives.
# You can assume that all values are integers. Do not mutate the input array/list.

def invert(lst):
    new_list = []
    for number in lst:
        new_list.append(-1 * number)
    return new_list
    pass
