usernames = ['admin', 'user1', 'user2', 'user3', 'user4']

if usernames:
    for user in usernames:
        if user == 'admin':
            print("\nHello admin, would you like to see a status report?")
        else:
            print("\nHello " + user + ", thank you for logging in again.")
else:
    print("\nWe need to find some users!")