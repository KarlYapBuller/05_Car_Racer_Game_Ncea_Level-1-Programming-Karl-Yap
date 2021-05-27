#Car Racer Game

#Higher Lower game

import random

#Number Checking Function goes here
def integer_check(question, low=None, high=None):

    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            #Question
            response = int(input(question))

            #Checks if response is not too low or too high
            #If both low and high are specified
            #If the response is too low or too high
            #Message will appear to the User instructing them what to do
            if situation == "both":
                if response < low or response > high:
                    print("Please enter a number between {} and {}".format(low, high))
                    continue

            #Checks response is not too low
            #If response it too low
            #Message will appear to the User instructing them what to do
            elif situation == "low only":
                if response < low:
                    print("Please enter a number that is more than (or equal to) {}".format(low))
                    continue

            elif response == "":
                print("Please input an integer")
                continue


            return response

        #Checks if response is an integer
        except ValueError:
            print("Please enter an integer.")
            continue

#Game Instructions
def game_instructions():
    statement_generator("How to play", "*")
    print("The goal of the Car Racer Game is to get to the race distance before the other cars you are racing.")
    print("You will be asked to pick a car (integer between 1 and 6), the ")
    print("race distance you want (integer between 5 and 15) and then you will be asked how many rounds you want to play (integer between 1 and 20).")
    print("Every round you play a random number out of 1 to 6 which represents the car numbers will be chosen and that car number will move one")
    print("race distance forward until one of the cars gets to the specified race distance you chose ")
    print("You will not be shown each step of the race just who wins the round because it would be very long to see each step and process.")
    print("You will need to press <Enter> to continue playing the game and 'xxx' to quit the game.")
    print("This should be all you need to know as the game is pretty easy to follow with instructions on the right input if you need it.")
    print("Good Luck")
    return""

#Played before function, output depends on what the user answers
#If the user answers yes, program continues ask user how many
#Rounds they want to play or if they want to play continuous mode
#If user answers no, game information will display
#If user answers anything other than yes/no, <error> please answer yes/no will appear
def played_before(question):
    valid = False
    while not valid:
        response = input(question).lower()
#If user response is either 'yes' or 'y' the response will be outputed as yes.
        if response == "yes" or response == "y":
            response = "yes"
            return response
#If user response is either 'no' or 'n' the response will be outputed as no.
        elif response == "no" or response == "n":
            response = "no"
            return response
#If user response is anything other than yes or no,user will be asked to answer yes or no.
        else:
            print("<error> please answer yes/no")

#Played before function, output depends on what the user answers
#If the user answers yes, program continues to show the
#Game summary which is in the game_history_statistics function
#If user answers no, User will be thanked for playing the game
#If user answers anything other than yes/no, <error> please answer yes/no will appear
def game_summary_question(question):
    valid = False
    while not valid:
        response = input(question).lower()
#If user response is either 'yes' or 'y' the response will be outputed as yes.
        if response == "yes" or response == "y":
            response = "yes"
            return response
#If user response is either 'no' or 'n' the response will be outputed as no.
        elif response == "no" or response == "n":
            response = "no"
            return response
#If user response is anything other than yes or no,user will be asked to answer yes or no.
        else:
            print("<error> please answer yes/no")

#Game Summary
def game_history_statistics():
    statement_generator("Game Summary", "*")
    for game in game_summary:
        print(game)
        print()
        print("Number of Races Won {} | Number of Races Lost {}".format(number_won, number_lost))
        print()

