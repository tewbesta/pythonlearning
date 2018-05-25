def AboutForLoops():
    print("let's move to for loops shall we?")
    FirstList = ["A", 'B', 'C', "d"]
    for x in FirstList:  # FirstList is the list we created above
        print(x)
    for y in range(
            5):  # the range operator starts from 0 until number in the parameter. Note this doesnot include the last  number ie 5
        if y == 3:
            break
        print(y)
    for y in range(2, 7):  # the range operator starts from 2 until 7
        if y == 5:
            break
        print(y)
    for y in range(3, 10, 2):  # the range operator starts from 3 skipping 2 numbers until 10
        print(y)
AboutForLoops()