def addfact(n):
	i=0
	sum=0
	for i in range(1,n):
		if n%i==0:
			sum=sum+i
			print(i)
	return sum
def main():
	print("Enter number")
	no=int(input())
	add=addfact(no)
	print("Addition of factor is:",add)
if __name__=="__main__":
	main()

*****************************output***************************
C:\Users\shree\Desktop\Python3\Assignments>python Assignment2_4.py
Enter number
14
1
2
7
Addition of factor is: 10
