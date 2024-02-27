# Write a function to check if a number is a prime number
# dividing the number starting from 2 to n
# To check if the remainder of any division is zero then the number is not prime

def check_prime_number(n):

    for i in range(2,n):
        if n % i == 0:
            print("It's not a prime")
            return
    print("The number is prime.")



# check_prime_number(5)
# check_prime_number(15)
check_prime_number(4)
