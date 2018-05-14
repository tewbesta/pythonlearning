def ex1():
    name= input("Please enter your name?"'\n')
    age = input("Please enter your age?"'\n')
    age = int(age)
    time = 100 - age
    year= 2018+ time
    print("Your name is" + name)
    print("Your age is " + str(age))
    print("You have " + str(time) +' years until you\'re a 100 years old')
    print("The year you turn a 100 is " + str(year))
    no= input("input the number of times you'd like to repeat the last message")
    print(int(no) * (" " + str(year)))

ex1()
def ex2():
    num = input("Please enter a number")
    if int(num) %2==0:
        print("You have entered an even number")
    else:
        print('You have entered an odd number')
ex2()

