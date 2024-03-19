from django.shortcuts import render
from django.http import JsonResponse
import asyncio
from chatterbot import ChatBot
chatbot = ChatBot("Chatpot")

async def chatresponse(query):
    return chatbot.get_response(query)

def index(request):
    return render(request, 'index.html', {"title": "FriendAI"})

def bot_response(request):
    if request.method == 'POST':
        message = request.POST.get('message', '')
        print(message)
        response = str(asyncio.run(chatresponse(message)))
        print(response)
        return JsonResponse({'response': response})
    return JsonResponse({'response': 'Method not allowed'}, status=405)


