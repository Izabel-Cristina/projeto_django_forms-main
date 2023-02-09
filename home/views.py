from django.shortcuts import render
from .models import Promocoes

# Create your views here.
def home(request):
    promocao=Promocoes.objects.all()
    context = {
        'promocao':promocao
    }
    return render(request, 'home/home.html', context)

