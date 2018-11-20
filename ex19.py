def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print ("You have %d cheeses!" % cheese_count)
    print ("You have %d boxes of crackers!" % boxes_of_crackers)
    print ("Man that's enough for a party!")
    print ("Get a blanket. \n")

print ("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print ("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print ("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5+6)

print ("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# In a way, the arguments to a function are kind of like our = character when we make a variable.
# In fact, if you can use = to name something, you can usually pass it to a function as an argument.
maria = 50
eleni = 37
cheese_and_crackers(maria, eleni)

print ("So, how many crackers do we have?")
crackers = input()

print("And how many cheeses?")
cheese = input()

print ("""
So you said that we have %r crackers and %r cheeses! Cool!
""" % (crackers, cheese))
