# creat a function that allows users to say there names and ages

def name_and_age():
    name = input('Enter your Name: ')
    age = int(input('Enter your age: '))
    city = input('Where do you live: ')
    return f'My Name is {name}, I am {age} years old and I live in {city}'

results = name_and_age()
print(results)
