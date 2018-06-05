#When using WITH keyword, you don't need to close the file
with open('pi_digits.txt') as file_object:
	read_data = file_object.read()
	print(read_data.rstrip())
	
with open('pi_digits.txt') as f:
	for line in f:
		print(line.rstrip())
		
with open('pi_digits.txt') as f:
	lines = f.readlines()
	
pi_string = ''
for line in lines:
	pi_string += line.rstrip()
	
print(pi_string)
print(len(pi_string))
