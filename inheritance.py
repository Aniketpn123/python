class Cars:
  def car(self):
    print('car')

class Bmw(Cars):
   def bmw(self):
     print('bmw')
  

class Hyundai(Cars):
  pass

bmw1=Bmw()
# bmw1.car()

def cart():
  print('yes')



# define fun to import 

def find_max(number):
  max=number[0]
  for x in number:
    if x > max:
      max=x
  return max  
