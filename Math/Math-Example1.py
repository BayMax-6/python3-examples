# Write a function that takes in two numbers and returns the difference of those two numbers, 
# always subtracting the smaller from the larger.

def difference(num1, num2):
    if num1 < num2:
        return num2 - num1
    elif num1 == num2:
        return 0
    else:
        return num1 - num2 
    