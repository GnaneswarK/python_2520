# this was famoused before python 3.7 after 3.7 
#   no one is using this
#   because normal dict after 3.7 version onwards become ordered list

from collections import OrderedDict

my_ordered_dict = OrderedDict()

my_ordered_dict['A'] = 25
my_ordered_dict['B'] = 45
my_ordered_dict['C'] = 27
my_ordered_dict['V'] = 23
my_ordered_dict['X'] = 15

print(my_ordered_dict.items())

# we can acheive this by using dict also so after 3.7 its present but no usage
