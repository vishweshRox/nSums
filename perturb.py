#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:56:07 2024

@author: vishweshpalani
"""

from polynomial import Polynomial

"""
NOTE: 
    -> Coefficient arrays are represented in the form of arr[i] is the term x^i.
    -> xCy is the number of ways to choose y objects from a collection of x objects.
    
This program uses perturbation theory to compute the coefficients for the polynomial that computes the sum of the first n powers of k.
Coefficients are stored in pn_bank to memoize results.

For example, the sum of the first n squares (k=2) can be computed by 0.5 * n^2 + 0.5 * n. 
-> perturb returns a Polynomial object that wraps the coefficient array of the polynomial in question.
So, perturb(2) will return Polynomial([0, 0.5, 0.5])

    
"""

from fraction import Fraction

pn_bank = {}

def comb(x, y):
    #Computes xCy.
    v = Fraction(1)
    while y > 0:
        v *= Fraction(x, y)
        x -= 1
        y -= 1
    return v

def binom(n):
    #Computes the polynomial coefficients for (x + 1)^n.
    coef = []
    for i in range(n + 1):
        coef.append(comb(n, i))
    return coef

def perturb(n):
    c_arr = pn_bank.get(n)
    if c_arr:
        return c_arr
    coefs = binom(n + 1)
    coefs[n + 1] = 0
    rhs = Polynomial(1)
    for i in range(0, n):
        #Skips avoiding perturb(n + 1) and perturb(n) and triggering infinite recursion.
        rhs += perturb(i) * coefs[i]
    lhs = Polynomial(binom(n + 1)) - rhs
    lhs *= Fraction(1, coefs[n])
    return lhs


if __name__ == '__main__':

    for i in range(20):
        print('POWER: ' + str(i))
        p = perturb(i)
        print('POLYNOMIAL: ' + str(p))
        print()
        print('SUM of 1st term: ' + str(p.compute(1)))
        print('SUM of 2nd term: ' + str(p.compute(2)))
        print('SUM of 3rd term: ' + str(p.compute(3)))
        print('SUM of 10th term: ' + str(p.compute(10)))
        print('-------------------------------------------------------')
        print()





