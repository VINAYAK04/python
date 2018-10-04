import random
a=['r','p','s']
x=0
y=0
while (True):
	p=input("Your choice r/p/s: ")
	c=random.choice(a)

	print("Your choice",p,"computer choice",c)
	if(p=='r' or p=='p' or p=="s"):
		if(p==c ):
			print("tie")
		elif((p=='r' and c=='p') or (p=='p' and c=='s') or (p=='s' and c=='r')):
			x=x+1
			print("computer won",x,"times")
		else:
			y=y+1
			print("U Won",y,"times")
		else:
			print("Give proper input")
			break
		if(x=3 or y=3):
			if(x==3):
				print("I'M Sorry,computer Won the game")
		else:
			print("Congrats U Won against computer, have a great day")
			break	