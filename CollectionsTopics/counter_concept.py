#   INPUT : "GNANESWAR"
#   OUTPUT : ['G' : 1, 'N' : 2, 'A' : 2, 'E' : 1, 'S' : 1, 'W' : 1, 'R' : 1]
#

#   to get this we are using HashMap<Charector,Integer> in java with .getOrDefault() methods for values

#   in python we have counter classes which is in collection framework
#   by importing this we will Easily get the output

from collections import Counter

my_name = "Gnaneswar"
#   Counter is subclass to Dict
#   inside counter we have all methods which are present in the Dict
#   Additionally we have more methods in Counter example elements() methods
result = Counter(my_name)
print(result)
# if you want most repeating charector
#   if we pass 1 it shows max repeating if we pass 2 it shows max 1 and max 2 most repetive charectors
#   similar concept of limit in SQL
#   if you have 2 charectors with same number of repeating it will pict the first occurence of the charector
#   output will be list of tuple
most_repeating_charector = result.most_common(2)
print(most_repeating_charector)


#   NOW REVERSE
# im having an dict of key value pairs like this
# input : {'G': 1, 'n': 2, 'a': 2, 'e': 1, 's': 1, 'w': 1, 'r': 1}
# OUTPUT = Gnnnneswr


input = {'G': 1, 'n': 2, 'a': 2, 'e': 1, 's': 1, 'w': 1, 'r': 1}
my_input = Counter(input)
#   .elements() will make this an iterable one
#   next we are saying add those itterable one to the list
#   next join the list with '' this
print(''.join(list(my_input.elements())))
