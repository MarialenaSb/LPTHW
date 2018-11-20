# We type python ex13.py to run the (script) ex11.py file. The ex11.py part of the command is called an "argument".
# We are going to write a script that also accepts arguments.

from sys import argv
#This is an import. This is how you add features to your script from the Python features set. Python asks you what you plan to use.
# The argv is the "argument variable," a very standard name in programming that you will find used in many other languages.
#This variable holds the arguments you pass to your Python script when you run it.

script, first, second, third = argv
# this line unpacks argv so that, rather than holding all the arguments, it gets assigned to four variables you can work with: script, first, second, and third.
#It just says "take whatever is in argv, unpack it, and assign it to all these variables on the left in order"
#After that we just print them out like normal.

print ("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print ("Your third variable is:", third)

script_q = input("Give a name to the script:")
Variable_a = input("Which is the name of the first variable?")

# In order to run the program I need to write python ex11.py first second third
# when I run it I can replace the first 2nd 3rd with any 3 things I want
