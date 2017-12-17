#Write a program which can compute the factorial of a given numbers.
#The results should be printed in a comma-separated sequence on a single line.

list = []
isOption = "y"

while isOption == "y":
    f_num = int(input("Enter the number for calculating factorial: "))

    def calculat(f_num):
        for num in range(1, f_num): f_num = f_num * num
        return(f_num)

    factorial = calculat(f_num)
    print(factorial)
    list.append(str(factorial))
    isOption = input("Do you want to calculate more[y/n]: ")
    print("\n------------------------------------------------------------------\n")
else:
    print(",".join(list))
