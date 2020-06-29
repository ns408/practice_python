#!/usr/bin/env python3

"""
Function play
"""

"""
Power of arbitrary keyword arguments and two ways of supplying them.
"""


def sample_func1(*args):
    print(args)


def sample_func2(**kwargs):
    print(kwargs)


sample_func1(
    "arg1",
    "arg2",
    "arg3",
)

sample_func2(
    kwd1="arg1",
    kwd2="arg2",
    kwd3="arg3",
)

sample_func1()
sample_func2()


"""
give the argument an empty default value and ignore the argument unless
provided a value.
"""


def sample_func3(arg=""):
    print(arg)


sample_func3()
sample_func3(arg="this")
sample_func3("that")
