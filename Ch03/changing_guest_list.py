guests = []
guests.append('Mary')
guests.append('Carrie')
guests.append('Matt')
print("Dear " + guests[0] + ", you're invited to dinner.")
print("Dear " + guests[1] + ", you're invited to dinner.")
print("Dear " + guests[2] + ", you're invited to dinner.")
print(guests[1] + " can't make it.")
guests[1] = "Adam"
print("Dear " + guests[0] + ", you're invited to dinner.")
print("Dear " + guests[1] + ", you're invited to dinner.")
print("Dear " + guests[2] + ", you're invited to dinner.")
