import random
print ("Welcome to the rock, paper, scissors game! If you want to quit, press 'q'.")
while (input != "q"):
	user_answer = input ("Would you like select rock, paper, or scissors?\n")
	options = ["rock", "paper","scissors"]
	computer_answer = random.choice(options)
	
	

	if user_answer == "rock" or user_answer == "Rock" and computer_answer == "paper":
		print("Here is your answer:", user_answer,", and here is mine:", computer_answer, ". I win.")
	elif user_answer == "rock" or user_answer == "Rock" and computer_answer == "rock":
		print("Here is your answer:", user_answer,", and here is mine:", computer_answer, ".We tied!")
	elif user_answer == "rock" or user_answer == "Rock" and computer_answer == "scissors":
		print("Here is your answer:", user_answer,", and here is mine:", computer_answer, "You win!!")
	elif user_answer == "paper" or user_answer == "Paper" and computer_answer == "rock":
		print("You win!")
	elif user_answer == "paper" or user_answer == "Paper" and computer_answer == "paper":
		print("We tied!")
	elif user_answer == "paper"  or user_answer == "Paper" and computer_answer == "scissors":
		print("I win.")
	elif user_answer == "scissors" or user_answer == "Scissors" and computer_answer == "paper":
		print("You win!")
	elif user_answer == "scissors" or user_answer == "Scissors" and computer_answer == "scissors":
		print("We tied!")
	elif user_answer == "scissors" or user_answer == "Scissors" and computer_answer == "rock":
		print("I win.")
	else:
		print("That's not an answer, please try again or press 'q' to quit.")
	
