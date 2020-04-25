

def qbit(num):
    dict={}
    for  i in range(1,num):
        dict[i]= i**3
    return  dict
print(qbit(7))
print("String to work as well as word counter")
def st(h):
    dict={}
    for i in h:
        dict[i] = h.count(i)
    return dict
print(st("muhamamdasadali"))

