#foodKeyword = open(/Keywords/foodkeywords.txt)
#if foodKeyword in sentence:
    #food(sentence)
#import urllib
#import json as m_json

def food(s):
    keyword  = ["food", "restaurant", "fastfood", "takeaway", "italian", "chinese", "indian", "pizza", "fish", "chips", "burger", "steak", "sandwich", "coffee", "mexican", "pub"]
    if ("restaurant" or "takeaway" or "food" or "fastfood") in s:
        foodType = input("What type of food? ")
        foodType = urllib.urlencode ( { 'q' : foodType } )
        response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + foodType + " food" ).read()
        json = m_json.loads ( response )
        results = json [ 'responseData' ] [ 'results' ]
        for result in results:
            title = result['title']
            url = result['url']   # was URL in the original and that threw a name error exception
            print ( title + '; ' + url )
    else:
        print(" ")
food("i want a restaurant")
 
