#Exceptions
prompt = "Give me two numbers and I'll divide them."
prompt += "(press q to stop)"

while True:
	first_number = input("First number: ")
	if first_number == 'q':
		break
	second_number = input("Second number: ")
	if second_number == 'q':
		break
	try:
		result = int(first_number) / int(second_number)
	except ZeroDivisionError:
		print("Can't divide by zero!")
	else:
		print(result)
