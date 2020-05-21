#1.Create an inner function to calculate the addition in the following way
#	Create an outer function that will accept two parameters ‘a’ and ‘b’
#Create an inner function inside an outer function that will calculate the addition of ‘a’ and ‘b’
#•	At last, an outer function will add 5 into addition and return it

def outerFunction(a, b):

    def innerFunction(a,b):
        return a+b
    sum = innerFunction(a, b)
    return sum+5

result = outerFunction(15, 20)
print(result)