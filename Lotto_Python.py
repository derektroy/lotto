"""
#
# File          :   Lotto_Python.py
# Created       :    
# Author        :   Derek Troy
# Version       :   1.0.0
# Licensing     :   (C) 2021 Derek Troy LYIT
#                   Available under GNU Public License (GPL)
# Description   :
#
"""
import random

myList = [random.randint(1, 20) for _ in range(6)] # A random number generator for a list of 6 numbers between 1 and 20, outputted to myList

ten_list = ["Tom", "Ivan", "Philly", "Seamus", "Mags", "Eileen", "Dave", "Biddy", "John", "James"] #A named list with 10 Lottery Players

print(myList)
print(ten_list)
print("P")