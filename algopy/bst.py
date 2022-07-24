# -*- coding: utf-8 -*-
"""
Created on May. 2022
Last edit on Jul. 2022
@author: BobTheHuge

Simple binary search tree implementation
"""

from algopy import bintree


class Bst:
    """
    Binary search tree main class
    """

    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right


def find_min(b: Bst):
    if b.left is None:
        return b.key

    return find_min(b.left)


def find_max(b: Bst):
    if b.right is None:
        return b.key

    return find_max(b.right)


def search(b: Bst, value):
    if b is None or b.key == value:
        return b

    if b.key < value:
        return search(b.right, value)

    return search(b.left, value)


def insert_leaf(b: Bst, value):
    if b is None:
        b = bintree.BinTree(value, None, None)
        return b

    if b.key is None:
        b.key = value
        return b

    if b.key == value:
        return b

    if b.key < value:
        b.right = insert_leaf(b.right, value)
    else:
        b.left = insert_leaf(b.left, value)

    return b


def cut(b: Bst, value):
    """
    Sub function of insert_root
    _> determines new left and right child
    """

    if b is None:
        return None, None

    if b.key <= value:
        l, r = cut(b.right, value)
        b.right = l
        return b, r

    else:
        l, r = cut(b.left, value)
        b.left = r
        return l, b


def insert_root(b: Bst, value):
    if b is None or b.key is None:
        return bintree.BinTree(value, None, None)

    l, r = cut(b, value)
    return bintree.BinTree(value, l, r)


def delete(b: Bst, value):
    if b is None or b.key is None:
        return None

    if b.key == value:
        if b.right is None or b.left is None:
            if b.right is None:
                return b.left
            return b.right

        b.key = find_max(b.left)
        b.left = delete(b.left, b.key)

    elif value < b.key:
        b.left = delete(b.left, value)

    else:
        b.right = delete(b.right, value)

    return b
