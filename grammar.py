#!/usr/bin/python
# Basic calculator using Grammar and STransformer

import operator as op
from plyplus import Grammar, STransformer

class Calculator(STransformer):
    def operator(self, exp):
        first, operator_symbol, second = exp.tail
        operator_func = { '+': op.add, '-': op.sub, '*': op.mul, '/': op.div }[operator_symbol]

        return operator_func(first, second)

    number      = lambda self, exp: float(exp.tail[0])
    neg         = lambda self, exp: -exp.tail[0]
    __default__ = lambda self, exp: exp.tail[0]

    add = operator
    mul = operator

grammar = Grammar("""
    start: add;
    ?add: (add add_symbol)? mul;
    ?mul: (mul mul_symbol)? atom;
    @atom: neg | number | '\(' add '\)';
    neg: '-' atom;
    number: '[\d.]+';
    mul_symbol: '\*' | '/';
    add_symbol: '\+' | '-';
    WS: '[ \t]+' (%ignore);
""")
calc = Calculator()

while True:
    try:
        s = raw_input('> ')
    except EOFError:
        break
        
    if s == '':
        break

    tree = grammar.parse(s)
    print(calc.transform(tree))