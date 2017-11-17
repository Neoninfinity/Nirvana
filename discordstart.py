import discord
import asyncio
import sys
from main import hello
from keywords import key
from GoogleSearcg import gsearch
from twittersearch import TwitSearch
#from discord_functions import *
keywords = key
client = discord.Client()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    #####################################
    #
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating messages...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
        return 0
    elif message.content.startswith('!gsearch'):
        #phrase = (message.content).replace('!gsearch', '')
        wordlist = message.content.split()
        wordlist.remove("!gsearch")
        phrase = ""
        intv = 1
        if not wordlist:
            tmp = await client.send_message(message.channel, "To google search format like this: '!gsearch [term] [value]'")
            return 0
        for x in wordlist:
            if is_number(x) == False:
                phrase = str(phrase) +str(x)+(" ")
                continue
            else:
                intv = int(x)
                break
        
        listneeded = gsearch(phrase,intv)
        OUTPUT = ""
        for x in listneeded:
            OUTPUT = OUTPUT + x +"\n"
        tmp = await client.send_message(message.channel, OUTPUT)
        return 0
        
    elif message.content.startswith('!adminshutdown'):
        tmp = await client.send_message(message.channel, "Shutting down, Goodbye!")
        sys.exit()
        
    elif message.content.startswith('!stweet'):
        OUTPUT = TwitSearch()
        tmp = await client.send_message(message.channel, OUTPUT)
        return 0
        
    elif message.content.startswith('!introduce'):
        await client.send_message(message.channel, "Hi I'm Nirvana a handy assistant\nI'm going to be the best bot around!!")
        return 0
    else:
        print("No response for select input")
    
    #########################################MAIN NIRVANA CODE
    sentence = message.content
    sentence = sentence.lower()
    brokenString = sentence.split()
    #print(("author is",type(message.author.id),message.content))
    if (len(set(brokenString).intersection(keywords))) > 0 or sentence in keywords.keys():
        ## Keyword checking goes here (if statements)
        for x in brokenString or sentence in keywords.keys():
            if x in keywords.keys():
                funcLoad = keywords[x]
            elif sentence in keywords.keys():
                funcLoad = keywords[sentence]
            else:
                funcLoad = 0

        if funcLoad == 1:
            OUTPUT = hello(sentence)
            tmp = await client.send_message(message.channel, OUTPUT)
        elif funcLoad == 2:
            print("placeholder")
        elif funcLoad == 3:
            print("") ## google function goes here
        else:
            print("Function not found")
    elif message.author.id == ("375255240326250496"):
        print(message.author)
    else:  
        tmp = await client.send_message(message.channel, "Sorry, I couldn't understand you")

client.run('Mzc1MjU1MjQwMzI2MjUwNDk2.DO23Qg.TAlBUyCq5MyE7UMH4hSLZz1WP-E')
