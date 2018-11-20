# in this exercise I will learn how to make strings that have variables embedded in them.
#You embed variables inside a string by using specialized format sequences and then putting the variables at the end with a special syntax that tells Python,
# "Hey, this is a format string. Put these variables in there."

name = 'Marialena Sbrini'
age = 24
height = 65
eyes = 'Brown'
teeth ='white'
hair = 'Brown'
weight = 132
centimeters = height * 2.54
kilos = weight / 2.2

print ("Let's talk about %s." % name)
print ("She's %d inches tall" % height)
print ("Actually that's not too tall.")
print ("She's got %s eyes and %s hair." %(eyes, hair))
print ("Her teeth are usually %s depending on the coffee." % teeth)
print ("%r inches equals %r centimeters." %(height, centimeters))
print (" %r pounds equals %r kilos." %(weight, kilos))

print ("If I add %d, %d and %d I get %d." %( age, height,  age, 165 + 48))
