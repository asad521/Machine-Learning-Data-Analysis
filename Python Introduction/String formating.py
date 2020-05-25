
name="Rahul"
age=34
print("Helloe{}. Your age is {}".format(name,age))
print(f"Hello{name}.Your name is {name}.Youe age is {age}. Your total money is {4+4}")

# num1,num3,num4=int(input("Enter three number to add sperated by comma")).split(",")
# total=num1+num3+num4
# print(f"Your total of {num1}, {num3} and {num4} is {total}")
num1,num3,num4=input("Enter three number to add sperated by comma").split(",")
# print(f"Your total of {num1} {num3} and {num4} is {total}")
# total=int(num1)+int(num3)+int(num4)
# or
print(f"Your average of {num1}, {num4} and {num3} is "
      f"{(int(num1)+int(num3)+int(num4))/3}")