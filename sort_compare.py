#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Week 4 - Sort Comparison"""

from timeit import default_timer as timer
import random


def insertion_sort(a_list):
    start = timer()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    end = timer()
    return (end - start)


def shell_sort(a_list):
    start = timer()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end = timer()
    return (end - start)


def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
        a_list[position] = current_value


def python_sort(a_list):
    start = timer()
    a_list.sort()
    end = timer()
    return (end - start)


def random_int_list(n):
    new_list = range(n)
    random.shuffle(new_list)
    return new_list


def check_sort_averages(test_input):

    # Initializing variables
    insertion_avg = 0
    shell_avg = 0
    python_avg = 0

    # Running each search method on each list sequentially
    for random_list in test_input:
        insertion_avg += insertion_sort(random_list)
        shell_avg += shell_sort(random_list)
        python_avg += python_sort(random_list)

    print '''
    Insertion Sort took {:.7f} seconds to run, on average.
    Shell Sort took {:.7f} seconds to run, on average.
    Python Sort took {:.7f} seconds to run, on average.
    '''.format(
        (insertion_avg / len(test_input)),
        (shell_avg / len(test_input)),
        (python_avg / len(test_input))
    )


def main():

    # Generating various test inputs
    test_input_a = [random_int_list(500) for _ in range(100)]
    test_input_b = [random_int_list(1000) for _ in range(100)]
    test_input_c = [random_int_list(10000) for _ in range(100)]

    print 'Input A, Size of Lists: 500'
    check_sort_averages(test_input_a)
    print 'Input B, Size of Lists: 1,000'
    check_sort_averages(test_input_b)
    print 'Input C, Size of Lists: 10,000'
    check_sort_averages(test_input_c)


if __name__ == '__main__':
    main()
