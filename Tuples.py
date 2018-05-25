def AboutTuples():
    print("on to the next, Tuple: it's like lists with out single braces but unmodifiable easily, allers commence:)")
    FirstTuple = ('T', "E", "W", 'B', "E", 'S', 'T', 'A')
    SecondTuple = tuple(('G', "E", "T", 'A', 'C', "H", 'E', 'W'))
    print(FirstTuple[3:7])  # prints 4th string upto 7th of FirstTuple
    FirstTuple = FirstTuple, " ", SecondTuple  # This is a trick if you would like to modify a tuple by adding onto it
    print(FirstTuple)
    del FirstTuple  # You can't edit tuple but you can delete it
    # This statement would be an error since tuples are unchageable...print(FirstTuple[3]='P')
AboutTuples()