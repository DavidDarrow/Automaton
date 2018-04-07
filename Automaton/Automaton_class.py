# -*- coding: utf-8 -*-
"""
Created on Sat Feb 17 00:09:12 2018

@author: davep
"""

from rules import rule


def wrap_index(L, index):
    length = len(L)
    try:
        return L[index]
    except IndexError:
        if index > 0:
            return wrap_index(L, index-length)
        else:
            return wrap_index(L, index+length)

def t_table(*table):
    try:
        if len(table) != 8:
            raise ValueError
        for i in table:
            if i not in (1, 0):
                raise TypeError
        string_table = [str(i) for i in table]
        keys = [bin(i)[2:].zfill(3) for i in range(len(table))][::-1] 
        return dict(zip(keys, string_table))

    except ValueError:
        print('Invalid Table: Transition Table must contain 8 integers')
    except TypeError:
        print('Invalid table: Table can only contain ints: 1 or 0')


class Automaton(object):
    def __init__(self, array_length=40, transition_table=None):
        self.array_length = array_length
        self.state = None
        self.translate_clean = str.maketrans('10', '# ')
        if type(transition_table) == dict:
            self.table = transition_table
        elif type(transition_table) == int:
            self.table = rule[transition_table]
        else:
            try:
                self.table = t_table(*transition_table)
            except:
                print('invalid table')
        
        self.initialize()

    def initialize(self, mode=None):
        if mode == 'random':
            import random
            self.state = ''.join([random.choice('10') for i in range(self.array_length)])
        else:
            self.state = ''.join([str(0) for i in range((self.array_length-1)//2)]) + '1' + ''.join([str(0) for i in range(self.array_length//2)])

    def display(self):
        if self.state:
            return self.state
        else:
            print('Not initialized')

    def get_index(self, index):
        return wrap_index(self.state, index)

    def neighborhood(self, index):
        return self.get_index(index-1) + self.get_index(index) + self.get_index(index+1)

    def get_next_gen(self):
        return ''.join([self.table[self.neighborhood(i)] for i in range(self.array_length)])
        
    def mutate(self):
        self.state = self.get_next_gen()
        
    def run(self, generations=80):
        for i in range(generations):
            print(self.state)
            self.mutate()
    
    def run_trans(self, generations=80):
        for i in range(generations):
            print(self.state.translate(self.translate_clean))
            self.mutate()
            
#    def run_live(self):
#        display = []
#        for i in range(50):
#            display.append(self.state)
#            self.mutate()
#        try:
#            while True:
#                printOut = '\n'.join(display)
#                print(printOut)
#                del display[0]
#                self.mutate()
#                display.append(self.state)
#                print('\b' * len(printOut), end='', flush=True)
#        except KeyboardInterrupt:
#            print('terminated')





