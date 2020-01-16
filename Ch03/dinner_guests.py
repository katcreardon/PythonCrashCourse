guests = ['Mary', 'Carrie', 'Matt']
print("Dear " + guests[0] + ", you're invited to dinner.")
print("Dear " + guests[1] + ", you're invited to dinner.")
print("Dear " + guests[2] + ", you're invited to dinner.")
print("\n")

print(guests[1] + " can't make it.")
guests[1] = 'Adam'
print("Dear " + guests[0] + ", you're invited to dinner.")
print("Dear " + guests[1] + ", you're invited to dinner.")
print("Dear " + guests[2] + ", you're invited to dinner.")
print("\n")

print("I found a bigger dinner table, so let's invite more guests.")
guests.insert(0, 'John')
guests.insert(2, 'Elizabeth')
guests.append('Fred')
print("\n")

print("Dear " + guests[0] + ", you're invited to dinner.")
print("Dear " + guests[1] + ", you're invited to dinner.")
print("Dear " + guests[2] + ", you're invited to dinner.")
print("Dear " + guests[3] + ", you're invited to dinner.")
print("Dear " + guests[4] + ", you're invited to dinner.")
print("Dear " + guests[5] + ", you're invited to dinner.")
print("\n")

print(str(len(guests)) + " guests are invited to dinner.")
