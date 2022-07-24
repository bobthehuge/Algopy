# -*- coding: utf-8 -*-
"""
Created on May. 2022
@author: BobTheHuge

Helps to test functions on random lists.
"""
from random import randint


def random_list(n, maxVal):
    """
    build a list with n random values in [0, maxVal]
    """
    l = []
    for i in range(n):
        l.append(randint(0, maxVal))
    return l


def random_sorted_list(n, step):
    """
    build a sorted list with n natural integers
    step is the maximum difference between values
    """
    l = [0]
    for i in range(1, n):
        l.append(l[i - 1] + randint(0, step))
    return l
