# Write a program that reads an integer from the user and handles invalid inputs

while True:

    try:
        integer_read = int(input("Please enter an integer number: "))
        print(f"your entered number is {integer_read}")
        break
    
    except:
        print("Wrong input!")

