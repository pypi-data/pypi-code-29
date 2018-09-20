
# https://www.digitalocean.com/community/tutorials/how-to-make-a-simple-calculator-program-in-python-3


def calc(num_1, operation, num_2):

    number_1 = int(num_1)
    number_2 = int(num_2)

# operation = input('''
# Please type in the math operation you would like to complete:
# + for addition
# - for subtraction
# * for multiplication
# / for division
# ''')

# number_1 = int(input('Enter your first number: '))
# number_2 = int(input('Enter your second number: '))

    if operation == '+':
        result = number_1 + number_2
        print('{} + {} = {}'.format(number_1, number_2, result))
        return result

    elif operation == '-':
        result = number_1 - number_2
        print('{} - {} = {}'.format(number_1, number_2, result))
        return result

    elif operation == '*':
        result = number_1 * number_2
        print('{} * {} = {}'.format(number_1, number_2, result))
        return result

    elif operation == '/':
        result = number_1 / number_2
        print('{} / {} = {}'.format(number_1, number_2, result))
        return result

    else:
        print('You have not entered a valid operator.')
