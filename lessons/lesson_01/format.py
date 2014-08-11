#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Lesson 01, String formatting with variable substitution.

#. Using the file `format.py`, create a new variable and assign it a value of
   `24`.

#. Return the `MYSTRING` constant, performing a format operation that will pass
   in the variable created in step #1.
'''

MYSTRING = '{:0>2d} is the number of months I have on my contract.\n It, ' \
    '{:0>2d}, is also the name of my sister\'s favorite TV show.'

MYSTRING = MYSTRING.format(24,24)
