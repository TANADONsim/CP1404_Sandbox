"""Input name and print odd characters"""

name = input("Enter name:-")

"""Check that name is not blank"""

while len(name) <= 0:
    print("Name is blank, enter again.")
    name = input("Enter name:-")

"""Print odd characters in the name"""
print(name[::2])

"""Another way of doing it"""
for i in range (0, len(name), 2):
    print(name[i], end="")

"""commit test"""