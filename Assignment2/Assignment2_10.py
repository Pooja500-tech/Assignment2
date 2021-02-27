def size(n):
	i=0
	sum=0
	while(n>0):
		i=i+1
		sum=sum+(n%10)
		n=n//10
	print("sum is :",sum)

def main():
	print("Enter no..")
	num=int(input())
	size(num)
	
if __name__=="__main__":
	main()
***************************output****************************
C:\Users\shree\Desktop\Python3\Assignments>python Assignment2_10.py
Enter no..
4567
Sum is: 22