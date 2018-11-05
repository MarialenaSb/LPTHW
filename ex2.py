cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print ("There are", cars, "cars available.")
print ("There are only", drivers, "drivers available.")
print ("There will be", cars_not_driven, "empty cars today.")
print ("We can transport", carpool_capacity, "people today.")
print ("We have", passengers, "to carpool today.")
print ("We need to put about", average_passengers_per_car, "in each car.")

# the _ is called underscore character.
# The = (single-equal) assigns the value on the right to a variable on the left. The == (double-equal) tests if two things have the same value.
# Every time you put " (double-quotes) around a piece of text you have been making a string. A string is how you make something that your program might give to a human. You print strings, save strings to files, send strings to web servers, and many other things.
