# #
# #
# # # i=0;
# # # while i <=10:
# # #     i=i+1
# # #     print(i)
# # i=0;
# # total=0;
# # num=input("Enter any numbers")
# # while i <=len(num)-1:
# #     total= int(num[i])+total
# #     print(len(num))
# #     i=i+1
# # print(total)
# # ====================================
# i=0;
# temp=""
# string="AsadAlikamran"
# # while i < len(string)-1:
# #     if string[i] not in temp:
# #         cnt= string.count(string[i])
# #         print(f"Letter {string[i]} frequency is {cnt} ")
# #         print(f"temp is {temp} and i is {string[i]}")
# #     temp = string[i]
# #     i=i+1
#
#
# while i < len(string)-1:
#     if string[i] not in temp:
#         cnt= string.count(string[i])
#         print(f"Letter {string[i]} frequency is {cnt} ")
#         print(f"temp is {temp} and i is {string[i]}")
#     temp = string[i]
#     i=i+1
# name="asad ali  d"
# temp_var=""
# i=0
# while i < len(name):
#     if name[i] not in temp_var:
#         temp_var+=name[i]
#
#         print(f"{name[i]}: {name.count(name[i])}")
#     i+=1

# =============Another method of doing upper function=================
name="asadali ali danish"
temp=""
for  i in  name:
    if i not in temp:
        temp=temp+i
        # print(f"temp is {temp}")
        print(f"{i}: {name.count(i)}")
