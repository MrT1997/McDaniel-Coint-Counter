# Tanner McDaniel
# COMP141 Fall 2015
# Assignment 3
# 23 September, 2015

# Tell the user what he or she is about to do
print('Welcome to \"The Coin Counting Game!\" of coins to equal one dollar ($1.00).')
print('All you have to do is get your total number')
print("Not too hard, right?")
print("-----------------------------------------------------------------------")

# ask user for amount of coins
num_pennies = int(input("How many pennies do you have? "))
num_nickels = int(input("How many nickels do you have? "))
num_dimes = int(input("How many dimes do you have? "))
num_quarters = int(input("How many quarters do you have? "))

# get individual coin value
penny_value = 0.01
nickel_value = 0.05
dime_value = 0.10
quarter_value = 0.25

# calculate total value
total_value = ((num_pennies * penny_value) + (num_nickels * nickel_value) + (num_dimes * dime_value) + (num_quarters * quarter_value))

if total_value == 1.00:
    print('Your total is $', \
          format(total_value, '.2f'), \
          sep='')
else:
    print('Sorry! Your total is $', \
          format(total_value, '.2f'), \
          sep='')

