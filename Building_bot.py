#Guide article for chatterbot https://online.datasciencedojo.com/blogs/building-an-ai-based-chatbot-in-python
#

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#Initializing bot
GoTBot = ChatBot(name = 'BankBot',
                  read_only = False,                  
                  logic_adapters = ["chatterbot.logic.BestMatch"],                 
                  storage_adapter = "chatterbot.storage.SQLStorageAdapter")

#Training on standard corpus data
corpus_trainer = ChatterBotCorpusTrainer(GoTBot)

corpus_trainer.train("chatterbot.corpus.english")


#Training on custom corpus
'''greet_conversation = [

    "Hello",

    "Hi there!",

    "How are you doing?",

    "I'm doing great.",

    "That is good to hear",

    "Thank you.",

    "You're welcome."

]


open_timings_conversation = [

    "What time does the Bank open?",

    "The Bank opens at 9AM",

]


close_timings_conversation = [

    "What time does the Bank close?",

    "The Bank closes at 5PM",

]'''


#Initializing Trainer Object

trainer = ListTrainer(GoTBot)


#Training BankBot

trainer.train(greet_conversation)

trainer.train(open_timings_conversation)

trainer.train(close_timings_conversation)