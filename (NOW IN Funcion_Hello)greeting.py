def hello(sentence):
    #This function returns a greeting and a question,they are both randomly selected from the following lists.
    from random import randint
    listgreeting = ["Hi ","Hello ","Hey ","Greetings "]  
    listgreetques = ["how are you?","how are things?","how’s it going?","how do you do?"]
    greetrandom = listgreeting[randint(0, len(listgreeting)-1)]
    greetques = listgreetques[randint(0, len(listgreetques)-1)]
    OUTPUT = greetrandom + greetques  #Putting the two responses together
    return (OUTPUT) #returning the response to the main program
