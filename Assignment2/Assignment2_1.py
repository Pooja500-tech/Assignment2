import Arithmetic1 as ar
def main():
	print("Enter Two no for operation")
	num1=int(input())
	num2=int(input())
	
	addition=ar.add(num1,num2)
	print("Addition is:",addition)
	
	subtraction=ar.sub(num1,num2)
	print("Subtraction is:",subtraction)
	
	multiplication=ar.mul(num1,num2)
	print("Multipication is:",multiplication)
	
	division=ar.div(num1,num2)
	print("Division is:",division)

if __name__=="__main__":
	main()

***************************output****************************
C:\Users\shree\Desktop\Python3\Assignments>python Assignment2_1.py
Enter Two no for operation
15
5
Addition is: 20
Subtraction is: 10
Multipication is: 75
Division is: 3.0