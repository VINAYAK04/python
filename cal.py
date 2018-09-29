#calcy program
i=int(input("enter value of i:"))
j=int(input("enter value of j:"))
o=input("what you want to do +-*/")

#defining addition 
def add(a,b):
	return a+b
#defining substration
def sub(a,b):
	return a-b
#defining multiplication
def mul(a,b):
	return a*b
#defining division
def div(a,b):
	return a/b

if(o=='+'):
   res=add(i,j)
elif(o=='-'):
	res=sub(i,j)
elif(o=='*'):
	res=mul(i,j)
elif(o=='/'):
	res=div(i,j)

print(res)