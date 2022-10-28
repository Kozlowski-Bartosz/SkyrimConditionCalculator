#!/usr/bin/env python

from sympy import *

#The main function that uses SymPy to reformat the condition expression
def CalculateConditions(es1):
    symb_array = []
    es1 = es1.lower()
    for ch in es1:
        if ch >= 'a' and ch <= 'z':
            if ch not in symb_array:
                symb_array.append(ch)
            

    ns1 = {item : item for item in symbols(symb_array)}
    my_symbols = tuple(ns1.values())

    e1 = sympify(es1, locals=ns1)
    models = satisfiable(e1, all_models=True)
    minterms = list(models)
    return_string = str(POSform(my_symbols, minterms)).upper()
    return return_string

#Translates a string into one similar to how Creation Kit presents it
def TranslateToCreationKit(s):
    s = s.replace(' & ', ' AND\n')
    s = s.replace(' | ', ' OR\n')
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.upper()
    s += (' AND')
    return s

#input_string = input('Enter a boolean expression to process: ')
input_string = '(A & B) | (C & D)'
print('Input: ' + input_string)
reform_string = CalculateConditions(input_string)
print('Boolean Output: ' + reform_string)
print('Creation Kit Output:\n' + TranslateToCreationKit(reform_string))

