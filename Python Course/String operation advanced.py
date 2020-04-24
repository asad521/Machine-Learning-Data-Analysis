# p     y      t        h       o       n
# 0     1      2        3        4      5
# -6   -5     -4       -3       -2       -1
lang="Python"
print(lang[-3:5:])  # Left of right direction of printing
print(lang[-3:0:-1]) # Right to left direction of printing
print(lang[:])
print(lang[2:])
print(lang[:4])
#++++++Step++++++++
lstring="WhatIsYourName"
print(lstring[::2]) # Step is Two
# Note
# lstring{m:n:p}
# # m i start, n is end argument, p is step and sign is direction
#============String Builtin method============#

# len is function .All other below are methods

name="MyNameisPytohnn"
print(f"Length of string is {len(name)} and count of m is {name.count('n')}")
#===============#
print("==================")
name="My Name is Pytohn"
print(f"Title is \" {name.title()}\" and captialize is \" {name.capitalize()} \"")
#===============#
print("==================")
name="My Name is Pytohn"
print(f"Upper letter is \"{name.upper()}\" and lower letter is \"{name.lower()}\"")
#===============#
print("==================")
name="My Name is Pytohn"
print(f"Upper letter is \"{name.upper()}\" and lower letter is \"{name.lower()}\"")
#===============#
#===============#

#===============#
name="       My Name is Pytohn"
print(f"Removing left space {name.lstrip()}")
name="My Name is Pytohn         "
name2="abc"
print(name,name2)
print(f"Removing left space {name.rstrip()} and is {name2}")
# =======REPLACE AND FIND==============

name="How are Your. I am fine"
print(name)
print(name.replace(" ","_"))
print(name.replace("is","was"))
print(name.replace("e","was"))
print(name.replace("e","was",1))  #Specify how many string to replace

print("==================")
name="My Name is Pymtohn"
print(f"Find a letter is  \" {name.find('m')} ")
print(f"Find a letter is  \" {name.find('am')} ")
print(f"Find a letter is  \" {name.find('m',7,15)} ") #Specify the range from which to find.
print(f"Find a letter is  \" {name.find('m',0,9)} ")
# =============================================================
name="Asad"
print(name.center(8,"*")) # 8 is width, 4 is length of word.remaing 4. which is added on both equally
# =================================
name="Asad"
name="asdfasdfsadf"
print(name)