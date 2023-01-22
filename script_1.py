# Intermediate Python Exercises 1 - Script #1
# Presley Gilliam - pgillia3@uncc.edu


# get_unique_list function
def get_unique_list(my_list):
    uniqueList = []

    # loops through each character in original list
    for eachChar in my_list:

        # if unique, add to unique list
        if eachChar not in uniqueList:
            uniqueList.append(eachChar)

    # return unique list
    return uniqueList


# sample test code
my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)
