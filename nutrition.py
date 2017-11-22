def CalorieFinder(string, num):

    from nutritionix import Nutritionix

    api_key = "5fc43e41551148e7105f4c0b6e8cba31"
    app_id = "cd1f176e"

    nix = Nutritionix(app_id, api_key)
    
    stringsearch = nix.search(string, results=("0:"+str(num))).json()
    item_id = stringsearch["hits"][0]["fields"]["item_id"]
    itemidsearch = nix.item(id=str(item_id)).json()
    itemcalorie = itemidsearch['nf_calories']
    return itemcalorie

def SugarFinder(string, num):
    
    from nutritionix import Nutritionix

    api_key = "5fc43e41551148e7105f4c0b6e8cba31"
    app_id = "cd1f176e"

    nix = Nutritionix(app_id, api_key)
    
    stringsearch = nix.search(string, results=("0:"+str(num))).json()
    item_id = stringsearch["hits"][0]["fields"]["item_id"]
    itemidsearch = nix.item(id=str(item_id)).json()
    itemsugar = itemidsearch[nf_sugars]
    return itemsugar

def FatFinder(string, num):
    
    from nutritionix import Nutritionix

    api_key = "5fc43e41551148e7105f4c0b6e8cba31"
    app_id = "cd1f176e"

    nix = Nutritionix(app_id, api_key)
    
    stringsearch = nix.search(string, results=("0:"+str(num))).json()
    item_id = stringsearch["hits"][0]["fields"]["item_id"]
    itemidsearch = nix.item(id=str(item_id)).json()
    itemsfat = itemidsearch[nf_saturated_fat]
    return itemsfat

def CalorieCalculator(string):
    num = 1
    sentenceList = string.split(",")
    totalCal = 0
    for i in sentenceList:
        totalCal = totalCal + CalorieFinder(i, num)
    return totalCal

print(CalorieCalculator("Slice of Cheese,1 Egg,Beef Patty,Burger Bun"))
