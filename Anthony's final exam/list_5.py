countries = ["china","Japan","Rusia","Turkey"]
for country in countries:
	print("I want to visit " + country)
	
print ('I am going to '+str(len(countries))+' countries')

print("I can't pay a visit to " + countries[3])

countries.remove("Turkey")
countries.insert(3,"USA")
