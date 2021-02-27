def star(n):
	j=0
	i=0
	for i in range(0,n+1):
		for j in range(0,i):
			print("*",end=" ")
		print("\r")
def main():
	print("enter cnt")
	no=int(input())
	star(no)

if __name__=="__main__":
	main()

*****************************output**************************
C:\Users\shree\Desktop\Python3\Assignments>python Assignment2_6.py
enter cnt
5

*
* *
* * *
* * * *
* * * * *