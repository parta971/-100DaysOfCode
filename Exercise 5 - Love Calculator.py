# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
true_score=0
love_score=0
name=name1+name2 
name=name.lower()

true_score +=name.count("t")
true_score +=name.count("r")
true_score +=name.count("u")
true_score +=name.count("e")
love_score +=name.count("l")
love_score +=name.count("o")
love_score +=name.count("v")
love_score +=name.count("e")

sc=str(true_score)+str(love_score)
sc=int(sc)
if sc<10 or sc>90:
    print(f"Your score is {sc}, you go together like coke and mentos.")
elif sc>=40 and sc<=50:
    print(f"Your score is {sc}, you are alright together.")
else:
    print(f"Your score is {sc}")
