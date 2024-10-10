# Name: Akshay
# Period: 5th
# Date: 10/10/2024
    
# define a function isLeapYear() that takes a given year as
# a parameter and returns true if the given year is a leap
# year and false if the given year is not a leap year.

def leapyear(year):

    # check if the year is divisible by 400, or divisible by 4 but not by 100
    if year % 400 == 0:
        return True
    elif year % 4 == 0 and year % 100 != 0:
        return True
    else:
        return false

