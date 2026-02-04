# class Point:
#   def __init__(self,x,y):
#     self.x= x
#     self.y=y

#   def draw(self):
#     print("y")


#   def line(self):
#     print('r')



# point1 = Point(10,20)

# # point1.draw()

# # point1.x=5
# # point1.y=4

# print(point1.x)


class Person:
  def __init__(self,name):
    self.name=name
  
  

  def talk(self):
    print(f'hi i am {self.name}')

aniket = Person("aniket")
aniket.talk()
print(aniket.name)

