#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""Week 4 - Sort Comparison"""

from timeit import default_timer as timer
import random


def insertion_sort(a_list):
    for index in range(1, len(a_list)):

        current_value = a_list[index]
        position = index

        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1

        a_list[position] = current_value
