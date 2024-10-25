temp=int(input("enter the temperature:"))
te_co=input("Is this in (C)celsius or (F)fahrenheit?")
if te_co=="C":
    f=(9/5*temp)+32
    print(temp,"Celsius is",f," Fahrenheit.")
elif(te_co=="F"):
    c= 5/9*(temp-32)
    print(temp,"Fahrenheit is",c,"Celsius.")