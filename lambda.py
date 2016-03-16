#!/usr/bin/python

import operator

def get_operator(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' : operator.div,
        '%' : operator.mod,
        '^' : operator.xor,
        }[op]

def calculate(op1, operator, op2):
    op1, op2 = int(op1), int(op2)
    return get_operator(operator)(op1, op2)

print calculate(*("1 + 3".split()))
print calculate(*("1 * 3".split()))
print calculate(*("1 % 3".split()))
print calculate(*("1 ^ 3".split()))