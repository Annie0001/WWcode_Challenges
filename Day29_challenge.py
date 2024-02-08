# Create a function that generates a random number between a given range.
import random

def random_num_between_a_and_b(a, b):

    if a <= b:

        return random.randint(a+1,b-1)

print(random_num_between_a_and_b(10,15))


