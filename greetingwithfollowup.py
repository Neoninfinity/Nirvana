def greetingwithfollowup(sentence):
    import urllib
    import json as m_json

    ### List of responses
    listgreeting = ["Hi ","Hello ","Hey ","Greetings "]
    listgreetques = ["\nhow are you?","\nhow are things?","\nhow’s it going?","\nhow do you do?"]
    listresponses = ["\nI am doing well","\nI feel nothing","\nmeh"]
    
    ########## Greeting ##########
    from random import randint
    greetrandom = listgreeting[randint(0, len(listgreeting)-1)]
    
    
    
    
    
    greetques = listgreetques[randint(0, len(listgreetques)-1)]
    OUTPUT = greetrandom + greetques
    ### OUTPUT THE FINAL RESPONSE
    return (OUTPUT)
