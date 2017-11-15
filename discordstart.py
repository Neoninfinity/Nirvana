import discord
import asyncio
from main import hello
from keywords import key
keywords = key
client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    ###################################
    sentence = message.content
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
        else:
            print("Function not found")
    elif message.author.id == ("375255240326250496"):
       #print(message.author)
    else:  
        tmp = await client.send_message(message.channel, "Sorry, I couldn't understand you") 
        

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
    else:
        print("No response for select input")

client.run('Mzc1MjU1MjQwMzI2MjUwNDk2.DO23Qg.TAlBUyCq5MyE7UMH4hSLZz1WP-E')
