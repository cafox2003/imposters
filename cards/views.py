from django.shortcuts import get_object_or_404, redirect, render
# Create your views here.
from django.template import loader
from .models import QuestionPair

def index(request):
    return render(request,"cards/index.html")

def card_detail(request, id):
    max_id = QuestionPair.objects.latest("id").id
    if id < 1:
        return redirect("card-detail", id=1)
    elif id > max_id:
        return redirect("card-detail", id=max_id)

    card = get_object_or_404(QuestionPair, id=id)
    return render(request, "cards/card_detail.html", {"card": card})
