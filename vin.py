#using functions

#reading values 
a=int(input("enter value of a:"))
b=int(input("enter value of b:"))

#defining addition
def add():
	return a+b
#defining substration
def sub():
	return a-b
#defining multipication
def mul():
	return a*b
#defining division
def div():
	return a/b

print("addition=",add())
print("substration=",sub())
print("multiplication=",mul())
print("division=",div())