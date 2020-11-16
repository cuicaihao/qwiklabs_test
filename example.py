#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
Created on   :2020/11/16 13:29:07
@author      :Caihao (Chris) Cui
@file        :example.py
@content     :xxx xxx xxx
@version     :0.1
@License :   (C)Copyright 2020 MIT
'''

# here put the import lib


def git_operation():
    print("I amm adding example.py file to the remote repository.")


git_operation()


# content of test_sample.py
def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 4
