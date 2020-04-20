from django.shortcuts import render
from django.http import HttpResponse
from webpage.models import restaurant

# Create your views here.
def index(request):
    restaurantfo = restaurant.objects.all()
    context = {
        'resinfo': restaurantfo
    }
    return render(request, 'webpage/index.html', context=context)


