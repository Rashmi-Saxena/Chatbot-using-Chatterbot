from chatterbot.trainers import ListTrainer
from chatterbot.chatterbot import ChatBot
import os

#trains the AI

bot= ChatBot('support')
trainer= ListTrainer(bot)

for _file in os.listdir('txt'):
    chats=open('txt/'+_file,'r').readlines()

    trainer.train(chats) 

t= True

while t:
    request=input('You:')
    response=bot.get_response(request)

    print('bot:', response)

    
    
