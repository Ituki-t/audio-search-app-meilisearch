from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Voice


# Create your views here.

def index(request):
    voice = Voice.objects.all()
    return render(request, 'voices/index.html', {'voice': voice})