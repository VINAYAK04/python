#dictionary
import random 
a={1:'r',2:'p',3:'s'}

c=a[random.randint(1,3)]

user_input=input("enter rock paper scissor")
print("computer puts ",c)

#condition
if(user_input=='r'and c=='s' or user_input=='p'and c=='r' or user_input=='s'and c=='r'):
	 print("you won")

else:
	print("you lose!!!")