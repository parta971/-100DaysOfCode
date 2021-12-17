print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill=0
if height>=120:
  print("you can ride the rollercoaster")
  age=int(input("what is your age? "))
  if age<12:
    bill=5
    print("pay 5$")
  elif age<=18:
    bill=7
    print("pay 7$")
  elif age>=45 and age<=55:
    print("Having midlife crisis? Don't worry! have a free ride with us! everything will be okay!")
  else:
    bill=12
    print("pay 12$")
  
  wants_photo=input("Do you want a photo taken? Y or N: ")
  if wants_photo=='Y':
    bill+=3
  
  print(f"your final bill is {bill}$")
else:
  print("Sorry! you cant ride the rollercoaster")