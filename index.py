# a function that allows users to say there names and ages

def name_and_age():
    name = input('Enter your Name: ')
    age = int(input('Enter your age: '))
    city = input('Where do you live: ')
    return f'My Name is {name}, I am {age} years old and I live in {city}'

results = name_and_age()
print(results)

# function for listing items to go back to school

def back_to_school_items():
    item_1 = input('Which setbook do you need: ')
    item_2 = input('What sport uniform would you like? ')
    item_3 = input('Which type of shoes do you need? ')
    return f'The list of items I need are {item_1}, {item_2} and, {item_3}'

shopping_items = back_to_school_items()
print(shopping_items)
