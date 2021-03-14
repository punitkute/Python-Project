import random 

def guess(x):
  random_number = random.randint(1,x)
  guess=0
  while guess != random_number:
    guess= int(input(f'Guess A Number Between 1 And {x}: '))
    if guess > random_number :
      print("Your Number Is Too Large. ")
      print("Please , Guess A Smaller Number: " )
      print(space)
    elif guess < random_number:
      print ("Your Number Is Too Small.")
      print("Please , Guess A Larger Number: ")
      print(space)
  
  print("YOU WIN !! You Guessed The Right Number.")
  print("Thanks For Playing The Game.")

space = ' ';
print("Welcome To Guessing Game ")
x= int(input("Give Us A Positive Number "))
if int(x) < 0:
  print("Invalid Input")
  print("Game Over")
else:
  guess(x) 