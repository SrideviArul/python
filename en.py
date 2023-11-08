#Encapsulation 
class En:
     #private variable declaration  cant not access noone 
     __companyname = "yaruda" 
     
     def __init__(self,company):
      #protected variable 
      self._company = company
     
p1 = En("saptiya")

print(p1._company)
print(p1.__companyname)

