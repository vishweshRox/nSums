#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 20:35:31 2024

@author: vishweshpalani
"""

import numpy as np
from fraction import Fraction

class Polynomial:
    """
    NOTE:
        -> Constructor may accept a Polynomial, NumPy Array, List or Number. 
        -> Empty iterables will be replaced with an object of an equivalent type holding the number 0, for ease of computation.
    """
    
    def __init__(self, ipt=[]):
        #arr is the coefficient array describing the polynomial.
        if isinstance(ipt, Polynomial):
            #Creates a copy of an existing polynomial.
            ipt = ipt.getArr()
        elif type(ipt) == np.ndarray:
            if ipt.size == 0:
                ipt += np.array([Fraction(0)])
            ipt = np.array([n if isinstance(n, Fraction) else Fraction(float(n)) for n in ipt])
        elif type(ipt) == list:
            if len(ipt) == 0:
                ipt = [0]
            ipt = np.array([Fraction(n) for n in ipt])
        elif type(ipt) == int:
            ipt = np.array([Fraction(ipt)])
        else:
            raise TypeError('Constructor must be a Polynomial, NumPy Array, List or Number.')
        self.coef = np.array(ipt)
        self.dim = self.coef.size - 1
        
        
    def __getitem__(self, idx):
        return self.coef[idx]
        
    def __setitem__(self, n, coef):
        self.coef[n] = coef
        
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index <= self.dim:
            coef = self[self.index]
            self.index += 1
            return coef
        raise StopIteration
    
    def __repr__(self):
        p_str = ''
        first = True
        for i in reversed(list(range(self.coef.size))):
            if self[i] != 0 or i == 0:
                p_str += ('+ ' if not first else '') + str(self[i]) + (f' * x^{str(i)} ' if i != 0 else '')
                first = False
            
        return p_str
    
    def getArr(self):
        return self.coef
    
    def getDim(self):
        return self.dim
    
    def _expand(self, n):
        #NOTE: Expansion will not affect the original array.
        k = n - self.dim
        exp_cpy = np.append(self.coef, np.zeros(k))
        return Polynomial(exp_cpy)
    
    """
    NOTE: Arithmetic operations accept constants and Polynomials only.
    """
        
    def __add__(self, P2):
        if not isinstance(P2, Polynomial):
            P2 = Polynomial([P2])
        if P2.getDim() < self.dim:
            return P2 + self
        else:
            return Polynomial(self._expand(P2.getDim()).getArr() + P2.getArr())
        
    def __sub__(self, P2):
        return self + (P2 * -1)
        
    def __mul__(self, P2):
        if type(P2) in [int, float, Fraction]:
            #Wraps it with a Polynomial object.
            P2 = Polynomial([P2])
        elif P2.getDim() < 0:
            P2 += Polynomial([0])
        product = Polynomial([])
        s1, s2 = self.dim + 1, P2.getDim() + 1
        for i in range(s2):
            temp = {}
            p_e = P2[i]
            for j in range(s1):
                temp[i+j] = self[j] * p_e #Single pass per element.
            new_p = Polynomial(np.zeros(max(temp.keys())+1))
            for k in temp:
                new_p[k] = temp[k]
            product += new_p
        return product
    
    def __rmul__(self, P2):
        return self * P2
    
    def compute(self, x):
        val = 0
        for i in range(self.dim + 1):
            val += self[i] * x ** i
        return val
    
if __name__ == '__main__':
    r1 = Polynomial(7) * Polynomial([2.3, 5.6])
    print(r1.compute(7))
    

        
    

        
    