#Continue the game function
def continue_game(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "":
            return response

        #If response is not "" or 'xxx' Error message will display to the User
        else:
            print()
            print("<Error> please enter either <Enter> or 'xxx'")
            print()


#Statement generator
#Decorates the statements in the Car Racer Game
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

#Main Routine

#Welcomes User to the Car Racer Game
#Statement is decorated
statement_generator("Welcome to the Car Racer Game", "*")

#Calls ask user if they have played before funtion and game information function
#Played before statement is decorated
#If the user answers yes, program continues to ask the user how much they want to play with
#If user answers no, game information will display
#If user answers anything other than yes/no, <error> please answer yes/no will appear
print()
statement_generator("Played before", "?")
show_played_before = played_before("Have you played this game before (yes/no)? ")
print()

if show_played_before == "no":
    print()
    game_instructions()

#Loops the Higher Lower Game
game_loop = ""
while game_loop == "":

    #Tells the User the Higher Lower Game is going to begin
    statement_generator("Lets get Racing", "*")

    #Asks the User what they want as there Low Number
    car_number = integer_check("What is your Car number (Integer between 1 and 6)? ", 1, 6)
    #Ask the User how many rounds they want to play
    race_distance = integer_check("What is your race distance (Integer between 5 and 15)? ", 5, 15)
    #Ask the User how many rounds they want to play
    rounds = integer_check("How many rounds do you want to play (Integer between 1 and 20)? ", 1, 20)
    print()

    game_summary = []

    #Rounds Played
    rounds_played = 0
    #Number of rounds won
    number_won = 0

    #Number of rounds lost
    number_lost = 0


    #If the number of rounds played is less than the
    #Number of rounds the User wants to play the Higher Lower Game will continue
    while rounds_played < rounds:

        #If the number of rounds played is more than or equal to
        #One the User will be asked if they wish to continue the game or if they wish to
        #Quit the game they should input 'xxx'
        if rounds_played >= 1:
            print()
            game_loop = continue_game("Press <Enter> if you wish to continue the game, if you wish to quit type 'xxx': ")
            print()

        #If the User inputs 'xxx' when they are asked if they want to continue the game or not
        #The Game Loop will end
        if game_loop == "xxx":
            break

        #Cars
        car_number_1 = 0
        car_number_2 = 0
        car_number_3 = 0
        car_number_4 = 0
        car_number_5 = 0
        car_number_6 = 0

        #The Car that moves ahead one space is generated between the User's Lowest Number and Highest Number
        car_move_forward = random.randint(1, 6)

        #Indicates the round
        round_start = statement_generator("Round {} of {}".format(rounds_played + 1, rounds), "#")


        while car_number_1 != race_distance and car_number_2 != race_distance and \
                car_number_3 != race_distance and car_number_4 != race_distance and \
                car_number_5 != race_distance and car_number_6 != race_distance:

            #If the random number in the car_move_forward is 1 the car_number_1 will
            #increase by one and if the car number 1 is equal to the User's chosen race distance and if car
            #number 1 is the car the User chose the User is displayed that they won, if it is not the car the
            #User chose they are displayed that they lost that round

            if car_move_forward == 1:
                car_number_1 += 1
                if car_number_1 == race_distance:
                    car_win = "Car Number 1 wins"
                    if car_number == 1:
                        user_win_lost = "You Won ✔"
                        number_won += 1
                    else:
                        user_win_lost = "You lost ❌"
                        number_lost += 1
                    break

            #If the random number in the car_move_forward is 2 the car_number_2 will
            #increase by one and if the car number 2 is equal to the User's chosen race distance and if car
            #number 2 is the car the User chose the User is displayed that they won, if it is not the car the
            #User chose they are displayed that they lost that round

            if car_move_forward == 2:
                car_number_2 += 1
                if car_number_2 == race_distance:
                    car_win = "Car Number 2 wins"
                    if car_number == 2:
                        user_win_lost = "You Won ✔"
                        number_won += 1
                    else:
                        user_win_lost = "You lost ❌"
                        number_lost += 1
                    break

            #If the random number in the car_move_forward is 3 the car_number_3 will
            #increase by one and if the car number 3 is equal to the User's chosen race distance and if car
            #number 3 is the car the User chose the User is displayed that they won, if it is not the car the
            #User chose they are displayed that they lost that round

            if car_move_forward == 3:
                car_number_3 += 1
                if car_number_3 == race_distance:
                    car_win = "Car Number 3 wins"
                    if car_number == 3:
                        user_win_lost = "You Won ✔"
                        number_won += 1
                    else:
                        user_win_lost = "You lost ❌"
                        number_lost += 1
                    break

            #If the random number in the car_move_forward is 4 the car_number_4 will
            #increase by one and if the car number 4 is equal to the User's chosen race distance and if car
            #number 4 is the car the User chose the User is displayed that they won, if it is not the car the
            #User chose they are displayed that they lost that round

            if car_move_forward == 4:
                car_number_4 += 1
                if car_number_4 == race_distance:
                    car_win = "Car Number 4 wins"
                    if car_number == 4:
                        user_win_lost = "You Won ✔"
                        number_won += 1
                    else:
                        user_win_lost = "You lost ❌"
                        number_lost += 1
                    break

            #If the random number in the car_move_forward is 5 the car_number_5 will
            #increase by one and if the car number 5 is equal to the User's chosen race distance and if car
            #number 5 is the car the User chose the User is displayed that they won, if it is not the car the
            #User chose they are displayed that they lost that round

            if car_move_forward == 5:
                car_number_5 += 1
                if car_number_5 == race_distance:
                    car_win = "Car Number 5 wins"
                    if car_number == 5:
                        user_win_lost = "You Won ✔"
                        number_won += 1
                    else:
                        user_win_lost = "You lost ❌"
                        number_lost += 1
                    break

            #If the random number in the car_move_forward is 6 the car_number_6 will
            #increase by one and if the car number 6 is equal to the User's chosen race distance and if car
            #number 6 is the car the User chose the User is displayed that they won, if it is not the car the
            #User chose they are displayed that they lost that round

            if car_move_forward == 6:
                car_number_6 += 1
                if car_number_6 == race_distance:
                    car_win = "Car Number 6 wins"
                    if car_number == 6:
                        user_win_lost = "You Won ✔"
                        number_won += 1
                    else:
                        user_win_lost = "You lost ❌"
                        number_lost += 1
                    break

        print("Car That Wins The Round: {}, it reached the race distance of {} first".format(car_win, race_distance))
        print("Car That You Chose: Car Number {}".format(car_number))
        print("Result: {}".format(user_win_lost))


        #The Game Summary
        game_summary.append("Round: {}| Result: {}| Your Car Chosen: Car Number {}| Car That Won: {}".format(rounds_played + 1, user_win_lost, car_number, car_win))

        #Increases the rounds played by 1
        rounds_played += 1

    #Calls game summary question function
    #Game Summary statement is decorated
    #If the user answers yes, program continues to show the
    #User the game summary which includes the game history and statistics
    #User will be thanked for playing the game
    #If user answers no, User will be thanked for playing the game
    #If user answers anything other than yes/no, <error> please answer yes/no will appear
    print()
    statement_generator("Game Summary", "?")
    show_game_summary_question = game_summary_question("Do you want to see your Game Summary (yes/no)? ")
    print()

    if show_game_summary_question == "yes":
        print()
        game_history_statistics()

    #Thanks the User for playing the Car Racer Game
    statement_generator("Thank you for playing the Car Racer Game", "*")

    #If the User wants to play the Car Racer Game again the game will loop from the start
    print()
    game_loop = continue_game("Press <Enter> if you wish to continue the game, if you wish to quit type 'xxx': ")
    print()
