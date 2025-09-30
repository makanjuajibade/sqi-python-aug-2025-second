# Stage 1
confirmed_guests = ["Alice", "Charlie", "Eve", "Bob", "Frank", "Grace", "David", "Hannah", "Liam", "Mia"] 
waitlist = []
print("\n\nStage 1")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)


# Stage 2
waitlist.extend(["Ken", "Jack", "Ivy"])
print("\n\nStage 2")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 3
waitlist.append("Noah")
waitlist.append("Oliver")
print("\n\nStage 3")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 4
confirmed_guests.remove("Alice")
confirmed_guests.append("Ken")
del waitlist[0]
print("\n\nStage 4")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# # Stage 5
print("\n\nStage 5")
print("Charlie" in confirmed_guests)
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# # # Stage 6
del confirmed_guests[1]
del confirmed_guests[4]
print("\n\nStage 6")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# # Stage 7
confirmed_guests.append("Jack")
confirmed_guests.append("Ivy")
waitlist.remove("Jack")
waitlist.remove("Ivy")
print("\n\nStage 7")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# # Stage 8
waitlist.remove("Oliver")
print("\n\nStage 8")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 9
print("\n\nStage 9")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
last_three_confirmed_guests = confirmed_guests[-3:]
print("Last three confirmed guests:", last_three_confirmed_guests)

# Stage 10
confirmed_guests.append("Noah")
waitlist.clear()
print("\n\nStage 10")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 11
print("\n\nStage 11")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
num_of_confirmed_guests = len(confirmed_guests)
print("Number of confirmed guests:", num_of_confirmed_guests)

# Stage 12
confirmed_guests.sort()
print("\n\nStage 12")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 13
confirmed_guests.remove("Grace")
confirmed_guests.remove("Noah")
confirmed_guests.append("Collins")
confirmed_guests.sort()
print("\n\nStage 13")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)

# Stage 14
print("\n\nStage 14")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)
guests_list_for_caterer = confirmed_guests.copy()
print("Guest list for the caterer:", guests_list_for_caterer)

# Stage 15
waitlist.clear()
print("\n\nStage 15")
print("Confirmed guests: ", confirmed_guests)
print("Waitlist: ", waitlist)