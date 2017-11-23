def reponseToHowAreYou(sentence):
    #This function
    from random import randint
    listresponses = ["I am doing well","Good","Fine","Pretty good"]
    listresponsesadd = ["\nHow can i help you?","\nHow may i be of assistance","\nWhat can i help you with?"]
    response = listresponses[randint(0, len(listresponses)-1)]   
    responseadd = listresponsesadd[randint(0, len(listresponsesadd)-1)] 
    OUTPUT = response + responseadd
    return (OUTPUT)
