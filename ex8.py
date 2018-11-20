formatter = ("%r %r %r %r")

print (formatter % (1, 2, 3, 4))
print (formatter % ("one", "two", "three", "four"))
print (formatter % (True, False, False, True)) # I dont need "" here.
#Python recognizes True and False as keywords representing the concept of true and false.
# If you put quotes around them then they are turned into strings and won't work.
print (formatter % (formatter, formatter, formatter, formatter))
print (formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."))
