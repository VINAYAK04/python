a=['1','2','3','4','5','6','7','8','9']

def print_Bored():
	print(a[0],'|',a[1],'|',a[2])
	print("----------")
	print(a[3],'|',a[4],'|',a[5])
	print("----------")
	print(a[6],'|',a[7],'|',a[8])

playerOneturn = True
while True:
	print_Bored()
	p=input("Choose an avilable place : ")

	if(p in a):
		if(a[int(p)-1]=='X' or a[int(p)-1]=='O'):
			print("Place taken, choose another place...")
			continue
		else:
			if playerOneturn:
				print("Player 1 >>")
				a[int(p)-1] = 'X'
				playerOneturn = not playerOneturn
			else:
				print("Player 2 >>")
				a[int(p)-1] = 'O'
				playerOneturn = not playerOneturn
			for i in(0,3,6):
				if(a[i]==a[i+1] and a[i]==a[i+2]):
				   print("Game Over");
				   exit()
			for i in range(3):
			    if(a[i]==a[i+3] and a[i+6]):
			    print("Game Over...")	   
			    exit()

		else:
			continue    