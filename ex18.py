#This is an import. The argv is the "argument variable and holds the arguments you pass to your Python script when you run it.
from sys import argv
# this line unpacks argv. it gets assigned to 2 variables.
script, input_file = argv
#This creates the function print_all with argument f.
def print_all(f):
    print(f.read())

# seek takes you to specific line in a file def rewind(f): f.seek(0)
def rewind(f):
    f.seek(0)
# What it does here in your code is move the current position in the file to the start (index 0).
# The use of this in the code is that on the previous lines, the entire file was just read, so the position is at the very end of the file.
# This means that for future things (such as calling f.readline()), you will be in the wrong place.
# Whereas you want to be at the beginning - hence the .seek(0).

# readline()reads one entire line from the file.
# fileObject.readline( size ); size − This is the number of bytes to be read from the file.
def print_a_line(line_count, f):
    print (line_count, f.readline())

current_file = open(input_file)

print ("First let's print the whole file:\n")

print_all(current_file)
#print (current_file.read())

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print, ("Let's print three lines:")

# The readline() function returns the \n that’s in the file at the end of that line
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
#current_line = current_line + 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

#NOTE: += this is kind of like a contraction for the two operations = and +. That means x = x + y is the same as x += y.

#NOTE: Inside readline() is code that scans each byte of the file until it finds a \n character, then stops reading the file to return what it found so far.
# The file f is responsible for maintaining the current position in the file after each readline() call, so that it will keep reading each line.
