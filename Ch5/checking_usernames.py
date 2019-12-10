current_users = ['user1', 'user2', 'user3', 'user4', 'user5']

new_users = ['user6', 'user7', 'User2', 'user3', 'user8']

for new_user in new_users:
    if new_user.lower() in current_users:
        print("\nYou will need to enter a new username.")
    else:
        print("\nThat username is available.")