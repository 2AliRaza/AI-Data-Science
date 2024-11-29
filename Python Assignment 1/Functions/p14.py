def convert_temperature(value, scale):
 if scale == 'C':
    return (value * 9/5) + 32  
 elif scale == 'F':
    return (value - 32) * 5/9   
 else:
    return "Invalid scale. Use 'C' for Celsius or 'F' for Fahrenheit."

print(convert_temperature(25, 'C'))  
print(convert_temperature(77, 'F'))  