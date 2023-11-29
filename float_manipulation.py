'''This program served to makes used of some math functions to derive calculations from a list made up of user float inputs'''
import math
import copy
float_list = []
# create list of flaot entries
print('''Hello user!
Help to create a list of 10 numbers by entering any number of your choice each time.
Decimals are also accepted.''')
for i in range(10):
    float_input = float(input("Enter any number:\n"))
    float_list += [float_input]
float_sum = sum(float_list)

# Derive calculations
print(f"Total of entry numbers = {float_sum}")
max_entry = max(float_list)
max_index = float_list.index(max_entry)
print(f"Index position of the maximun entry number = {max_index}")
min_entry = min(float_list)
min_index = float_list.index(min_entry)
print(f"Index position of the minimum entry number = {min_index}")
average_entry = float_sum/len(float_list)
average_entry_rounded = round(average_entry,2)
print(f"Average of the entry numbers = {average_entry_rounded}")
asc_float_list = sorted(float_list)
median_entry = (asc_float_list[5] + asc_float_list[6])/2
print(f"Median of entry numbers = {median_entry}")
