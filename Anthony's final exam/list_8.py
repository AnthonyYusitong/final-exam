countries = ["china","Japan","Rusia","Turkey"]
for country in countries:
	print("I want to visit " + country)
	
print ('I am going to '+str(len(countries))+' countries')

print("I can't pay a visit to " + countries[3])

countries.remove("Turkey")
countries.insert(3,"USA")

countries = ["china","Japan","Rusia","USA"]

for country in countries:
	print("I am glad to visit " + country)

countries_extra = ["India","UK","Thailand"]
for country in countries_extra:
	print("I gonna travel to " + country)

print("I have more travel funds!")

countries_extra.insert(3,"Australia")
for country in countries_extra:
	print("I want to go to " + country)
	

