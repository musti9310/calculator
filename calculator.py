
def main():
	number1=input("Enter the first number:")
	number2=input("Enter the second number:")
	operation=input("Choose the operation (+, -, /, *):")

	if number1.isnumeric() and number2.isnumeric():
		number1 = float(number1)
		number2 = float(number2)	
		if operation == "+":
			answer = number1 + number2
			print("The answer is %f" %(answer))
		elif operation == "-":
			answer = number1 - number2
			print("The answer is %f" %(answer)) 
		elif operation == '/':
			answer = number1 / number2
			print("The answer is %f" %(answer))
		elif operation == "*":
			answer = number1 * number2
			print("The answer is %f" %(answer))
		else:
			print('Invalid Input')

				

	else:
		print("Invalid Input")


	


	
				



if __name__ == '__main__':
	main()
