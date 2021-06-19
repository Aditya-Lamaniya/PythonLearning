# A non returning function

def average(a, b): print("average of given value is ", (a + b) / 2)


average(10, 20)


# a function that return value

def average(a, b): return (a + b) / 2


result = average(10, 20)
print("the average of given numbers is =:", result)


# a function that returns multiple value

def calc(a, b): return (a + b) / 2, a + b, a - b, a / b, a * b, a % b


result= calc(10, 20)
print('all the operations are as follow  =:', result)

