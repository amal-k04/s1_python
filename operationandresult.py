'''
Author:Amal k philip
Date:18-10-2024
description:arithmetic, comparison, and logical operators.'''
num_1=int(input("enter the number1 :"))
num_2=int(input("enter the number2 :"))
sum=num_1+num_2
div=num_1/num_2
print("sum:",sum,",division",div)
print("Is number1 greater than number2?:",num_1>num_2)
print('Is number1 and number2 are equal?:',num_1==num_2)
print('logical AND:',(num_1>0) and (num_2>0))
print("logical OR:",(num_1>0 or num_2>0))