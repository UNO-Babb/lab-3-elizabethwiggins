#RPS.py
#Name:
#Date:
#Assignment:
import random

def main():
  
  wins = 0  
  ties = 0  
  losses = 0

  playAgain= "Y"
  while playAgain=="Y":
    #Create a loop that continues as long as the user wants to play.
    #User can play as many games as they wish.

    #Randomly choose the computer between 'R', 'P', or 'S'
   
    #Prompt the user for their RPS selection
    player=input("Select Rock Paper or Scissors (R, P, or S):")
    computer=(random.choice(["R", "P", "S"]))
    #Determine winner and state what happened to the user
    if computer=="R":
      print("Computer Chose Rock")
    elif computer=="P":
      print ("Computer Chose Paper")
    else:print 
    ("Computer Chose Scissors")

    if player=="R":
      print("Player Chose Rock")
    elif player=="P":
      print ("Player Chose Paper")
    else:
      print ("Player Chose Scissors")

    if player=="R" and computer=="R":
      print("Tie")
    ties= ties + 1
    if player=="R" and computer=="P":
        print ("Computer wins.")
        losses= losses + 1
    if player== "R" and computer== "S":
        print ("You win!")
        wins= wins + 1

    if player == "P" and computer== "R":
      print ("You win!")
      wins= wins + 1
    if player=="P" and computer=="P":
      print ("Tie")
      ties=ties + 1
    if player== "P" and computer=="S":
      print ("Computer wins.")
      losses= losses + 1

    if player=="S"and computer=="R":
      print ("Computer wins.")
      losses= losses + 1
    if player== "S" and computer== "P":
      print ("You win!")
      wins= wins + 1
    if player== "S" and computer== "S":
      print ("Tie")
      ties= ties + 1

    


    #Ask the user if they would like to play again.
    playAgain=input("Play again? (Y/N):")
    
  #In the end, print the stats
  print("Wins \t Ties \t Losses")
  print("---- \t ---- \t ------")
  print(wins, "\t", ties , "\t", losses)

if __name__ == '__main__':
  main()
