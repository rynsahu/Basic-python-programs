print("Enter the number for solving power of: ")
base = input("Base: ")
exponent = input("Exponent: ")

def solve_power_of(base, exponent):                       #Function Definitio..
    return base ** exponent

ans = solve_power_of(int(base), int(exponent)) #Function call..
print("Answer: " + str(ans))
