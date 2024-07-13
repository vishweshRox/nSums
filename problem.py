#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 15:09:56 2024

@author: vishweshpalani
"""

'''
WHY THE PREVIOUS CODE DIDN'T WORK.
'''
num = 10**18 + 1
gcd = 1
result_float_div = int(num / gcd)  # Might not be exactly 10**18 + 1 due to floating-point precision issues
result_int_div = num // gcd        # Will be exactly 10**18 + 1

print(result_float_div)  # Could potentially print an inaccurate result
print(result_int_div)    # Will print the correct result