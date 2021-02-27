def factorial(n):
	
	i=0
	fact=1
	for i in range(1,n+1):
		fact=fact*i
	return fact	
def main():
	print("Enter no")
	no=int(input())
	fact1=factorial(no)
	print("Factorial of given no is",fact1)
if __name__=="__main__":
	main()

*************************output**************************
C:\Users\shree\Desktop\Python3\Assignments>python Assignment2_3.py
Enter no
5
Factorial of given no is 120