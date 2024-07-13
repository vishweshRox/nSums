#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 20:56:13 2024

@author: vishweshpalani
"""

import math as m

class Fraction:
    def __init__(self, num, denom=1):
        
        if type(num) == float:
            num = floatToFraction(num)
        if type(denom) == float:
            denom = floatToFraction(denom)
        
        #num, denom must be of type int or Fraction
        
        if type(num) == int and type(denom) == int:   
        
            #catches zero divison
            if denom == 0:
                raise ZeroDivisionError()
                
            gcd = m.gcd(num, denom)
            
            #always in simplest form
            self.num = num // gcd
            self.denom = denom // gcd
            
        elif type(num) in [int, Fraction] and type(denom) in [int, Fraction]:
            
            #catches zero division
            if type(denom) == int:
                if denom == 0:
                    raise ZeroDivisionError()
            else:
                if denom.getNum() == 0:
                    raise ZeroDivisionError()
        
            new_f = num / denom
            self.num = new_f.getNum()
            self.denom = new_f.getDenom()
            
        else:
            raise TypeError('Constructor must receive inputs of type int, float or Fraction.')
            
        #sign-correction
        if self.num * self.denom > 0:
            self.num, self.denom = abs(self.num), abs(self.denom)
        else:
            self.num, self.denom = -1 * abs(self.num), abs(self.denom)
        
            
    def __repr__(self):
        if self.denom == 1:
            return f'{self.num}'
        return f'( {self.num} / {self.denom} )'
    
    def getNum(self):
        return self.num
    
    def getDenom(self):
        return self.denom
    
    def inverse(self):
        return Fraction(self.denom, self.num)
    
    def __add__(self, o_f):
        if type(o_f) == int:
            o_f = Fraction(o_f)
        return Fraction(self.num * o_f.getDenom() + self.denom * o_f.getNum(), self.denom * o_f.getDenom())
    
    def __radd__(self, o_f):
        return self + o_f
        
    def __sub__(self, o_f):
        return self + (o_f * -1)
    
    def __rsub__(self, o_f):
        return (self - o_f) * -1
    
    def __mul__(self, o_f):
        if type(o_f) == int:
            o_f = Fraction(o_f)
        return Fraction(self.num * o_f.getNum(), self.denom * o_f.getDenom())
    
    def __rmul__(self, o_f):
        return self * o_f
    
    def __truediv__(self, o_f):
        #define for operations between numbers and fractions
        if type(o_f) == int:
            o_f = Fraction(o_f)
        return self * o_f.inverse()
    
    def __rtruediv__(self, o_f):
        return Fraction(o_f) * self.inverse()
    
def floatToFraction(x):
    #only converts non-recurring decimals, CANNOT handle recurring decimals e.g. 0.333333
    d = 1
    while x % 1 != 0:
        x *= 10
        d *= 10
    return Fraction(int(x), int(d))
    

if __name__ == '__main__':
    n = 26.62986413
    f1 = Fraction(n)
    print(f1)
        