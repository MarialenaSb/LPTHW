people = 20
cats = 30
dogs =15

if people < cats:
    print ("Too many cats! The world is doomed!") #True

if people > cats:
    print ("Not many cats! The world is saved!") #False

if people < dogs:
    print ("The world is drooled on!") #False

if people > dogs:
    print ("The world is dry!") #True

dogs += 5 #Reminder: The "increment by" operator +=, means that the code x += 1 is the same as doing x = x + 1.

if people >= dogs:
    print("People are greater than or equal to dogs.") #True

if people <= dogs:
    print ("People are less than or equal to dogs.") #True

if people == dogs:
    print("People are dogs.") #True
