import random

name=input("ENTER YOUR NAME : ")
print("HELLO",name,"WELCOME TO NUMBER GUESSING GAME")

start_range=int(input("ENTER STARTING VALUE FOR THE RANGE: "))
end_range=int(input("ENTER ENDING VALUE FOR THE RANGE: "))

random_number = random.randint(start_range, end_range)

guess_count = 0
user_guess = None


while user_guess != random_number:
  guess_count += 1
  user_guess = int(input(f"GUESS A NUMBER BETWEEN {start_range} AND {end_range} :"))

  if user_guess == random_number:
    print("GREAT! YOU GUESSED THE NUMBER IN",guess_count,"tries.")
  elif user_guess < random_number:
    print("YOUR GUESS IS LOW. TRY AGAIN.")
  else:
    print("YOUR GUESS IS HIGH. TRY AGAIN.")



