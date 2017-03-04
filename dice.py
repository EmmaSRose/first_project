import random
#print(random.randint(1,6))
print(" Hello! Welcome to Dice")

done = False

while not done:
	n = random.randint(1,6)
	print(" Your number is " + str(n))
	print("Would you like to play again? [y/n]")
	response = raw_input()
	if response == 'n':
		print("game over.")
		done = True