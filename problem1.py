#
# Name: Ahmed Kamran
# Collaborator(s): none
#

'''
    DESCRIPTION: 
    Write a short program that asks for a number of seconds (as an integer), 
    converts that value to a number of seconds, minutes, hours, and days, 
    then prints the equivalent seconds, minutes, hours, and days. 
'''
numSec = int(input("How many seconds? "))
days, numSec = divmod(numSec,60*60*24) # Days and remaining seconds
hours, numSec = divmod(numSec, 60*60) # Hours and remaining seconds
minutes, numSec = divmod(numSec, 60) # Minutes and remaining seconds
seconds = numSec # Remaining seconds

print(F"{numSec} seconds is equivalent to {days} {'days' if (days>1) else 'day'}, {hours} {'hours' if (hours>1) else 'hour'}, {minutes} {'minutes' if (minutes>1) else 'minute'}, and {seconds} {'seconds' if (seconds>1) else 'second'}.")
