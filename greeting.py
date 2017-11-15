def greeting(sentence):
    import urllib
    import json as m_json

    ### List of responses
    listgreeting = ["Hi ","Hello ","Hey ","Greetings "]
    listgreetques = ["how are you?","how are things?","how’s it going?","how do you do?"]

    ########## Greeting ##########
    from random import randint
    greetrandom = listgreeting[randint(0, len(listgreeting)-1)]
    greetques = listgreetques[randint(0, len(listgreetques)-1)]
    OUTPUT = greetrandom + greetques  
    ### OUTPUT THE FINAL RESPONSE
    return (OUTPUT)

