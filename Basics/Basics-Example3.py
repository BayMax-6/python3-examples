#Write a function that takes in a number of people and a number of groups. 
#The people will be split up into the groups evenly (there might be left over people). 
#Return the number of people that are left over after creating the even groups.

def left_over(num_people, num_groups):
    return (num_people % num_groups) 
    #just use the mod operator! 
    