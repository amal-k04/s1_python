'''
Author:Amal k philip
Date:25-10-2024
description:comparing of three numbers '''
num_1=int(input("enter the first number:"))
num_2=int(input("enter the second number:"))
num_3=int(input("enter the third number:"))
if num_1>num_2:
    if num_1>num_3:
        print("The largest number is",num_1)
    else:
        print("The largest number is",num_3)
elif num_3>num_2:
    print("The largest number is",num_3)
else:
    print("The largest number is",num_2)