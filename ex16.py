#This one is like your scripts with argv
# We tell Python we want to make a function using def for "define"
# print_two is the name of the function
# args is a lot like our argv parameter but for functions
def print_two(*args) :
    # * That tells Python to take all the arguments to the function and then put them in args as a list.
    # It’s like argv that you’ve been using, but for functions. It’s not normally used too often unless 
    # specifically needed.
    arg1, arg2 = args
    print ("arg1: %r, arg2: %r" %(arg1, arg2))

# ok, that *args is actually pointless, we can just do This
def print_two_again(arg1, arg2):
    print ("arg1: %r, arg2: %r" %(arg1, arg2))

#this just takes one argument
def print_one(arg1) :
    print("arg1: %r" % arg1)

#this one takes no arguments
def print_none():
    print ("I got nothing'.")

print_two ("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()
