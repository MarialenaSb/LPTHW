from sys import argv

script, filename = argv
#unpack argv. it gets assigned to 2 variables: script and filename

txt = open(filename)
#open: it takes a parameter and returns a value you can set to your own variable.If I put ex13.txt when I'm going to run the program then the filename refers to this.

print ("Here is your file %r: " % filename)
#Here is your file ex13.txt
print (txt.read())
# here we call a function on txt. We give a file a command by using the . (dot or period), the name of the command, and parameters. This will appear the text from the ex13.txt

print ("Type the filename again: ")
file_again = input(">")

txt_again = open(file_again)
# it defines as the variable txt_again the answer of the user
print (txt_again.read())
#It appears the text again if the name is right

txt_again.close()
txt.close()
