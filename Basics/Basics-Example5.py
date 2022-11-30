#Write a function that takes in a number that represents hours and converts it to seconds. 
#The function should return the number of seconds.

def hours_to_seconds(hours):
    return( hours *60) * 60
    # fist 60 is for minutes and the second 60 is for seconds! 
    pass


#Could also do this as well!

def hours_to_seconds(hours):
    #defining variables
    seconds = 60
    minutes = 60
    
    return( hours * minutes) * seconds
    