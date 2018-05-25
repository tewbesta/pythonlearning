def AboutWhileLoops():
    print("finally onto while loops, allers vous")
    x = 0
    while x < 3:  # this helps to loop until 3
        print(x)
        x += 1
    x = 0
    while x < 5:  # Conditional statements can be used in loops. Continue jumps out of conditional statements and continues  looping while break exists loop
        x += 1
        if x == 1:
            print("Welcome to loops")
        elif x == 2:
            continue
        elif x == 4:
            break
        print(x)
AboutWhileLoops()