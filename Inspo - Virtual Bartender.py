#virtual bartender
from random import choice


drinks = ("vodka","whiskey","gin","tequila","rum","rakia","sake")
print("Welcome to the virtual pub")
name= input("I am the virtual bartender, how do I call you? ")
try:
   age=input(f"How old are you {name}? ")
   age=int(age)
   if age >=21:
       legal = True
   elif age<16:
       legal=False
   else:
       print("Based on your age, i need to ask you where are you from")
       country=input(f"Where are you from {name}? ")
       legal= False
       if age>=21:
           legal= True
       elif age >=18 and country != "USA":
           legal=True
       elif age >=16 and country == "Luxembourg":
           legal=True
   if legal:
       print("You are allowed to drink")
       print(f"Here is a {choice(drinks)} for you")
   else:
       print(f" I cannot serve you {name}")
   if age>120 or age<5:
       print(f"Please do not lie to your virtual bartender")
except ValueError:
   print("Please enter a valid age")
