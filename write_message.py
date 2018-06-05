filename = "programming.txt"

with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love new games.\n")
	
with open(filename, 'a') as f:
	f.write("I also like sleeping.")
	
with open(filename) as f:
	cont = f.read()
print(cont)
