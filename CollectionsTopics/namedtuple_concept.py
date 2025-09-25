#   Scenerio
#   In Java we know what is POJO Class plain old Java Object
#   where only instance varaiables will be there if is encapsulated then getters setters

#   in python if we want pojo type we need create class __init__ methods pass argumethds

#   we can do this without creating an class in python by importing namedtuples from collections

from collections import namedtuple

# here we will create an class which take 2 parameters
#   x and y which points x-axis and y-axis and class name should be Point
#   we can do like this namedtuple("ClassName","x(variable1),y(variable2)") NOTE :: variables are seperated by comma ,

#   PLEASE NOTE IT ADYAKSHA IT IS IMMUTABLE ONCE ASSIGNED YOU CANNOT CHANGE
#   IF YOU WANT MUTTABLE DATA THEN GO WITH dataclasses
#   dataclasses which are more powerful than namedtuple because they allow mutability and default values:
Points = namedtuple("Points" , 'x,y')

p = Points(3,5)
print(p)
print(f"({p.x} , {p.y})")