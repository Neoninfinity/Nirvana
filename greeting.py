def main(sentence):
    import urllib
    import json as m_json

    ### List of responses
    listgreeting = ["Hi ","Hello ","Hey ","Ahoy there matey ","Greetings "]
    listgreetques = ["how are you?","how are things?","how’s it going?","how are ye feeling today?","how do you do?"]

    ### Lists for checking input
    listfood = ["food","eat","hungry","restaurant","pizza","burger","fastfood"]
    listgeneral = []

    ###
    ##sentence = input("Press enter when you are ready to begin: ")
    while sentence!="finish":  
      ########## Greeting ##########
      sentence = sentence.lower() ###Input
      from random import randint
      greetrandom = listgreeting[randint(0, len(listgreeting)-1)]
      greetques = listgreetques[randint(0, len(listgreetques)-1)]
      OUTPUT = greetrandom + greetques  
      if sentence == ("how are you?"):
            OUTPUT = "I'm good thanks!"
      ### OUTPUT THE FINAL RESPONSE
      return (OUTPUT)
      sentence = input("Press enter when you are ready to begin: ")
