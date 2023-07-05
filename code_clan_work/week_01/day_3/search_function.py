# Using Loops to Search Lists

chickens = [
	{ "name": "Margaret", "age": 2, "eggs": 0 },
	{ "name": "Hetty", "age": 1, "eggs": 2 },
  { "name": "Henrietta", "age": 3, "eggs": 1 },
  { "name": "Audrey", "age": 2, "eggs": 0 },
  { "name": "Mabel", "age": 5, "eggs": 1 },
]

# print(chickens[2]["eggs"])

for chicken in chickens:
	if chicken["name"] == "Henrietta":
		num_eggs_henrietta = chicken["eggs"]
print(num_eggs_henrietta)

audrey_found = False
for chicken in chickens:
	if chicken["name"] == "Audrey":
		print(chicken)
		audrey_found = True
if audrey_found == False:
	print("Audrey wasn't found!")