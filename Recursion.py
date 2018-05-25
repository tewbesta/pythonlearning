print("let's learn about recursion shall we. This is also a way to loop. Note it's using a function.")
def FirstRecursion(k):
    if (k > 0):
        result = k + FirstRecursion(k - 1)
        print(result)
    else:
        result = 0
    return result  # important to recurse(loop backwards by calling results as defined above


print("Recursion Results")
FirstRecursion(5)  # gives a parameter from 0-5 that will be input to the above function)