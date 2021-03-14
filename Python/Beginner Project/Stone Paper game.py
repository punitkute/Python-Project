import random

def play():
  user = input("Enter 'r' for Rock , 'p' for Paper or  's' for scissor \n")
  computer = random.choice(['r', 'p', 's'])

  if(user == 'r') or (user == 'p') or (user == 's'):
   
    if user == computer:
      return 'MATCH IS TIE !'
  
    if is_win(user , computer):
      return 'CONGRATS! YOU WIN THE GAME!!'
    return 'YOU LOST! TRY AGAIN'

  else:
    return 'INVALID CHOICE.\nGAME OVER'
  
def is_win(player , opponent):
  # return true if player wins
  #r > s , s > p , p > r
  if(player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
    return True

print(play())
