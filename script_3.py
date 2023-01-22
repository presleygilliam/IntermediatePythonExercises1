# Intermediate Python Exercises 1 - Script #3
# Presley Gilliam - pgillia3@uncc.edu

# function to count usage of each letter in string
def letterUsage(origString):

    # set string to lowercase values without spaces and create dict
    noSpaces = origString.replace(" ", "")
    lowerString = noSpaces.lower()
    strDict = {}

    # loop through each character in string
    for char in lowerString:

        # calculate character count and add to dict
        count = lowerString.count(char)
        strDict[char] = count

    print(strDict)


# prompt user to input string and call function
stringInput = input('Enter a string: ')
letterUsage(stringInput)
