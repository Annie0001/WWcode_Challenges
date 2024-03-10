# Create a function that checks if a number is a perfect square

# ex. 1 = 1^2 = 1*1
# ex. 4 = 2^2 = 2*2
# ex. 9 = 3^2 = 3*3
# ex. 16 = 4^2 = 

import math

def find_perfect_square_number(number):
        
        if number < 0:
            print("Please enter a positive number.")
            return
        if type(number) == float:
            print("Please enter a number with no decimal point.")
            return
        square_root_reault = math.sqrt(number)
        if square_root_reault ** 2 == number :
            print("Your number is a Perfect square!")

        else:
            print("Please enter another number. Your number is not a Perfect Square!")

#find_perfect_square_number(9)
# find_perfect_square_number(2)
#find_perfect_square_number(16)
#find_perfect_square_number(0)
#find_perfect_square_number(5)
#find_perfect_square_number(81)
#find_perfect_square_number(15)
#find_perfect_square_number(-9)
find_perfect_square_number(16.2)
