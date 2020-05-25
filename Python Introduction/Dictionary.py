

data={
    "name":"Asad",
     "age":34,
      "sex": "male",
    "fav_movies":["Teray Naal","MI3","Sky Fall","Dela Venus"],
    "hobies": ["Cricket","Net Surfing","Books reading"]
}
print(data)

print(data["fav_movies"])
print(type(data["fav_movies"]))
print(type(data))

data["Discription"]= "This is data about student Asad "
print(data)

if "male" in data.values(): # Male is Present
    print("Presntt")
else:
    print("Not Present")
# =======================================
    if "Cricket" in data.values():  # Cricket is not present. It will check whole value.Not single value
        print("Presntt")
    else:
        print("Not Present")
print("======Printing==============")
for i in data:  # Print All keys
    print(i)
print("==========First Method=======================")
for i in data.values(): #   Print all values
        print(i)
# Another way to print  values
print("=======Second Method======================")
datavalue= data.values()
print(datavalue)
# Another way to print  values
print("=========Third Method======================")
for i in data:
    print(data[i])
print("========4th Item Method======================")

for i in data.items():
    print(i)

for i,j in data.items():
    print(f"Key is {i} : Value is {j}")
print("========5 th Item Method======================")
print(data['name']) # This is simple method, same asa acessing data in list,tuple
print("========6 get method Method======================")
print(data.get("names")) #This method is same as above .But good because if you write wrong name of key
#it will  written None rather than giving error.
print(data.get("names","Key not found in dictionary")) #YOU CAN WRITE YOUR OWN MASSAGE IN DICT

print("========Making list of key and value seprately======================")
# You can store key and values into different list
key=[]
value=[]
for i,j in data.items():  #Extra info. This is actually tuple unpacking, If you assign only i varaible, then it will give output tuple
    key.append(i)         # Basically you are assign one tuple into two variable.i , j and using that to create list .
    value.append(j)
print(key)
print(value)
print("========Adding data(key in terms of dictionary) to dictionary======================")
for i in data:
    print(i)
data["fav_Song"]='Jazz',"Rap","Classic"

for i in data:
    print(i)
print("========To delete specific item/key from dict=========")
# pop will delete any sepcified key and it will return the key value in original formate of key.
m=data.pop("Discription")
print(m)
print(type(m))
print("========By pop item method=========")
# pop will delete any sepcified key and it will return the key value in original formate of key.
# It will return a complete tuple with key and value together.
m=data.popitem()
print(m)
print(type(m))
print("======================================")
print(data)
education_info={
    "school": "FG Govt High School",
    "College":"ABC Govt College Males",
     "Subjects":["Math","Science","Computer Science"]
}
data.update(education_info)
print("======================================")
for i in data:
    print(i)
print("===========Frame Method===========================")
#If you want to add multiple keys with same value, use fromkeys method
# This method is used to creat a new dict with multiple keys having same value.
#This method return a dictionary
#dict. fromkeys(iterable,[value])
#iterable can be any iterbale(list,tuple,string) , but
#Better to use tuple, because if you use list as key,then change in origial will also effect dict.
m=dict.fromkeys(['BloodGroup','Matritcal Status','Language'],'Unknown')
for i in m.items() :
    print(i)
print("===========Mutability Check===========================")
A=['BloodGroup','Matritcal Status','Language']
m=dict.fromkeys(A,'Not Given')
for i in m.items() :
    print(i)
print("===========Addition One more element into list===========================")
A.append("Asad")
print(A)
print("===========Mutability Check===Value Did not Change====================")
for i in m.items() :
    print(i)
# ========
m=data.copy()
new_dict=m # This will not creat new dictionary. if you change something in m, it will also change in new diction
# Therefore use copy method
#Copy data dictionary into m
data.clear() # To clear Dictionary
print(data)