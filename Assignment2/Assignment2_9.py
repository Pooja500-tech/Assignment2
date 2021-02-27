def size(n):
	i=0
	while(n>0):
		i=i+1
		n=n//10
	print("Number of digit in no",i)

def main():
	print("Enter no..")
	num=int(input())
	size(num)
	
if __name__=="__main__":
	main()
		
*************************output************************
C:\Users\shree\Desktop\Python3\Assignments>python Assignment2_9.py
Enter no..
456123
Number of digit in no 6
		