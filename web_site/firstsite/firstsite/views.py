from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    text = request.GET['usertext']
    amount = len(text.split())

    return render(request, 'reverse.html', {'green': text[::-1], 'amount': amount, 'text': text})

