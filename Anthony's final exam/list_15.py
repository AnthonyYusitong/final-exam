friends = ["Peter","Steven","Eric","Robin","Ben"]
for friend in friends:
	print(friend + " will travel with me")

friends.sort()
for frined in friends:
	print(friend + " will travel with me")

friends_sort = sorted(friends)

print ('\n')
for friend in friends_sort:
	print(friend + " (Sort)will travel with me")

friends.reverse()
print ('\n')
for friend in friends:
	print ('2 I want to go with '+ friend)
movies.reverse()
print ('\n')
for friend in friends:
	print ('3 I want to go with '+ friend)

friends.sort(reverse=False)
for friend in friends:
	print(friends)