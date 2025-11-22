from django.shortcuts import render
# Create your views here.
from django.template import loader
from .models import QuestionPair

def index(request):
    return render(request,"cards/index.html")

def card_detail(request, id):
    card = QuestionPair.objects.get(id=id)
    return render(request, "cards/card_detail.html", {"card": card})
