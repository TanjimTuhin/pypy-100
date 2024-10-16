programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    123 : "it's a number though."
    }

print(programming_dictionary[123])

#adding new item to dictionary 
programming_dictionary["Loop"] = "A way to repeat a block of code over and over again."

print(programming_dictionary)

#create an empty dictionary 
empty_dictionary = {}

#wipe an existing dictionary 
programming_dictionary={}
print(programming_dictionary)

#edit an item in a dictionary
programming_dictionary["Bug"]='A moth in your computer'
print(programming_dictionary)

#loop
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])