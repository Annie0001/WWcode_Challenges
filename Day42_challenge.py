# Write a program that uses a try-except block to handle division by zero

# try:
#   print("Hello")
# except:
#   print("Something went wrong")

def division_by_zero(n):
    try:
        result = 10 / n
        return result
    
    except:
        print("Give a number greater than zero!")


print(division_by_zero(11)) 
# print(division_by_zero(0))
