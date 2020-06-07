#import modules
import random


#starting the game & options
options = ["rock", "paper","scissors"]
comp_choice = random.choice(options)
print("Welcome to a game of Rock , Paper , Scissors !")
user_option = raw_input("What is your choice?")
print('Your choice is ' + user_option)
print('Computer Choice is ' + comp_choice)


#logic of the game
# Rock vs Paper --> paper wins
# Scissors vs rock --> rock wins 
# Paper vs Scissors --> Scissors wins

if user_option == comp_choice:
  print('It is a draw!')
elif user_option == "rock" :
     if comp_choice == "scissors" :
         print('You have won! ;)')
     elif comp_choice == "paper" :
         print('You lose :( Better luck next time!')
elif user_option == "scissors" :
     if comp_choice == "paper" :
         print('You have won! ;)')
     elif comp_choice == "rock" :
         print('You lose :( Better luck next time!')
elif user_option == "paper" :
     if comp_choice == "rock" :
         print('You have won! ;)')
     elif comp_choice == "scissors" :
         print('You lose :( Better luck next time!')
  