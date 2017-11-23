def Sugar(sentence):
    sentenceList = sentence.split(",")
    if len(sentenceList) == 1:
        SugarFinder(sentence)
    else:
        SugarCalculator(sentence)
    
def Calorie(sentence):
    sentenceList = sentence.split(",")
    if len(sentenceList) == 1:
        CalorieFinder(sentence)
    else:
        CalorieCalculator(sentence)

def Fat(sentence):
    sentenceList = sentence.split("")
    if len(sentenceList) == 1:
        FatFinder(sentence)
    else:
        FatCalculator(sentence)
            
def CalorieFinder(string):
    num = 1
####From https://github.com/leetrout/python-nutritionix###
    from nutritionix import Nutritionix
    api_key = "5fc43e41551148e7105f4c0b6e8cba31"
    app_id = "cd1f176e"
    nix = Nutritionix(app_id, api_key)
    stringsearch = nix.search(string, results=("0:"+str(num))).json()
### My Code ###
    item_id = stringsearch["hits"][0]["fields"]["item_id"]
    itemidsearch = nix.item(id=str(item_id)).json()
    itemcalorie = itemidsearch['nf_calories']
    if itemcalorie is None:
        raise TypeError("Please enter a food that contains Calories. ")
    else:
        return itemcalorie
    
def SugarFinder(string):
    num = 1
###From https://github.com/leetrout/python-nutritionix###    
    from nutritionix import Nutritionix
    api_key = "5fc43e41551148e7105f4c0b6e8cba31"
    app_id = "cd1f176e"
    nix = Nutritionix(app_id, api_key)   
    stringsearch = nix.search(string, results=("0:"+str(num))).json()
### My Code ###
    item_id = stringsearch["hits"][0]["fields"]["item_id"]
    itemidsearch = nix.item(id=str(item_id)).json()
    itemsugar = itemidsearch['nf_sugars']
    print("type is",type(itemsugar))
    if itemsugar is None:
        OUTPUT =  "Please enter a food that contains Sugar. "
        return OUTPUT
    else:
        return itemsugar

def FatFinder(string):
    num = 1
###From https://github.com/leetrout/python-nutritionix###       
    from nutritionix import Nutritionix
    api_key = "5fc43e41551148e7105f4c0b6e8cba31"
    app_id = "cd1f176e"
    nix = Nutritionix(app_id, api_key)   
    stringsearch = nix.search(string, results=("0:"+str(num))).json()
### My Code ###    
    item_id = stringsearch["hits"][0]["fields"]["item_id"]
    itemidsearch = nix.item(id=str(item_id)).json()
    itemfat = itemidsearch['nf_saturated_fat']
    if itemfat is None:
        OUTPUT = "Please enter a food that contains Fat. "
        return OUTPUT
    else:
        return itemfat

#### My Code ### 
def CalorieCalculator(string):
    num = 1
    sentenceList = string.split(",")
    totalCal = 0
    for i in sentenceList:
        totalCal = round((totalCal + CalorieFinder(i)),2)
    percentage = round(((totalCal/2200)*100),2)
    return totalCal, percentage

def SugarCalculator(string):
    num = 1
    sentenceList = string.split(",")
    totalSugar = 0
    for i in sentenceList:
        totalSugar = round((totalSugar + SugarFinder(i)),2)
    percentage = round(((totalSugar/32)*100),2)
    return totalSugar, percentage
    
def FatCalculator(string):
    num = 1
    sentenceList = string.split(",")
    totalFat = 0
    for i in sentenceList:
        totalFat = round((totalFat + FatFinder(i)),2)
    percentage = round(((totalFat/24)*100),2)
    return totalFat, percentage

print(Calorie("kit kat"))
