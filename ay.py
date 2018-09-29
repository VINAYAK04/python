import random
while True:
	i=input("Press n to quit")
	if(i=='n'):
		print("bye")
		exit()
	else:
		print("you got",random.randint(1,6))