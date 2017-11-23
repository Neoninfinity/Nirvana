#I had the majority of these functions directly on the server.

def hello(sentence):
    #This function returns a greeting and a question, they are both randomly selected from the following lists.
    from random import randint
    listgreeting = ["Hi ","Hello ","Hey ","Greetings "]  
    listgreetques = ["how are you?","how are things?","how’s it going?","how do you do?"]
    greetrandom = listgreeting[randint(0, len(listgreeting)-1)]
    greetques = listgreetques[randint(0, len(listgreetques)-1)]
    OUTPUT = greetrandom + greetques  #Putting the two responses together
    return (OUTPUT) #returning the response to the main program

def goodbye(sentence):
    #This function returns a goodbye, that is randomly selected from the following list.
    from random import randint
    listgoodbye = ["Goodbye","Toodle-oo","Cheerio","Adios","Bye-bye"]  
    response = listgoodbye[randint(0, len(listgoodbye)-1)]
    OUTPUT = response    
    return OUTPUT

def reponseToHowAreYou(sentence):
    #This function
    from random import randint
    listresponses = ["I am doing well","Good","Fine","Pretty good"]
    listresponsesadd = ["\nHow can i help you?","\nHow may i be of assistance","\nWhat can i help you with?"]
    response = listresponses[randint(0, len(listresponses)-1)]   
    responseadd = listresponsesadd[randint(0, len(listresponsesadd)-1)] 
    OUTPUT = response + responseadd
    return (OUTPUT)

def random(sentence):   
    listRandomQuestions = ["what is your name?","what is your favourite colour?","how old are you?","what can you do?","how can you help me?"]
    listRandomResponses = ["My name is Nirvana","My favourite colour is blue","I am 1 week old","I can count calories of foods you have eaten.\n I can google stuff for you.","I can count calories of foods you have eaten.\n I can google stuff for you."]
    for i in listRandomQuestions:
        if i in sentence:
            num = listRandomQuestions.index(i)
            OUTPUT = listRandomResponses[num]
            return OUTPUT

def responses(sentence):
    #This function returns a response
    
    ###Not my code###
    from string import punctuation
    sentence = ''.join(c for c in sentence if c not in punctuation)
    ###-----------###   
    
    listofAnswers = ["its going well","good","doing well","fine","im good","i am good","very well","not bad","going well","hanging in there","and you"]
    listofResponses = ["Good to hear \nHow can i help you?","I'm doing well \nHow can i help you?"]
    for i in listofAnswers:
        if i in sentence:
            if (listofAnswers.index(i)<=9):
                OUTPUT = listofResponses[0]
            elif (listofAnswers.index(i)==10):
                OUTPUT = listofResponses[1]
            return OUTPUT
    
