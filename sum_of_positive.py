# Sum of positive
# 8 kyu
#
# You get an array of numbers, return the sum of all the positives ones.

def positive_sum(arr):
    positives = []
    for number in arr:
        if number >= 0:
            positives.append(number)
    return sum(positives)
