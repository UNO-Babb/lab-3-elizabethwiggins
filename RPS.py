#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  wins = 0
  ties = 0
  losses = 0
  #Create a loop that continues as long as the user wants to play.
  #User can play as many games as they wish.

  #Randomly choose the computer between 'R', 'P', or 'S'
  import random
  #Prompt the user for their RPS selection
  input("Select Rock Paper or Scissors (R, P, or S):")
  response=print("Computer chose: ");print(random.choice(["Rock", "Paper", "Scissors"]))
  #Determine winner and state what happened to the user
  #Ask the user if they would like to play again.
  input("Play again? (Y/N):")

  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
