def AboutLists():
    print("let's begin learning about lists, similar to arrays")
    FirstList = ["A", 'B', 'C', "d"]  # one method to write lists
    SecondList = list(('Z', 'y', "x"))  # another method to write lists using constructors(a method to initialize value with the  same name as the class it is in)
    print(FirstList)
    print(SecondList)
    FirstList.append("E")  # method to add to lists
    SecondList.remove("Z")  # method to remove lists
    print(FirstList)
    print(SecondList)


AboutLists()
