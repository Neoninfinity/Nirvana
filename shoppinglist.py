###If shopping list is said runs the shoppingList function###
if "shopping list" in sentence:
  
###Asks user for str input for the list and adds it to the shopping list###
def shopping(word):
    shoppingList = []
    while word!="stop":
        word = input("What do you want adding to the shopping list? ")        
        if word in shoppingList:
            continue
        shoppingList.append(word)
        if word == "stop":
            shoppingList.remove("stop")
    return shoppingList
