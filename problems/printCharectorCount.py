#   INPUT : "GNANESWAR"
#   OUTPUT : ['G' : 1, 'N' : 2, 'A' : 2, 'E' : 1, 'S' : 1, 'W' : 1, 'R' : 1]
#

#   to get this we are using HashMap<Charector,Integer> in java with .getOrDefault() methods for values

#   in python we have counter classes which is in collection framework
#   by importing this we will Easily get the output

from collections import Counter

my_name = "Gnaneswar"

result = Counter(my_name)
print(result)

