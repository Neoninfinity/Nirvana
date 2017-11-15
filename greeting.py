def mainpersonality(sentence):
    import urllib
    import json as m_json

    ### List of responses
    listgreeting = ["Hi ","Hello ","Hey ","Greetings "]
    listgreetques = ["how are you?","how are things?","how’s it going?","how do you do?"
    
    
    
    ##sentence = input("Press enter when you are ready to begin: ")
    while sentence!="finish":  
      ########## Greeting ##########
      from random import randint
      greetrandom = listgreeting[randint(0, len(listgreeting)-1)]
      greetques = listgreetques[randint(0, len(listgreetques)-1)]
      OUTPUT = greetrandom + greetques  
      if sentence == ("how are you?"):
            OUTPUT = "I've been better...\n Cuphead is a hard game"
      ### OUTPUT THE FINAL RESPONSE
      return (OUTPUT)
      sentence = input("Press enter when you are ready to begin: ")
