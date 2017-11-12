def main(sentence):
    import urllib
    import json as m_json
    sentence=0

    ### List of responses
    listgreeting = ["Hi ","Hello ","Hey ","Ahoy there matey ","Greetings "]
    listgreetques = ["how are you?","how are things?","how’s it going?","how are ye feeling today?","how do you do?"]

    ### Lists for checking input
    listfood = ["food","eat","hungry","restaurant","pizza","burger","fastfood"]
    listgeneral = []

    ###
    ##sentence = input("Press enter when you are ready to begin: ")
    while sentence!="finish":
      sentence = str(sentence)  
      ########## Greeting ##########
      print(sentence)
      sentence = sentence.lower() ###Input
      from random import randint
      random = randint(0, 4) ###choose random response 
      greetrandom = listgreeting[randint(0, len(listgreeting)-1)]
      greetques = listgreetques[randint(0, len(listgreetques)-1)]
      OUTPUT = greetrandom + greetques

      ### OUTPUT THE FINAL RESPONSE
      return (OUTPUT)
      sentence = input("Press enter when you are ready to begin: ")
  
  
  
  
  
  
  
