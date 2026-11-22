beatles = []

beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

for name in ["Stu Sutcliffe", "Pete Best"]:
    beatles.append(input("Enter " + name + ": "))

del beatles[3]
del beatles[3]

beatles.insert(0, "Ringo Starr")

print(beatles)
