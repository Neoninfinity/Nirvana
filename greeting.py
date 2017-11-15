import urllib
import json as m_json
##########################################################################################
### List of responses
listgreeting = ["Hi ","Hello ","Hey ","Ahoy there matey ","Greetings "]
listgreetques = ["how are you?","how are things?","how’s it going?","how are ye feeling today?","how do you do?"]

### Lists for checking input
listfood = ["food","eat","hungry","restaurant","pizza","burger","fastfood"]
listgeneral = []

################################################################################################################
sentence = input("Press enter when you are ready to begin: ")
while sentence!="finish":

  ########## Greeting ##########
  sentence = sentence.lower() ###Input
  from random import randint
  random = randint(0, 4) ###choose random response 
  greetrandom = listgreeting[random]
  greetques = listgreetques[random]
  OUTPUT = greetrandom + greetques
  print (OUTPUT) ###just for testing
  ################################# return output to screen

  ##################################################################################################Check if they are talking about food
  for i in listfood:
    if i in sentence:
        OUTPUT =  def food(sentence)
        print("Suprise")
  sentence = input("Press enter when you are ready to begin: ")
################################################################################################################

##########


