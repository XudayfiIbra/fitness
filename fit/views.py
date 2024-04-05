from django.shortcuts import render
from . models import Biceps

def index(request):
    bicep = Biceps.objects.all()
    return render(request, 'index.html', {
        'bicep':bicep
    })
    
