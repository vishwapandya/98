#create test.txt 
f = open('test.txt')
#f.read()

#to print the file line by line
fileLines = f.readlines()

#readlines() defined on file object splits the lines in the file and stores it line by line as a list. We can print these lines 
# by calling a for loop on the list.
for line in fileLines:
    print(line)

introString = "My name is Wily, I am 15 years old."

#split() splits the given string by their whitespaces, gives each individual word and stores them in a list.
words = introString.split()
print(words)

#split() splits using whitespace by default. You can also specify which separator to use to split the items.
#For example, we could have used comma (,) as the separator
phrases = introString.split(",")
print(phrases)

#creating a custom defined function
def greet(name):
    print('Hello, '+ name + '. How are you?')

# #will use it like greet("vishwa") otherwise error will come 