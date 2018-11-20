#there is still problem with the strings

from sys import exit

#redistribution
def redistribution():
    print("""
    Congratulations!
    This is the last part of our game..
    It is called redistribution part and
    you have to decide how much money you want to offer to another player.
    Your payoff will be decided according to your decisions of redistribution and...
    your luck! Your score is 1613.

    You have to allocate the units of a sum (your score and another player's score)
    in each case!

    """)

    score_one = input("There are 2413 units. How much money do you want to transfer to the other player?:")
    score_two = input("There are 1613 units. How much money do you want to transfer to the other player?:")
    score_three = input("There are 3226 units. How much money do you want to transfer to the other player?:")
    score_four = input("There are 3613 units. How much money do you want to transfer to the other player?:")

    thank_you("You have earned %r" %(score_three))

# case_one
def case_one():
    print("""
    \t In this part, you will be asked to complete a set of ​ math problems​.
    Your task is to fill the missing numbers and solve as many problems as you can.
    """)

    while True:
        try:
            answer_one = int(input("149 + 240. This is equal to: >"))
            break
        except:
            print("That's not a valid option!")
    if answer_one == 389:
        print("Correct!")
    else:
        thank_you("You need more practice!")

    while True:
        try:
            answer_two = int(input("300 + 158. This is equal to: >"))
            break
        except:
            print("That's not a valid option!")
    if answer_two == 458:
        print("Correct!")
    else:
        thank_you("You need more practice!")

    while True:
        try:
            answer_three = int(input("529 + 237. This is equal to: >"))
            break
        except:
            print("That's not a valid option!")
    if answer_three == 766:
        redistribution()
    else:
        thank_you("You need more practice!")

# case_two
def case_two():
    print("""
    \t In this part, you have to guess the number that I'm thinking.
    This is a number from 1 to 20​.
    Which is the correct number?
    """)

    while True:
        try:
            dice = int(input("Type a number here: > "))
            break
        except:
            print("That's not a valid option!")

    if dice == 12:
        redistribution()
    elif dice < 12:
        thank_you("It's not your lucky day!")
    elif dice > 20:
        thank_you("You should choose a number between 1 and 20!")
    else:
        print("You have another chance! Let's start again..")
        case_two()
#Questionnaire
def questionnaire():

    print("Where are you from?")
    nationality = input(">")

    print("How old are you?")
    age = input(">")

    print("Which is your education level?")
    education = input(">")

    print("Which is your occupation?")
    occupation = input(">")

    print("So, you are from %r, you are %r years old, your education level is %r and your occupation is %r. Thank you!" %(nationality, age, education, occupation))

    print("Now you have to choose one number from 1 to 10.")

    while True:
        try:
            question = int(input('Out of these options\(1,2,3...9,10), which is your favourite?'))
            break
        except:
            print("That's not a valid option!")

    if question < 5:  # PROBLEM
        case_one()
    elif question > 5:
        case_two()
    else:
        thank_you("We are sorry you cant continue!")

def thank_you(bye):
    print(bye, "Thank you for your participation!")
    exit(0)

def start():

    print(" Welcome! You are about to take part in an experiment, and we are very thankful for your participation.")
    print("First, you have to answer some personal informations.")
    print ("Are you ready?")

    ready = input(">")

    if ready == "yes":
        questionnaire()
    else:
        thank_you("We respect the fact that you dont want to share your info with us.")
start()
