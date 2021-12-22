#Write your code below this line 👇
def prime_checker(number):
    if n%2==0 or n%3==0 or n%5==0 or n%7==0:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
