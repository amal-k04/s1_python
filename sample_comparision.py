'''
Author:Amal k philip
Date:25-10-2024
description:comparing of three numbers '''
num_1=int(input("enter the first number:"))
num_2=int(input("enter the second number:"))
num_3=int(input("enter the third number:"))

if num_1>num_2 and num_1>num_3:
    print("the largest number is:",num_1)
elif num_2>num_1 and num_2>num_3:
    print("the largest number is:",num_2)
else:
    print("the largest number is:",num_3)