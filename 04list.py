myList = ["hi", 2, "hello"]
print (myList)
print (myList[2])
print (myList[2])
print (myList[:2])
print (myList[-1])
print (myList[-3:])
print ("add the item in the list")
get = input("Enter the item: ")
myList.append(get)                            # Adding the items in a myList using get variable.
print (myList)
print ("remove the added item in the list")
myList.remove(get)                            #Removing the item which added in list from get variable.
print (myList)
