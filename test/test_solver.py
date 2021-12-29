from solver import *


def test_evaluate_postfix1():
    assert evaluate_postfix(["8", "9", "3", "+", "x", "16", "/"]) == 6


def test_evaluate_postfix2():
    assert evaluate_postfix(["2", "2", "+"]) == 4


def test_shunting_yard():
    assert shunting_yard(["13", "+", "171", "-", "(", "11", "-", "3", ")"]) == \
           ["13", "171", "+", "11", "3", "-", "-"]


def test_solve1():
    assert solve("13 + 171 - ( 11 - 3 )") == 176


def test_solve2():
    assert solve("13 x 17 - ( 11 - 3 )") == 213


def test_solve3():
    assert solve("3 x 5 x 9 / ( 1 + 2 ) / 45") == 1
