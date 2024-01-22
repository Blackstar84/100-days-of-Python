programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
    }


print(programming_dictionary["Bug"])

print(programming_dictionary)

# Adding new items to the dictionary

programming_dictionary["Coma"] = "Use to separete new items of a dictionary"

print(programming_dictionary)


# Create a new dictionary

empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}

# print(programming_dictionary)

# Edit an item in a dictionary
# If item exist will replace with the given text, otherwise it will create a new item

programming_dictionary["Bug"] = "A moth in your computer"

print(programming_dictionary)


# Loop through a dictionary

for key in programming_dictionary:
    print(f"{key}: {programming_dictionary[key]}")

