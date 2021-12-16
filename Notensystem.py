Note = float(input("Gib deine Note ein: "))
if Note >= 5.5:
    print("Deine Note im amerikanischen System ist A")
elif Note < 5.5 and Note >= 4.5:
    print("Deine Note im amerikanischen System ist B")
elif Note < 4.5 and Note >= 4.0:
    print("Deine Note im amerikanischen System ist C")
else:
    print("Deine Note im amerikanischen System ist F")