# Write a function to find the largest common divisor of two numbers using a function

def largest_common_divisor_of_two_numbers(num1, num2):
        # for to the lowest number between the 2 given numbers
        smaller_number = 0
        divisor = 0
        if num1 <num2:
            smaller_number = num1
        else:
            smaller_number = num2
        for i in range (2,smaller_number+1):
        # divide each of the numbers by that number and check if the remainder is zero for both of them
            if num1 % i == 0 and num2 % i == 0:
        # save the number that gives the remainder zero in somewhere
                divisor = i 
        # if one of the given numbers is divisable by a number then just continue the loop
        return divisor

print(largest_common_divisor_of_two_numbers(12,15))
#print(largest_common_divisor_of_two_numbers(6,18))