# How to Create Lists using List Comprehension
#LIST = [ITEM, ITEM, ITEM]
#new_list = [NEW_ITEM for ITEM in LIST]
from tkinter.font import names

numbers =[1,2,3]
new_list = [n+1 for n in numbers]
print(new_list)

# List Comprehension funkar inte enbart på listor
name ="Molly"
new_name = [letter.upper() for letter in name]
# "".join([letter.upper() for letter in name])
print(new_name)

# Range
numer_list = [n * 2 for n in range(1,5) ]
print(numer_list)


# Conditional list comprehension - if
names_list = ["Anna", "Erik", "Sara", "Molly", "Maria", "Lukas", "Emma"]
new_list_names = [name.upper()  for name in names_list if len(name) >= 5 ]
print(new_list_names)




# How to use Dictionary Comprehension

# new_dict = {NEW_KEY: NEW_VALUE for ITEM in LIST}

import random

all_students = {name:random.randint(1,5) for name in names_list}

print(all_students)

passed_students = {student: score for (student, score) in all_students.items() if  score >= 3 }

print(passed_students)





fruit_dict = {
    "fruit": ["Apple", "Banana", "Orange"],
    "price": [10, 7, 12]
}

# looping dictionary
#for (key, value) in fruit_dict.items():
#    print(key,value)


import pandas
fruit_data_frame =pandas.DataFrame(fruit_dict)
for (index, row) in fruit_data_frame.iterrows():
    print(row.fruit) # row  or -> row.fruit  row.price