# Work with Python 3.6
import discord
import os
client = discord.Client()

#import values
gm_dict={}
with open("valuesGMAX.txt", 'r') as f:
      for line in f:
        items = line.split('/')
        key, values = items[0], items[1:]
        gm_dict[key] = values
norm_dict={}
with open("values.txt", 'r') as f:
      for line in f:
        items = line.split('/')
        key, values = items[0], items[1:]
        norm_dict[key] = values
types_dict={}
with open("types.txt", 'r') as f:
      for line in f:
        items = line.split('/')
        key, values = items[0], items[1:]
        types_dict[key] = values
        
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    #Help  
    if message.content.startswith('%help') or message.content.startswith('$help'):
      msg="Enter query as '%ball (or $ball) [PokemonNameHere]' to get pokemon catch rates! \n"
      msg+="Enter query as '%ball (or $ball) G [PokemonNameHere]' to get catch rates for gigantamaxes!"
      await client.send_message(message.channel, msg)

    #Wiggly
    elif message.content.startswith('%wiggly') or message.content.startswith('$wiggly'):
      await client.send_file(message.channel, "wiggly.png")

    #type matchup
    elif message.content.startswith('%matchup') or message.content.startswith('$matchup'):
      words=message.content.split()
      search=words[1].capitalize()
      if(len(words)!=2):
        msg="Please enter one type at a time!"
      elif search not in types_dict:
        msg="Invalid input!"
      else:
        msg='For '+search
        msg+=' types, use '+types_dict.get(search)
        msg+=' type moves!'
      await client.send_message(message.channel, msg)

    #Ballbot
    elif message.content.startswith('%ball') or message.content.startswith('$ball'):
        words = message.content.split()
        if (len(words)<2) or (len(words)>3):
            msg="Invalid input!"
        else:
            #it's not gmax
            if(len(words)==2):
                pk = words[1].capitalize()
                if pk not in norm_dict:
                  msg="Invalid input!"
                else:
                  msga = 'Here are the ball catch rates for '+pk
                  msgb = '\n'.join(map(str,norm_dict.get(pk)))
                  msg=msga+':\n'+msgb
                  msg+="Please note that these values may not be completely correct!"
            else:
                if(words[1]!='G' and words[1]!='g'):
                    msg="Invalid input!"
                else:
                    #it's GMax
                    pk = words[2].capitalize()
                    if pk not in gm_dict:
                      msg="Invalid input!"
                    else:
                      msga = 'Here are the ball catch rates for Gigantamax '+pk
                      msgb = '\n'.join(map(str,gm_dict.get(pk)))
                      msg=msga+':\n'+msgb
                      msg+="Please note that these values may not be completely correct!"
        #output message
        await client.send_message(message.channel, msg)

#tells me the bot is open
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(str(os.environ.get('TOKEN')))
