#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Lesson 01, Code Analysis

Alter `analyze.py` by minimally changing the file so that the code
returns the following string:

    .. code:: python

        'It was a beautiful day to run ten miles in the park!'.
'''


def english_distance(distance):
    '''
    Returns english distance distance name from integer.

    distance
        An integer distance to be converted to English

    CLI example:

    .. code-block:: python

        english = english_distance(5)
    '''
    distances = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
    }

    if distance in distances:
        english = distances[distance]
    else:
        english = 'too many'

    return english


def running_log(descriptor, distance, location):
    '''
    Returns a statement about today's running.

    descriptor
        An english descriptor about how today felt
    distance
        The distance run (an integer)
    location
        The location of the run

    CLI Example:

    .. code-block:: python

        my_statement = running_log('amazing', 18, 'on the wing of a plane')
    '''
    eng_dist = english_distance(distance)
    return 'It was a {} day to run {} miles {}'.format(descriptor, eng_dist,
                                                       location)

print running_log('rotten', 8, 'on the road.')
