def locate_card(cards, query):

    #Create a positional variable with value 0
    position = 0

    #set up a oop for repetaition
    while True:

        #Check if the current position matches the query
        if cards[position] == query:

            #Answer found! Return and Exiit
            return position

        #increment the position
        position += 1

        #if we have reached the end of array
        if position == len(cards):

            #Number not found and will return position as -1

            return -1


# Creating a test case for our function
test = {
    'inputs' : {
        'cards' : [13, 11, 10, 7, 4, 3, 1, 0],
        'query' : 7
    },
    'output' : 3
}
#cehcking the result
result = locate_card(**test['inputs'])
output = test['output']

print(result)
print(result == output)


from jovian.pythondsa import evaluate_test_case # importing test cases to check our result
