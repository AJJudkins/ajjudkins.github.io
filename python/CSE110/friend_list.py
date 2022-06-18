list_of_friends = []
name = None

while name != "end":
    name = input("What is the name of your friend? \n")
    if name != "end":
        list_of_friends.append(name)

print("Your friends are: ")
for friend in list_of_friends:
    print(friend)
