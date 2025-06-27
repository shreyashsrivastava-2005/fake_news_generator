import random

subjects = [
    "Virat Kohli",
    "Amitabh Bcchan",
    "A cricket team",
    "People on street",
    "A cat",
    "Tribal communities"
]

actions = [
    "dances with",
    "plays",
    "declared",
    "canceled",
    "injured",
    "fought with"
]

places_or_people = [
    " in Agra",
    "Selena Gomez",
    "the war",
    "event at night",
    "back of the shop",
    "at the hills",
]

while True:
   subject = random.choice(subjects)
   action = random.choice(actions)
   places = random.choice(places_or_people)
   
   headline = f"Breaking News: {subject} {action} {places}" 
   print("\n "+headline)
   
   user_input = input("Do you want another news(yes/no): ").strip().lower()
   
   if user_input == "no":
       break
   
print("Thankyou for using Fake news generator. Have a good day!")

