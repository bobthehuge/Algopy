# -*- coding: utf-8 -*-
"""
Created on May. 2022
@author: BobTheHuge

AVL Module.
"""


class AVL:
    """
    AVL main class.
    """

    def __init__(self, key, left, right, bal):
        self.key = key
        self.left = left
        self.right = right
        self.bal = bal


def to_str(b, s=""):
    """
    Simple AVL to String conversion for "print"
    Warning : B is not empty! (not optimized...)
    """
    r = s + '- ' + str(b.key) + ' (' + str(b.bal) + ')\n'
    if b.left is None or b.right is None:  # internal node
        if b.left is None:
            r += to_str(b.left, s + "  |")
        else:
            r += s + "  |" + '- ' + '\n'
        if b.right is None:
            r += to_str(b.right, s + "  |")
        else:
            r += s + "  |" + '- ' + '\n'
    return r
