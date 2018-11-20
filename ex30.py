people = 30
cars = 40
buses = 15

if cars > people: #True
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if buses > cars: #False
    print ("Thst's too many buses.")
elif buses < cars: #True
    print ("Maybe we could take the buses.")
else:
    print("We still can't decide.")

if people > buses: #True
    print("Alright, let's just take the buses.")
else:
    print("Fine, let'sstay home then.")

 #if multiple elif blocks are true then python will run only the first one because it starts at the top and runs the first block that is True. 
