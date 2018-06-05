def count_words(book):
	try:
		with open(book) as f:
			contents = f.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + book + " doesn't exist."
		print(msg)
		with open("missing_files.txt", 'w') as f:
			f.write(book)
	else:
	    words = contents.split()
	    num = len(words)
	    print("The file " + book + " has about " + str(num) + " words.")

	    
books = ["alice.txt", "bible.txt", "hamlet.txt"]
for book in books:
	    count_words(book)

with open("missing_files.txt") as f:
	files = f.read()
	print(files)
