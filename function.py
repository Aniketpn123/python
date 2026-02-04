# def my_name(name,surname):
#   print(f'y {name} {surname}')


# my_name('aniket','ani')
# def square(no):
#   print(no*no)
#   return 2 
# print(square(3))



# exception handle  ......


try:
  age= int(input('value :'))
  risk= 2000/age
  print(age)
except ZeroDivisionError:
  print(' invalid age zero')
except ValueError:
  print('invalid value')
