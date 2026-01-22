
"""
Data Overlap

Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.
You are going to create a list called result which contains the numbers that are common in both files.

e.g. if file1.txt contained: 1 2 3

and file2.txt contained: 2 3 4

result = [2, 3]

IMPORTANT:  The output should be a list of integers and not strings!
"""



# Formaterar lista
def create_list(list):
    new_list =[ int(    number.replace("\n", "")     ) for number in list]
    return new_list

with open("file1.txt") as file1:
    list_one = create_list( file1.readlines())

with open("file2.txt") as file2:
    list_two = create_list(file2.readlines())

print(list_one,list_two)

# Kollar om nummer i lista 1 finns i lista 2 → skapar en ny lista med gemensamma nummer
result= [number for number in list_one if number in list_two]
print(result)
