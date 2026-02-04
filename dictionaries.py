# x={
#   "name":'aniekt',
#   "age":347,
#   "mail":"anffpn",
#   "is":True
# }

# x["name"]="viel"
# print(x["age"])
# print(x["name"])
# print(x)
# print(x.get("Age","23"))

# 1. input pritning

# phone= input("no:")

# x= {
#  "1":"one",
#  "2":"two",
#  "3":"three",
#  "4":"four",
#  "0":"zero",
# }

# for i in phone:
#   print(x.get(i,"!"))

m= input(">")
w = m.split(' ')
x={
  "1":"one",
  "2":"two"
}
for i in w :
  print(x.get(i, i))



