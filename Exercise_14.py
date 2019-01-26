'''
Let’s do one exercise that uses argv and input together to ask the user
something specific. In this exercise we’ll use input slightly differently by
having it print a simple > prompt. This is similar to a game like Zork or
Adventure.

'''

from sys import argv

# prog = argv
# x = input()
# print(x)
# print('{} takes input {}'.format(prog,x))

prog, user_name = argv
prompt = '> '
firstLine = 'Hello {}!! Welcome to my hub at {}'
print(firstLine.format(user_name, prog))
print('Please answer the questions below')
print('Your Full Name: ')
fullName = input(prompt)
print('Where do you live?')
location = input(prompt)
print('Who is your spouse?')
spouseName = input(prompt)
print('What programming language are you using?')
lang = input(prompt)

print(
'''Message from {}
Hi {}. Your full name is {}. 
You live in {}.
Your spouse is {}. 
You are using {} as the programming language
'''.format(prog,user_name,fullName,location,spouseName,lang)
)