my_dict = {"name":"john", "occupation":"student", "favorite_food": "panda_express"}

print(my_dict.values())
print(my_dict.keys())
print([k for k,v in my_dict.items() if v == "john"])
print([k for k,v in my_dict.items() if v in ("john","panda_express")])

my_dict['new_key'] = 'new_value'
print(my_dict)

meals = {
	"breakfast": "eggs", 
	"lunch":"pasta", 
	"dinner":"fish"}
print([v for k,v in meals.items() if k in ("breakfast","lunch")])

del meals["breakfast"]
print(meals)

people = {
  "john":31,
  "bob":20,
  "sandra":41
}

people["steve"] = 27
people["bob"] = 19
del people["sandra"]
print(people)

countries = {
	"uk":{
		"capital":"London",
		"population": 1000
	},
	"germany":{
		"capital":"Berlin",
		"population": 200
	}
}

print(countries)
print(countries["germany"]["population"])