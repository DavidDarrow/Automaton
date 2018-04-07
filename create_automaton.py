# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 15:12:26 2018

@author: davep
"""


import os
os.chdir('D:\\Documents\\600x\\Automate\\projecttest\\Automaton')
import argparse
import random
from Automaton_class import *



def create_automaton():
    """
    Note: you don't have to put = after the argument on the command line, you 
          can just type: python PATH -a 60 -g 100 -t 0 0 0 1 1 1 0 0
    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--Array_length', type=int, default=50, dest='array_length', 
                        help='Number of cells in array')
    parser.add_argument('-g','--generations', type=int, default=80, dest='generations',
                        help='Number of generations to run cellular automaton')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-r', '--rule', type=int, dest='transition_table', 
                       help='Pre-existing rule from: 30, 54, 60, 102, 110, 158, 182')
    group.add_argument('-t', '--table', nargs=8, type=int, dest='transition_table',
                       help='specify a new transition table. Takes 8 [1 or 0] args')

    
    args = parser.parse_args()
    a = Automaton(args.array_length, args.transition_table)    
    print(a.run(args.generations))    
    
    
    
if __name__ == "__main__":
    create_automaton()
