#foodKeyword = open(/Keywords/foodkeywords.txt)
#if foodKeyword in sentence:
    #food(sentence)
#import urllib
#import json as m_json

def food(s):
    keyword  = ["food", "restaurant", "fastfood", "takeaway", "italian", "chinese", "indian", "pizza", "fish", "chips", "burger", "steak", "sandwich", "coffee", "mexican", "pub"]
    if ("restaurant" or "takeaway" or "food" or "fastfood") in s:
        foodType = input("What type of food? ")
        from google import *
        num_page = 1
        search_results = google.search(foodType, num_page)
        for result in search_results:
            print(result.description)
    else:
        print(" ")
food("i want a restaurant")
 
