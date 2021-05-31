import os
#   Custom directory
directory = input("Enter the directory that you want to save the file:")
#   Custom filename
filename =  directory + input("Enter the filename:")

#   User name
name = input("Please enter your name:")
#   User address
address = input("Please enter your address:")
#   User phone number
phone = input("Please enter your phone number:")
#   Creates new file
with open(filename, 'w') as file_object:
    file_object.write("{},\n".format(name))
    file_object.write("{},\n".format(address))
    file_object.write("{},\n".format(phone))
#   Display user input
with open(filename) as file_object:
    contents = file_object.read()
print(contents)
