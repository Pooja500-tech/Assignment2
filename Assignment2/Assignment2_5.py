def prime(n):
	if n>1:
		for i in range(2,n):
			if (n%i)==0:
				print(n,":is Not Prime")
				break
		else:
			print(n,":is Prime")
	else:
		print(n,":is Not Prime")
def main():
	print("Enter number to check")
	no=int(input())
	prime(no)
if __name__=="__main__":
	main()
*****************************output*****************************
C:\Users\shree\Desktop\Python3\Assignments>python Assignment2_5.py
Enter number to check
5
5 :is Prime

C:\Users\shree\Desktop\Python3\Assignments>python Assignment2_5.py
Enter number to check
6
6 :is Not Prime	