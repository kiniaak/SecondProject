from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

bot= ChatBot('chatbot',read_only=False,
              logic_adapters=[
                {
                    'import_path':'chatterbot.logic.BestMatch',
                    #'default_response':'Sorry,I dont know what that means',
                    #'maximun_similarity_threshold':0.90
                }
                ])

list_to_train=[

    "hi",
    "hi,there",
    "What's your name?",
    "I'm just a chatbot",
    "What is your fav food?",
    "I like cheese",
    "what's your fav sport?",
    "swimming",
    "do you have children?",
    "no"
]

chatterbotCorpusTrainer=ChatterBotCorpusTrainer(bot)

#list_trainer=ListTrainer(bot)
#list_trainer.train(list_to_train)
chatterbotCorpusTrainer.train('chatterbot.corpus.english')

def index(request):
    return render(request,'blog/index.html')

def specific(request):
    return HttpResponse("This is the specific url")   

def getResponse(request):
    userMessage= request.GET.get('userMessage')
    chatResponse= str(bot.get_response(userMessage))
    return HttpResponse(chatResponse)

