import random 
x = 5
print(x)
myVariable = "enna pandra"
print(myVariable)
print(type(myVariable))
fruits = [5.000,"rasam"]
xx,y=fruits
print(xx)
print(y)
print(type(xx))
xa,ya,za = 5,"cfvgds",5
print(xa)
print(ya)
print(za)
print(xa)
xi = "awesome"

def myfunc():
  print("Python is " + xi)

myfunc() 



def practical():
    global summa
    summa = "en"
    print("python is " + summa)
    
practical()
print("python is " + summa)

print(random.randrange(8, 10)) 

rangeFind=range(7)
print(rangeFind)

for i in rangeFind:
  print(i)
  
  
n=10
if n>5:
  print("true")
  
  
sure = "enna pandra"
print("enna" in sure)

print("ennaq" not in sure)

print(sure[:2])
  
print(sure.upper())
print(sure.lower())
print(sure.strip())
lett = sure.split(" ")
print(lett[0])
age = 42
rate = 45.50
txt = "enna da edhu {} rate enna theriyuma {}"
print(txt.format(age , rate ))

allah = "enna pandra  \"vitru\" po"
print(allah)
critical = "paal"

print(critical.center(20))
print(len(allah))

print(critical.capitalize())
print(critical.casefold())
print(critical.center(20))
print(critical.count("paal",0,5))

print(critical.endswith("paal"))
critical1 = "s\ta\tp\tt\ti\ty\ta\t pa"
print(critical1.expandtabs(5))
print(critical.find("a",0,2))
print(critical.index("a"))
critical3="papa {}"
print(critical3.format("enga"))
critical4 = "papa {weight:.2f} {what}"
print(critical4.format(weight = 45,what ="sapta"))
#empty placeholder
critical5 = "papa {}".format("enna")
print(critical5)
#numbered indexes 
critical6 = "papa {0}".format("papa")
print(critical6)
#named indexes
critical7 = "papa {what}".format(what="summa")
print(critical7)
txt2 = "saptiya {:<15} eppo".format("sapadu") 
print(txt2)
txt3 =  "{:%}".format(0.25)
print(txt3)
txt3 =  "{:.0%}".format(0.25)
print(txt3)
txt3 =  "{:=8}".format(-25)
print(txt3)
txt3 =  "{:^8}".format(25)
print(txt3)
txt3 =  "{:-} {:-}".format(25,-7)
print(txt3)
#it if for iterable and join a string 
mytuple = ("fathi","allah","al-malik")
txt="**".join(mytuple)
print(txt)


txt1="sapadu"
c=txt1.join(mytuple)
print(c)

v=txt1.ljust(20) + "enna"
print(v)

v="             over           "
print(v.lstrip())
print(v.rstrip())

txt4="good sam good good"
txt5="banana"
x = "mSa"
y = "eJo"
#vb= str.maketrans("s","r")

#print(txt4.translate(vb))

vf=str.maketrans(x,y)
print(txt4.translate(vf))

print(txt4.replace("good","bad",2))
print(txt5.rjust(20))
print(txt4.rpartition("good"))




#list 
fruits = ['apple','orange','graps']
fruits.append('laddu')
print(fruits)
flowers = ['lotus','malli']
fruits.append(flowers)
print(fruits)
fruits.extend(flowers)
sapadu =fruits.copy()
print(sapadu)
print(fruits.index('lotus'))
fruits.insert(0,'banana')
print(fruits)


print(bool("True"))
class myfunc():
  def enne():
    return 1
  
  enne()
  
  #print(bool(enne))
  myobj = myfunc()
  print(bool(myobj))
  
  def myfunc():
    return True 
  
  if myfunc():
    print("yes")
  
  x=80
  print(isinstance(x,int))
  
  
  
  
  