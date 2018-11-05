#A string is usually a bit of text you want to display to someone, or "export" out of the program you are writing.
# Python knows you want something to be a string when you put either " (double-quotes) or ' (single-quotes) around the text.
#You saw this many times with your use of print when you put the text you want to go inside the string inside " or ' after the print to print the string.

x= ("There are %d types of people." %10)
binary= "binary"
do_not= "don't"
y= ("Those who know %s and those who %s" %(binary, do_not))

print (x)
print (y)

print ("I said: %r." % x)
print ("I also said: '%s'." % y)

hilarious =False
joke_evaluation= ("Isn't that joke so funny?! %r")

print (joke_evaluation % hilarious)

w= ("This is the left side of...")
e= ("a string with a right side.")

print (w + e)
