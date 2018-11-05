def add(a, b):
    print ("ADDING %d + %d" % (a, b))
    return a + b

def subtract (a, b):
    print("SUBTRACTING %d - %d" % (a, b))
    return a - b

def multiply (a, b):
    print("mULTIPLYING %d * %d" %(a, b))
    return a * b

def divide (a, b):
    print ("DIVIDING %d / %d" % (a, b))
    return a / b

print ("Lets do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print ("Age: %d, Height: %d, Weight:%d, IQ:%d \n" %(age, height, weight, iq))

# A puzzle for the extra credits.
print ("Here is a puzzle.")

#what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

div = divide(iq, 2)
mul = multiply(div, weight)
sub = subtract(height, mul)
what = add(sub, age)

print("That becomes: ", what, "Can you do it by hand?")
