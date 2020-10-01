from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot

english_bot = ChatBot("Ciara Bot", storage_adapter="chatterbot.storage.SQLStorageAdapter",
                      preprocessors=['chatterbot.preprocessors.clean_whitespace'],
                      logic_adapters=[{
                          'import_path': 'chatterbot.logic.BestMatch',
                          'default_response': 'i honestly have no idea how to respond to that',
                          'maximum_similarity_threshold': 0.8
                      },
                          "chatterbot.logic.MathematicalEvaluation"])
def trainbot():
    chatterbot.trainers.UbuntuCorpusTrainer(english_bot)
    trainer = ChatterBotCorpusTrainer(english_bot)
    trainer.train("chatterbot.corpus.english")
    print("training with intents.json\n")
    trainer.train("./intents.json")
    print('training with dataset1.json\n')
    trainer.show_training_progress


def get_bot_response(string):
    userText = string
    if(userText == "what is your name" or userText == "who are you" or userText == "what is your name?"):
        return str("My name is Ciara Bot")
    elif(userText == "i am antriksh"):
        return str("Hi! Antriksh")
    elif(userText == 'who made you' or userText == 'who made you?' or userText == 'who is your father'):
        return str('A guy named Antriksh made me')
    else:
        return str(english_bot.get_response(userText))

