'''This program served to output a random joke from a defined list every time it runs'''
import random
print("For every time u run this code.You are guranteed a laugh!")
jokes = ['I know they say that money talks, but all mine says is ‘Goodbye.’',
             'I went to buy some camo pants but couldn’t find any.',
             'I failed math so many times at school, I can’t even count.',
             'I used to have a handle on life, but then it broke.',
             'Never trust atoms; they make up everything.']
crack_joke = random.choice(jokes)
print(crack_joke)