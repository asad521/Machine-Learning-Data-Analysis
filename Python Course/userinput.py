# How to take input as string from user. Default input is string
# user=input("Enter your name: \n")
# print("Your name is: "+ user)
# num1=input("Enter first number ")
# num2=input("Enter second number")
# print(num1+num2)  #This is concatination of two string .No addition of two number.
# # To add, Your must need to convert input to integer or float.
# num1=int(input("Enter first number "))
# num2=int(input("Enter second number"))
# total=num1+num2
# print("Your total is "+ str(total))
#+++++ Data Conversion+++++#
# str(variable)
# float(variable)
# int(variable)
#float and int can be added together without conversion. Output will be in float
#+++++++++++++++++Take Multiple input in 1 line input++++++++++++++++++++++++#
print("==============================")
name,age=input("Enter your name and age").split()
print(name,age)
name,age=input("Enter your name and age").split(",")
print(name,age)
# After your press comma, then it will take age .ALL
#All values before will be name