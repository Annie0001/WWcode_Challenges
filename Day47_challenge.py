# Create a program that imports the math module and uses its functions

import math

def addition(num1, num2):
    results= math.fsum([num1, num2])
    return results

print(addition(3, 5))