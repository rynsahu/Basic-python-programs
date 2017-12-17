# Formula---->  F = C × 9/5 + 32
def converter(celsius):
        if celsius > -273.15:
            f = celsius * 9/5 + 32
            return f
        else:
            return("Temperature is not valid!")

print("**** Convert the temperature in to Fahrenheit ****")
temp = [10.0,-20.0,-289.0,100.0]

for celsius in temp:
         print(converter(celsius))
