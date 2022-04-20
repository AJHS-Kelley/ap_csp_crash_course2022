# This program will model a game of rock, paper, scissors.

player1_choice = " " # Set to an empty string value.
player2_choice = " " # Set to an empty string value.

possible_choices = ["Rock", "Paper", "Scissors"] # List of choices.

player1_score = 0
player2_score = 0
# Create player score variables, start them at 0. 

#def example_function(): # Defining the function. 
    #print("This is an example function.")
    #print("It will only run when the function is called.")
    #print(possible_choices)

#example_function() # This calls the function.

def display_introduction():
    print("Hello, there!")
    print("This program will play rock, paper, scissors with you.")
    print("You will make a choice of rock, paper, or scissors.")
    print("The computer will do the same.")
    print("Then, the winner will be declared using these rules:")
    print("Rock beats scissors, paper beats rock, and scissors beats paper.")

display_introduction() 
