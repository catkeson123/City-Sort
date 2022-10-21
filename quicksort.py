# Author: Calvin Atkeson
# Date: 11/8/21
# Purpose: Lab 3 quicksort

# compare functions
# takes in two parameters to compare
def compare_func(a,b):
    return a <= b

# partition function
# given parameters
def partition(the_list, p, r, compare_func):
    i = p - 1
    j = p
    pivot = the_list[r]
    while j < r:
        if compare_func(the_list[j], pivot):
            i = i + 1
            (the_list[i], the_list[j]) = (the_list[j], the_list[i])
        j = j + 1
    (the_list[i + 1], the_list[r]) = (the_list[r], the_list[i + 1])
    return i + 1

# quicksort function
# given parameters
def quicksort(the_list, compare_func, p = 0, r = None):
    # base case
    if r is None:
        r = len(the_list) - 1

    # recursion
    if p < r:
        q = partition(the_list, p, r, compare_func)
        quicksort(the_list, compare_func, p, q-1)
        quicksort(the_list, compare_func, q + 1, r)

# sort function
# given parameters
def sort(the_list, compare_func):
    quicksort(the_list, compare_func)








