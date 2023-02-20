from django.shortcuts import render
from .models import Promocoes, Contato
from .contato_forms import FormContato

# Create your views here.
def home(request):
    promocao=Promocoes.objects.all()
    context = {
        'promocao':promocao,
        'form': FormContato()
    }
    return render(request, 'home/home.html', context)



