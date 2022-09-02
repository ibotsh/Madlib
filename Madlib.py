print("Welcome!")
print("Lets play Madlibs! Please enter the following ↓")

adj = input("Type in an adjective: ")
verb1 = input("Type in a verb: ")
verb2 = input("Type in another verb: ")
famous_person = input("Lastly, type in a famous person: ")

madlib = "Games are so {adj}, they make me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you're {famous_person}".format(adj=adj, verb1=verb2, verb2=verb2, famous_person=famous_person)

print(madlib)
