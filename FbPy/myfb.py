import fbchat
from getpass import getpass
username = input("Username: ")
client = fbchat.Client(username, getpass())
no_of_friends = int(raw_input("Number of friends: "))
for i in range(no_of_friends):
	name = input("Name: ")
	friends = client.searchForUsers(name) # return a list of names
	friend = friends[0]
	msg = input("Message: ")
	sent = client.sendMessage(msg, thread_id=friend.uid)
	if sent:
		print("Message sent successfully!")
