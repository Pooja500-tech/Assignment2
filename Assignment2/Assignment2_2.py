def star1(value):
	i=0;
	j=1;
	for i in range(0,value):
		for j in range(0,value):
			print("*",end=" ")
		print("\r")
			
		
def main():
	print("Enter count")
	cnt=int(input())
	star1(cnt)
if __name__=="__main__":
	main()

**********************output****************************
C:\Users\shree\Desktop\Python3\Assignments>python Assignment2_2.py
Enter count
5
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *