from django.urls import path

from . import views
from .models import QuestionPair
from django.shortcuts import redirect

def redirect_to_first(request):
    first =  QuestionPair.objects.first()
    return redirect('card-detail',id=first.id)

urlpatterns = [
    # path("", views.index, name="index"),
    path("", redirect_to_first),
    path("<int:id>", views.card_detail, name="card-detail")
]
