def greetingwithfollowup(sentence):
    import urllib
    import json as m_json

    ### List of responses
    listgreeting = ["Hi ","Hello ","Hey ","Greetings "]
    listgreetques = ["\nHow are you?","\nHow are things?","\nHow’s it going?","\nHow do you do?"]
    listresponses = ["\nI am doing well","\nI feel nothing","\nmeh"]
    
    ########## Greeting ##########
    from random import randint
    greetrandom = listgreeting[randint(0, len(listgreeting)-1)]
    response = listresponses[randint(0, len(listresponses)-1)]    
    greetques = listgreetques[randint(0, len(listgreetques)-1)]
    OUTPUT = greetrandom + response + greetques
    ### OUTPUT THE FINAL RESPONSE
    return (OUTPUT)
