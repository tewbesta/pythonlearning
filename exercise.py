#python learning like a pro, yeh Whatev
print("Welcome! Bien venue, Allers Vous!")
x="is"
y=" YoU   ArE ReadIng  DiS   "
print(y[1:3]) #displays from 2nd string to 4th
print(len(y)) #outputs length of y
print(y.strip()) #removes the white spaces at the start and end of the string
print(y.lower()) #converts all letter of Y into lower letters
print(y.upper()) #converts all letter of Y into upper letters
print(y.replace("R", "L")) #replaces the first capital R with L 
print(y.split("  ")) #splits y strings based on paramater given in brackets which is spaces
print("Let's learn about Lists, Sets, Tuples, Dictionaries, Conditions, Loops, Recursions and functions. Note: They are enclosed in functions(def... )for organization.")
def AboutLists():
 print("let's begin learning about lists, similar to arrays in c code")
 FirstList=["A", 'B', 'C', "d"]#one method to write lists
 SecondList=list(('Z', 'y', "x"))#another method to write lists using constructors(a method to initialize value with the  same name as the class it is in)
 FirstList.append("E")#method to add to lists
 SecondList.remove("Z")#method to remove lists
 print(FirstList)
 print(SecondList)
def AboutTuples():
 print("on to the next, Tuple: it's like lists with out single braces but unmodifiable easily, allers commence:)")
 FirstTuple=('T',"E","W",'B', "E",'S','T','A')
 SecondTuple=tuple(('G',"E","T",'A','C', "H",'E','W'))
 print(FirstTuple[3:7])#prints 4th string upto 7th  
 FirstTuple=FirstTuple," ", SecondTuple #This is a trick if you would like to modify a tuple by adding onto it
 print(FirstTuple)
 del FirstTuple #You can't edit tuple but you can delete it
 #This statement would be an error since tuples are unchageable...print(FirstTuple[3]='P')
def AboutSets():
 print( "let's now learn about sets(like lists but unordered, shall we?")
 FirstSet={'WAZZZZZ', 'UPPPP', '?'}#method to declare sets
 SecondSet=set(("Bruh","Sis"))#method to declare sets using constructors
 print(FirstSet)
 print(SecondSet)
 FirstSet.add("HOMZ:)") #method to add to sets
 print(FirstSet)
 FirstSet.remove("HOMZ:)")#method to remove from sets
 print(FirstSet)
 print(len(FirstSet)) #method to access length of sets
def AboutDictionaries():
 print("Now on to dictionaries, which are like the name suggests, lists with a description, comprende vous?")
 FirstDict={"You": "u", 'Eye':'I', 'Look':'lk'}
 SecondDict=dict(four="4", to="2")
 print(FirstDict)
 print(SecondDict)
 FirstDict['u']='you'#This is how you can alter the description of a dictionary, the parameter is the 2nd word (description) 
 print(FirstDict)
 FirstDict['You']='u'#Note how it's different when you write the first(main) word as the parameter. Now it outputs a   new  dictionary 'u':'You'
 print(FirstDict)
 del(FirstDict['Look'])
 print(FirstDict)
 print(len(FirstDict))
 print('Almost there, now we deal with conditions')
def AboutConditions():
 if (3>30):#condition statements, if a condition is satisfied, it runs th code. #Note: You can work with out an else  statement but if condition is not met, no code to run.
   print("yehhh right")
 else:
    print("ofcourse not")
def AboutWhileLoops():
 print("finally onto while loops, allers vous")
 x=0
 while x<3:#this helps to loop until 3
    print(x)
    x+=1
 x=0
 while x<5:#Conditional statements can be used in loops. Continue jumps out of conditional statements and continues  looping while break exists loop
    x+=1
    if x==1:
       print("Welcome to loops")
    elif x==2:
       continue
    elif x==4:
       break
    print(x)
def AboutForLoops():
 print("let's move to for loops shall we?")
 FirstList=["A", 'B', 'C', "d"]
 for x in FirstList:#FirstList is the list we created above
   print(x)
 for y in range(5):#the range operator starts from 0 until number in the parameter. Note this doesnot include the last  number ie 5
  if y==3:
    break  
  print(y)
 for y in range(2,7):#the range operator starts from 2 until 7
  if y==5:
    break
  print(y)  
 for y in range(3, 10, 2):#the range operator starts from 3 skipping 2 numbers until 10
    print(y)
print("let's learn about recursion shall we. This is also a way to loop. Note it's using a function.")
def FirstRecursion(k):
  if(k>0):
    result = k+FirstRecursion(k-1)
    print(result)
  else:
    result = 0
  return result#important to recurse(loop backwards by calling results as defined above
print("Recursion Results")
FirstRecursion(5)#gives a parameter from 0-5 that will be input to the above function 
print(AboutLists())
def MyProFunction(NickName):
    print("My nick name is "+NickName)
MyProFunction("T.YAWWWWW:)")
#We can also declare function parameter before calling it
def AnotherWay(Name="Tewbesta"):
  print("My name is "+ Name)
AnotherWay()
print("Yo name pleashh") 
name= input() #input will be saved as name
print("Bonjour"+ name.upper()+":)")