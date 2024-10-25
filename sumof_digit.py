num=int(input("enter your number:"))
sum=0
while num>0:
    reminder=num%10
    sum=sum+reminder
    num=num//10
print("sum of digits of the number:",sum)