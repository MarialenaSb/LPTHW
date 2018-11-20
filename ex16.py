from sys import argv

script, filename = argv

print ("We are going to erase %r." %filename)
print ("If you don't want that, hit CTRL-C(^C).")
print ("If you do want that, hit RETURN.")
#If I use the syntax with print("""....""") I get the same result.

input("?")

print ("Opening the file...")
target = open(filename, 'w')
#It’s really just a string with a character in it for the kind of mode for the file.
#If you use 'w', then you’re saying “open this file in ‘write’ mode”—hence the 'w' character (truncating the file if it already exists).
#There’s also 'r' for “read,” 'a' for append, and modifiers on these.The most important one to know for now is the + modifi er, so you can do 'w+', 'r+', and 'a+'.
#This will open the fi le in both read and write mode and, depending on the character used, position the fi le in different ways.


print ("Truncating the file. Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print ("I'm going to write these to the file.")

target.write('\n'.join((line1,line2,line3)))

text = open(filename)
data = (text.read())
# ???????????

print ("And finally, we close it.")
target.close()
