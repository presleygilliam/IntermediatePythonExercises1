# Intermediate Python Exercises 1 - Script #2
# Presley Gilliam - pgillia3@uncc.edu


def get_combined_dict(my_dict_1, my_dict_2):

    # dictonary for combined list
    dictFinal = {}

    # loops through dict elements
    for element in my_dict_1:

        # gets common keys
        if element in my_dict_2:

            # gets number values from each list with common key
            value1 = my_dict_1[element]
            value2 = my_dict_2[element]

            # calculates total and appends to dict
            total = value1 + value2
            dictFinal[element] = total

    return dictFinal


# sample test code
my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
