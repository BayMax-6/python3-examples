# Write a function that takes in a number and either a + or a -. 
# The function should return the consecutive number either before (-) or after (+) the number.

def consecutive_number(number, symbol):
    if symbol == '+':
        return number +1
    else:
        return number -1

# we could check for junk symbols here of have that as the else condition, but this is enough to slove the current problem! 