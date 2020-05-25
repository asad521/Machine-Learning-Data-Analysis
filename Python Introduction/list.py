# l1=["banana","mango","apple"]
# # list1=["A","B","C"]
# # list1.append("asad")
# # l1.insert(1,"Karman")
# # print(l1)
# # list1=l1+list1 #equals to extend
# # print(list1 )
# # append will add to end of list
# # insert method can give index
# # append methond will append the list as element. Even if you give
# # a list. size of Appended(output) list will only increase by 1 element
# # ======
# # if you want to make new list containing are element of l1 and l2,
# # then concatinat(+) the both list to get the third list/or extend third list . Not append list.other wise it will only
# # add one element as a list. will not add element of list.

# ====================Deleteing========================================================
last = ["A", "B", "C", "D", 5, 6, 7]
print(last)
last.pop()  # to delete last item
print(last)
last.remove("C")  # to remove the specific element in list.
# If there are two same element , then it will delete first
print(last)

del last[2]  # To delete number at sepecific  index
print(last)
m = [1, 4, 5, 2, 45, 9, 455]
m.sort()
print(m)
m.sort(reverse=True)
print(m)
# m.sorted()#will only print the list.Not sort the actual
print(m.index(455))
# ======compare======
m = [1, 2, 3, ]
n = [1, 2, 3, 9]
print(m == n)
# ================================
print("========================")
name = "asad ali khan".split()
print(name)
# split methond is only used to split string from space or commna
# you can store splitted element into multiple variable
# or if you give only one variable, it will make a list of all element
# ==========list to string==========
names = ["asad", "ali", "salman", "qamar"]
m = ','.join(names)
print("M has become string which is "+m)
print(m[2])
print(type(m))
# ========Looping in list===================
# fruit = ["A", "B", "C", "D", "E", "F", "G"]
# for m in fruit:
#     print(m)
    # loop  are same as in string .Both show the element content .
    # Both show  Element. Not index or integer
    # If you want to know the index ,then you need to start loop with integer(from 0)
    # and when match occures ,then you can note the index

print("=================")
# stringg = "My name is asad"
# for i in stringg:
#     print(i)
# ============
nest=[]
# a = "a b c"
# b = "d e f"
# c = "g h i"
# list1= a.split()
# list2 = b.split()
# list3 = c.split()
# list1.append(list2)
# list1.append(list3)
# print(list1)
# print(list1[4])
# print(list1[4][1])
# =====================
# listt=["asad"]
# print(type(listt))
# print(listt[0])
# =====================
# ===========================
# numbers=list(range(1,11))
# print(numbers)
# numbers=list(range(0,11,2))
# print(numbers)
# print(numbers.index(2))
