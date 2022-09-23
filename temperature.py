
def temperature_converter(num):
    "This is a temperature converter function that takes input from a user and returns the value in degree celsuis"
    
    if num.endswith('K') or num.endswith('k'):
        x = num.upper()
        current_temp = float(x.replace("K", ""))
        new_temp = current_temp - 273.15
        return new_temp

    elif num.endswith('F') or num.endswith('f'):
        x = num.upper()
        current_temp = float(x.replace("F", ""))
        new_temp = (current_temp - 32) * 5/9
        return new_temp
    
    return num


temp = temperature_converter(input("Enter a current temperature measurement in fahrenheit or kelvin:"))
print(f'the temperature entered is equivalent to {temp} Celsuis')