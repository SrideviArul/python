import datetime
date = datetime.datetime.now()
print(date)
result = repr(date)
print(result)
print(eval(result))
'''print(f.readable())
print(f.writable())
f.write('allah\n')
list = ['apple\n','banana\n']
f.writelines(list)'''
f =  open("/home/assistanz/enna.txt",'r')
content = f.read()
print(content)
#positional arguements
def add(no1,no2):
    print(no1+no2)
    
add(1,2)

#keyword arguements
def adds(no1,no2):
    print(no1+no2)
    
adds(100,no2=2)     #always position arguements follows keyword arguements

#default arguements
def adi(no1,no2=1):
    print(no1+no2)
adi(10,11)

#variable length arguements
def ada(no1,*no2):
    print(no1)
    total =0
    for i in no2:
        total = total + i
        print(total)
        
ada(10,202,299)     

#keyword variable arguements
def ad(**kwargs):
    print(kwargs)
    for key,value in kwargs.items():    
      print(key,value)
      
ad(name='fathi',age='22')    
    

