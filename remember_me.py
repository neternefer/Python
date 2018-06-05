import json

def get_stored_username():
	filename = "user_name.json"
	try:
		with open(filename) as f:
			username = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return username


def get_new_username():
	name = input("What is your name? ")
	filename = "user_name.json"
	with open(user_name, 'w') as f:
		json.dump(name, f)
	return name
	
def greet_user():
	username = get_stored_username()
	
	if username:
		print("Welcome back, " + username + "!")
	else:
		username = get_new_username()
		print("We'll remember you when you come back " + username + "!")
		

greet_user()
	


