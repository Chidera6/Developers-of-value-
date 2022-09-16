"This is a temperature converter that takes input from a user and returns the value in degree celsuis"
temp = input("Enter a current temperature measurement in fahrenheit or kelvin:")
if temp.endswith('K'):
    y = float(temp.replace("K", ""))
    new_temp = y / 273.15
    print(f'the temperature of {temp} is equivalent to {new_temp}C')
elif temp.endswith('F'):
    y = float(temp.replace("F", ""))
    new_temp = y * (100/212)
    print(f'the temperature of {temp} is equivalent to {new_temp}C')
else:
    print(f'the temperature of {temp} is equivalent to {temp}')

