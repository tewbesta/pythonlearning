def AboutDictionaries():
    print("Now on to dictionaries, which are like the name suggests, lists with a description, comprende vous?")
    FirstDict = {"You": "u", 'Eye': 'I', 'Look': 'lk'}
    SecondDict = dict(four="4", to="2")
    print(FirstDict)
    print(SecondDict)
    FirstDict[
        'u'] = 'you'  # This is how you can alter the description of a dictionary, the parameter is the 2nd word (description)
    print(FirstDict)
    FirstDict[
        'You'] = 'u'  # Note how it's different when you write the first(main) word as the parameter. Now it outputs a   new  dictionary 'u':'You'
    print(FirstDict)
    del (FirstDict['Look'])
    print(FirstDict)
    print(len(FirstDict))
    print('Almost there, now we deal with conditions')


AboutDictionaries()
