# Write a test case for a function that checks if a number is prime

def prime_number(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                print("It is not a prime number.")
                return
        print("It's a prime number")
    else:
        print("It's not a prime number")
        
        


# prime_number(5)
# prime_number(7)
#prime_number(6)
prime_number(1)