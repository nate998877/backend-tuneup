#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "nateTheNotSoGreat"

import cProfile
from timeit import Timer
import pstats
import functools


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    # You need to understand how decorators are constructed and used.
    # Be sure to review the lesson material on decorators, they are used
    # extensively in Django and Flask.
    def cProf(*args, **kwargs):
        profile = cProfile.Profile()
        retval = profile.runcall(func, *args, **kwargs)
        profile.print_stats()
        ps.print_stats()
        return retval
    # raise NotImplementedError("Complete this decorator function")
    return cProf


def read_movies(src):
    """Returns a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """returns True if title is within movies list"""
    if movies[0].lower() == title.lower():
        return True
    return False



# @profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = sorted(read_movies(src))
    duplicates = []
    while movies:
        movie = movies.pop(0)
        if movies and is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper(command):
    """Part A:  Obtain some profiling measurements using timeit"""
    # YOUR CODE GOES HERE
    total_runs = 10
    repeats = 10
    t = Timer(lambda: command('movies.txt')).repeat(repeats,total_runs)
    fin = min(t)/total_runs
    print("Best time across {} repeats of {} runs per repeat: {} sec".format(repeats, total_runs, fin))

def main():
    """Computes a list of duplicate movie entries"""
    timeit_helper(find_duplicate_movies)
    result = find_duplicate_movies('movies.txt')
    print('Found {} duplicate movies:'.format(len(result)))
    print('\n'.join(result))


if __name__ == '__main__':
    main()
