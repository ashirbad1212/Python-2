#Get the key corresponding to the minimum value from the following dictionary using appropriate python logic.

# initializing the dictionary
testing_the_dict = {'Physics': 88, 'maths': 75, 'Chemistry': 72, 'baisc electrical engineering': 89}

# printing the original dictionary
print("The original dictionary is : " + str(testing_the_dict))

# Finding min value keys in dictionary
temp = min(testing_the_dict.values())
res = [key for key in testing_the_dict if testing_the_dict[key] == temp]

# printing result
print("Keys with minimum values are : " + str(res))