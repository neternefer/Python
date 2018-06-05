import json

filename = "numbers.json"

with open(filename) as f:
	contents = json.load(f)
	
print(contents)
