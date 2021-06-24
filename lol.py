#1: Make a function to calculate the average of an array of numbers--they may not all be integers

# 1 point
def calc_avg(arr):
    if checkType(arr) == "string":
        print("can't calculate average")
    else:
        print(sum(arr) / len(arr))
def checkType(a_list):
    for element in a_list:
        if isinstance(element, int):
            break
        if isinstance(element, str):
            return("string")
        if isinstance(element, float):
            break

calc_avg([5, 4, 3, 2,1])
calc_avg([3.25, 5, 4.5, 10])
calc_avg(["lol", 4, 5]) # +2

#2: Cedric is trying to plan his upcoming vacations with his future kids and grandkids. Create a program that prints the next 20 leap years.
def calc_leap_years(yr, num=20):
    list_of_leap_years = []
    count=0
    while count < num:
        if yr % 4 == 0:
            if yr % 100 != 0 or yr % 400 == 0:
                list_of_leap_years.append(yr)
                count += 1
        yr += 1
    print(list_of_leap_years)
        
# def is_leap(year):
#      return (year%4 == 0 and year%100 != 0) or (year % 400 == 0)
# def calc_leap_years(year, counts=20):
#      cnt = 0
#      leaps = []
#      while cnt != counts:
#          if is_leap(year):
#              leaps.append(year)
#              cnt += 1
#          year += 1
#      print(leaps)

# for i, years in enumerate( calc_leap_years(1690, 15), 1 ):
#     print(i, years)
calc_leap_years(2020)
calc_leap_years(2012)
calc_leap_years(2050)

# 3. Cedric likes to play with numbers. Sometimes he is given a string containing numbers and characters, which he does not like. Write a function to help Cedric play with numbers that takes in a string and computes the sum of the integers embedded in the string. 
def findSum(str1):
    # A temporary string
    temp = "0"
    # holds sum of all numbers
    # present in the str1ing
    Sum = 0
    # read each character in input string
    for ch in str1:
        # if current character is a digit
        if (ch.isdigit()):
            temp += ch
        # if current character is an alphabet
        else:
            # increment Sum by number found
            # earlier(if any)
            Sum += int(temp)
 
            # reset temporary str1ing to empty
            temp = "0"
 
    # atoi(temp.c_str1()) takes care
    # of trailing numbers
    return Sum + int(temp)
# input alphanumeric string
str1 = "12abc20yz68"
str2 = "24!defgh?50"
str3 = "-40zyxq40"

import re
def findSumNeg(str1):
    result = [int(d) for d in re.findall(r'-?\d+', str1)]
    return sum(result)
 
# Function call
print(findSum(str1)) #100
print(findSum(str2)) #74
print(findSumNeg(str1)) #100
print(findSumNeg(str3))  #0

# 4.
def division(num1, num2):
     
    if (num1 == 0): return 0
    if (num2 == 0): return INT_MAX
     
    negResult = 0
     
    # Handling negative numbers
    if (num1 < 0):
        num1 = - num1
         
        if (num2 < 0):
            num2 = - num2
        else:
            negResult = true
                 
    elif (num2 < 0):
        num2 = - num2
        negResult = true
     
    # if num1 is greater than equal to num2
    # subtract num2 from num1 and increase
    # quotient by one.
    quotient = 0
 
    while (num1 >= num2):
        num1 = num1 - num2
        quotient += 1
     
    # checking if neg equals to 1 then
    # making quotient negative
    if (negResult):
            quotient = - quotient
    return quotient
 
# Driver program
num1 = 13; num2 = 2
print(division(num1, num2)) #6
print(division(100, 2.5)) #40
 