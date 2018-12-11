ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split() # split(ten_things, )
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # as long as the length of the list is different than 10 the loop will be executed
    next_one = more_stuff.pop() # removes the last element of stuff / pop(more_stuff, )
    print ("Adding: ", next_one)
    stuff.append(next_one) #adds at the end of the list a new element from more_stuff / append(stuff, next_one)
    print("There's %d items now." %len(stuff))

print ("There we go:", stuff) # --> There we go: ['Apples', 'Oranges', 'Crows', 'Telephone', 'Light', 'Sugar', 'Boy', 'Girl', 'Banana', 'Corn']
print("Let's do some things with stuff.")

print (stuff[1]) # --> Oranges
print(stuff[-1]) # --> Corn ?
print(stuff.pop()) # --> Corn (it will erase the last element of the list) / pop(stuff, )
print(' '.join(stuff)) # --> Apples Oranges Crows Telephone Light Sugar Boy Girl Banana / join(' ', stuff)
print('#'.join(stuff[3:5])) # --> Telephone#Light / join(#, stuff[3:5])

#https://realpython.com/python3-object-oriented-programming/
#https://python.swaroopch.com/oop.html
#https://www.programiz.com/python-programming/object-oriented-programming

#NOTE: The class of something is simply its type. The dir function effectively shows you all the methods and attributes associated with the instance.
