# #
# #
# # # Tuple is same as list. You just cannot use addition(append,insert,remove) or subtraction function in tuple
# # # # Because Tuple are immutable. All other function you can use
# # However if there is list in tuple ,there you can append,insert,remove from that list.
# # Means list  inside a tuple will have its all feature as list
# # # #  Too create tuple with one element .You must need to add comma at the end.Otherwise pytohn
# # # # will create int/string/chr based on element
# #
# # name=("asdfa") # name is string
# # print(type(name))
# # name=(3)#name is integer
# # print(type(name))
# # name=(3,) # name is tuple
# # print(type(name))
# #
# # name=("ali", 2, "khan","d") #Tuple with 4 element.Ali is one element.Cannot accest a/l/i sperately.
# # print(name[2])
#
# ####In tuple, there is no conversion to string/. Tulips has only link with variable#########unpacking
# #######You can convert multiple variable to tuple at onece .You can convert/store tulip to multiple variable.
# # =======Tulip to variable=========
# # name=("ali", 2, "khan","d")
# # a,b,c,d=name
# # print(a,b,c,d)
# # print(type(a))
# # print(type(b))
# # print(type(c))
# # print(type(d))
# # #If you assign multiple data to single vairble, they output variable will become tuple.
# # =======Variable to Tulip=========sanme as list=========
# # name=1,"asad",343,"what is your"
# # print(type(name))
# # print(name)
# # =======List to tulip=========sanme as tuplip=========
# # name=["ali", 2, "khan","d"]
# # a,b,c,d=name
# # print(a,b,c,d)
# # print(type(a))
# # print(type(b))
# # print(type(d))
# # print(type(c))
#
# # ======
# # # If you return two variable from function using return statement, then return data formate will be tuple,
# # def abc(a,b):
# #     c=a+b
# #     d=a*b
# #     return c,d
# # m=(abc(4,3))
# # print("Return of two variable from function  is tuple which is "+ str(m))
# # print("You can store tuple in different variable as below")
# # a,b=m
# # print(a,b)
# # print(type(a),type(b))
# # # =======Generation List======
# # name1= list(range(1,11))
# # print(name1)
# # print(f"Type of name 1 is :{type(name1)}")
# # print(f"zero element of string is: {name1[4]}")
# # =======Generation Tuple======
# # name1= tuple(range(1,11))
# # print(name1)
# # print(f"Type of name 1 is :{type(name1)}")
# # print(f"zero element of string is: {name1[4]}")
# # =======cREATE Tuple======
# name1= tuple(range(1,11))   #First create tuple
# print(name1)
# print(f"Type of name 1 is :{type(name1)}")
# print(f"zero element of string is: {name1[3]}")
# # =======Tuple Converstion to list======
# print("Conversion Tuple to List")
# name1=list(name1)
# # print(f"Type of name 1 is :{type(name1)}")
# # print(f"zero element of string is: {name1[3]}")
# #
# # # =======Tuple Converstion to string======
# # print("Conversion Tuple to List")
# # name1=str(name1)
# # print(f"Type of name 1 is :{type(name1)}")
# # print(f"zero element of string is: {name1[3]}")
#
#
# # =======cREATE List============
# name1= list(range(1,11))   #First create tuple
# print(name1)
# print(f"Type of name 1 is :{type(name1)}")
# print(f"zero element of list is: {name1[3]}")
# # =======List to Tuple======
# print("Conversion list to Tuple")
# name1=tuple(name1)
# print(f"Type of name 1 is :{type(name1)}")
# print(f"zero element of list is: {name1[3]}")
# # =======List to String======
# print("Conversion list to string")
# name1=str(name1)
# print(f"Type of name 1 is :{type(name1)}")
# print(f"zero element of  is: {name1[3]}")

# ========String to list=========
name="This is a string"
print(name)
m=list(name)
print(type(m))
print("After conversion ")
print(m)
print(m[5])

