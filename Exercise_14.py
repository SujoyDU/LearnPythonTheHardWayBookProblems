'''
Let’s do one exercise that uses argv and input together to ask the user
something specific. In this exercise we’ll use input slightly differently by
having it print a simple > prompt. This is similar to a game like Zork or
Adventure.

'''

from sys import argv
prog = argv
x = input()
print(x)
print('{} takes input {}'.format(prog,x))