from random import randint	# Imports the randint method from the module random

player_wins = 0
computer_wins = 0
winning_score = int(input("What do you want the winning score to be? "))
while player_wins < winning_score and computer_wins < winning_score:	# While both the player and the computer have fewer than the winning number of points:
	print("...rock... \n....paper... \n....scissors....")
	choice1= input("Enter Your Move: ").lower()
	if choice1 == "quit":	# allows the user to quit by typing "quit"
		break
	rand_num = randint(0,2)	# Picks either 0, 1, or 2.
	if rand_num == 0:
		computer = "rock"
	elif rand_num == 1:
		computer = "paper"
	else:
		computer = "scissors"
	print(f"the computer played {computer}")
	if choice1:
		if choice1 == computer:
			print("tie!")
		elif choice1 == "rock":
			if computer == "paper":
				print ("computer wins!")
				computer_wins += 1
			if computer == "scissors":
				print("You win!")
				player_wins += 1
		elif choice1 == "paper":
			if computer == "rock":
				print ("You win!")
				player_wins +=1
			if computer == "scissors":
				print ("computer wins!")
				computer_wins += 1
		elif choice1 == "scissors":
			if computer == "rock":
				print ("computer wins!")
				computer_wins += 1
			if computer == "paper":
				print ("You win!")
				player_wins += 1
	else: 
		print("Please enter a valid move, or 'quit' to quit")	# If the user does not enter a valid move, this runs
print (f"Computer: {computer_wins}")
print (f"Player: {player_wins}")
if int(computer_wins) > int(player_wins):
	print (f"The computer wins this round!, {computer_wins} to {player_wins}")
elif int(player_wins) > int(computer_wins):
	print (f"The human wins this round, {player_wins} to {computer_wins}")
elif player_wins == computer_wins:
	print("It's a tie!")