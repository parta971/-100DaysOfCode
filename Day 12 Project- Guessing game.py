import random
from Art import logo

print(logo)

def set_level():
  level=input("Choose a difficulty. Type 'easy' or 'hard':").lower()
  if level=='easy':
    return 10
  elif level=='hard':
    return 5
  else:
    print("Wrong input!")


def game():
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
  number=random.randint(1,100)
  #print(f"Pssst, the correct answer is {number}")
  turns=set_level()
  loop=True
  while loop:
    print(f"You have {turns} left!")
    guess=int(input("Guess a number: "))

    if number>guess:
      print("To Low\nGuess Again:")
      turns-=1
    elif number<guess:
      print("To High\nGuess Again:")
      turns-=1
    elif number==guess:
      print(f"You Guessed it!! The number was {number}")
      loop=False
    if turns==0:
      print(f"You loose! {turns} left! The number was: {number}")
      loop=False
  
game()



