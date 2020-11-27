''' 1
my_list = [1, 2, 3]
my_new_list = [i * 2 for i in my_list]
print(my_new_list)
'''

''' 2
my_list = [1, 2, 3]
my_new_list = [i ** 2 for i in my_list]
print(my_new_list)
'''



''' 4
from datetime import datetime
year1 = datetime.now().year
year2 = 1900
rad = year1 - year2
for i in range(rad+1):
    print(year2 + i)
'''