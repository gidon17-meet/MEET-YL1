n=input("please input a word, or at least a string of letters ;)")
letters=len(n)
opposite_word=""

x=len(n)-1
while x>=0:
	opposite_word+=n[x]
	x-=1
if opposite_word==n:
	print("True")
else: 
	print("False")
	

