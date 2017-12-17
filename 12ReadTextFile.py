file = open("fruits.txt", "r")    #Use to open the file it may be a .txt or .bll(binary file).
content = file.read()             #Storing the file in to content variable.
file.close()                      #closing the opend file.
print(content)
