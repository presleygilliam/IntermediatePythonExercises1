# Intermediate Python Exercises 1 - Script #4
# Presley Gilliam - pgillia3@uncc.edu

# declare vars
inputNum = 0
sumOfInput = 0
userInput = 0

# loop until user inputs 5 valid integers
while inputNum < 5:

    finished = False
    while finished != True:

        # try catch block to determine if user is inputting an integer
        try:
            # prompt user to input value
            userInput = int(input('Enter int #' + str(inputNum + 1) + ': '))
            finished = True
        except:
            # print error message if not an integer
            print('Invalid input. Please enter an int.')

    # add to sum and increase count for loop
    sumOfInput = sumOfInput + userInput
    inputNum = inputNum + 1

# prints sum to user
print('Your sum is ' + str(sumOfInput))
