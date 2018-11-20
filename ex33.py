i = 0
numbers =[]


while i < 10 and i != 8 :   #for i in range(0,10):
    print("At the top i is %d" % i)
    numbers.append(i)

    i = i + 2
    print ("Numbers now:" ,  numbers)
    print ("At the bottom i is %d" %i)

print ("The numbers:")

for num in numbers:
    print (num)
