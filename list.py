listitem =  ["apple","banana","orange"]
newlist = []
for x in listitem:
    if "a" in x:
        newlist.append(x)
        
        print(newlist)
        
listitem.sort(reverse =True)
print (listitem)

def funct(n):
    return abs( n - 50)

listda =  [65,50,45,23,1,49]

listda.sort(key = funct)
print(listda)