===============================
1. Print sorted module
===============================

Import module:
==============
    >>> MyList = __import__('1-my_list').MyList


Function:
=========
Write a class MyList that inherits from list:

    * You can assume that all the elements of the list will be of type int

Section // No exceptions
=========================

Test case #0: A test case to order a disordered list of positive integers

    >>> my_list = MyList()
    >>> my_list.append(1)
    >>> my_list.append(4)
    >>> my_list.append(2)
    >>> my_list.append(3)
    >>> my_list.append(5)
    >>> print(my_list)
    [1, 4, 2, 3, 5]

    >>> my_list.print_sorted()
    [1, 2, 3, 4, 5]

    >>> print(my_list)
    [1, 4, 2, 3, 5]

Test case #1: A test case to order a disordered list of positive integers

    >>> my_list = MyList()
    >>> my_list.append(5)
    >>> my_list.append(4)
    >>> my_list.append(3)
    >>> my_list.append(2)
    >>> my_list.append(1)
    >>> print(my_list)
    [5, 4, 3, 2, 1]

    >>> my_list.print_sorted()
    [1, 2, 3, 4, 5]

    >>> print(my_list)
    [5, 4, 3, 2, 1]

Test case #2: A test case for a empty list

    >>> my_list = MyList()
    >>> print(my_list)
    []

    >>> my_list.print_sorted()
    []

    >>> print(my_list)
    []

Test case #3: A test case for do nothing

    >>> my_list = MyList()
    >>> my_list.append(-5)
    >>> my_list.append(-4)
    >>> my_list.append(-3)
    >>> my_list.append(-2)
    >>> my_list.append(-1)
    >>> print(my_list)
    [-5, -4, -3, -2, -1]

    >>> my_list.print_sorted()
    [-5, -4, -3, -2, -1]

    >>> print(my_list)
    [-5, -4, -3, -2, -1]

Test case #4: A test case to order a disordered list of negative integers

    >>> my_list = MyList()
    >>> my_list.append(-1)
    >>> my_list.append(-4)
    >>> my_list.append(-2)
    >>> my_list.append(-3)
    >>> my_list.append(-5)
    >>> print(my_list)
    [-1, -4, -2, -3, -5]

    >>> my_list.print_sorted()
    [-5, -4, -3, -2, -1]

    >>> print(my_list)
    [-1, -4, -2, -3, -5]


Section // Attribute Errors
============================

Test case #5: A invalid test case of tuples

    >>> my_list = (1, 2)
    >>> print(my_list)
    (1, 2)
    
    >>> my_list.print_sorted()
    Traceback (most recent call last):
    AttributeError: 'tuple' object has no attribute 'print_sorted'

    >>> print(my_list)
    (1, 2)
