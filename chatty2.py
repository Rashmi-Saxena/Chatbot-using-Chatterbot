# Importing chatterbot
from chatterbot.chatterbot import ChatBot

# Create object of ChatBot class
bot = ChatBot('SupportBot')

# Create object of ChatBot class with Storage Adapter
bot = ChatBot(
    'SupportBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

# Create object of ChatBot class with Logic Adapter
bot = ChatBot(
    'SupportBot',  
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)

# Inport ListTrainer
from chatterbot.trainers import ListTrainer

trainer = ListTrainer(bot)

trainer.train([
'(hi|hello|hey|holla|hola)',
'Hello',
'I need help| assistance',
'yes, how may i help?',
'have a question|another question',
'Yes, go ahead',
'what does profcess do ?',
'We help people ditch the script on the old ways of thinking and make the people-work connections that enable the growth which job seekers and employers are striving for. We are all about placing the right people in the right positions, not just filling a quota. We listen to both the client and candidates needs and ensure the entire process is a conversation, not just a transaction. We establish an ease in alliance between the company demand and skilled workforce through our well-defined research and tech based platform which mainly monitors the real time market trend and various diversified needs. The alliance is established by assisting the company with a skilled workforce and providing the opportunity to the talented candidates to update their employment status. It is not a success until both our client and candidate are happy. Let us help you find success, no matter which side of the process you are on.',
'What all services does prof-cess have?',
'to view the services that we provide, you can visit this link https://profcess.com/services',
'(who are prof-cess?| what makes profcess special?| why profcess?)',
'We at Prof-cess are the story of work with a team of supercharged, talented, and experienced people along with fresher who are highly ardent and can go to any extent to achieve the customary goal',
'Okay Thanks',
'No Problem!'
])

name=input("Enter Your Name: ")
print("Welcome to Prof-cess! I am a support bot, let me know how can I help you?")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye' or request =='be back later' or request == 'see you soon':
        print('Bot: Bye! Have a nice day.')
        break
    else:
        response=bot.get_response(request)
        print('Bot:',response)