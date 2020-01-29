import random


def print_hello(text):
    print(text)


#print('Hello World')
#print('What a beautiful day')

my_rand: int = random.randint(1, 6)
print_hello(f'this is my number: {str(my_rand)}')
