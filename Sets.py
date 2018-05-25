def AboutSets():
    print("let's now learn about sets(like lists but unordered, shall we?")
    FirstSet = {'WAZZZZZ', 'UPPPP', '?'}  # method to declare sets
    SecondSet = set(("Bruh", "Sis"))  # method to declare sets using constructors
    print(FirstSet)
    print(SecondSet)
    FirstSet.add("HOMZ:)")  # method to add to sets
    print(FirstSet)
    FirstSet.remove("HOMZ:)")  # method to remove from sets
    print(FirstSet)
    print(len(FirstSet))  # method to access length of sets
AboutSets()