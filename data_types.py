# Data Types in Python

"""
The quantitative (numerical) variable type

can be further divided into two types:
1. Discrete - can take on only a finite number of values(e.g. only positive inter)
 - 학생수, 사건수, 사용자 수
2. Continuous - can take on any value within a range
 -  몸무게, 키, 온도, 시간
"""

import numpy as np

# Integer
type(4) # <class 'int'>
type(4.) # <class 'float'>
type(0) # <class 'int'>
type(-4) # <class 'int'>

# Float
type(3/5) # =0.6 <class 'float'>
type(6*10**(-1)) # =60^-1 <class 'float'> / ** means exponentiation
type(3//5) # =0 <class 'int'> / // means floor division
type(np.pi) # <class 'float'>

"""
The categorical variable type

can be further divided into two types:
1. Nominal - can take on only a finite number of values(e.g. only positive inter)
 - 성별, races, 결혼여부(marital)
2. Ordinal - can take on any value within a range(need inherent order)
 - 성적, 학년 
"""

# Boolean
type(True) # <class 'bool'>
print(6 < 5) # False
print(6 > 5) # True
print(type(6 < 5)) # <class 'bool'>

""" Boolean expressions are often used in "if blocks" to control program flow"""

if 6 < 5 :
    print("Yes!")

""" Square brackets [...] create a literal list. """

myList = [True, 6<5, 1==3, None is None]
print(myList) # [True, False, False, True]
for element in myList:
    print(type(element)) # <class 'bool'> <class 'bool'> <class 'bool'> <class 'bool'>

# String
""" A String is a single "text" value of arbitary length."""
type("Hello, World!") # <class 'str'>
print("""This sentence makes
sense""") # This sentence makes sense

type("np.pi") # <class 'str'>
x = np.asarray (['dog', 'cat', 'bird'])
# x.mean() is not allowed.

# Lists

"""A list can hold values (possibly of defferent types) in sequence."""

myList = [1, 1.1, "String", None]
for element in myList:
    print(type(element)) # <class 'int'> <class 'float'> <class 'str'> <class 'NoneType'>

myList = [1, 2, 3]
for element in myList:
    print(type(element))
sum(myList)/len(myList) # note that this outputs a float

