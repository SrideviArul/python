class Sup:
    #constructor here using __init__ and self denote the object 
    def __init__(self,name,age):
        self.name =name
        self.age =  age
        
    def  product_details(self):
        return self.name ,self.age
    
product1 =  Sup("fathima",23)    #object creation 
product2 =  Sup("bemila",25)
    
print(product1.name)
print(product2.product_details())  #method calling






      
        
        
    
    
      