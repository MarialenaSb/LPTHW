# We’re going to actually write a Python script to copy one file to another.

from sys import argv
from os.path import exists
# We import the command named exists. This returns True if a file exists, based on its name in a string as an argument. It returns False if not.

script, from_file, to_file=argv
# from_file is the argv[1]

print("Copying from %s to %s" %(from_file, to_file))

in_file = open(from_file)
indata = in_file.read()

print ("The input file is %d bytes long" %len(indata))

print ("Does the output file exist? %r" % exists(to_file))
print ("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file,'w')
out_file.write(indata)

print ("Alrigth, all done.")

out_file.close()
in_file.close()

#I could have the same output with the following code:
# from sys import argv; open(argv[2],'w').write(open(argv[1]).read())
