def pattern(no):
	i=0
	j=0
	for i in range(1,no+1):
		for j in range(1,no+1):
			print(i,end=" ")
		print("\r")
def main():
 	
	print("Enter size.. ")
	n=int(input())
	pattern(n)

if __name__=="__main__":
	main()


**********************output*************************************
C:\Users\shree\Desktop\Python3\Assignments>python Assignment2_7.py
Enter size..
5
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5


