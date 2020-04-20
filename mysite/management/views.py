from django.shortcuts import render
from webpage.models import restaurant
from django.conf import settings

# Create your views here.

def Management(request):
    msg = ''
    if request.method == 'POST':
        restaurantnew = restaurant.objects.create(
            restaurant_name=request.POST.get('restaurant_name'),
            seller_phone=request.POST.get('seller_phone'),
            desc=request.POST.get('desc'),
            picture=request.FILES.get('picture'),
            restaurant_status=request.POST.get('restaurant_status'),
        )
        msg = 'สร้างร้านค้าได้แล้ว: %s' % (restaurantnew.restaurant_name)

    else:
        restaurantnew = restaurant.objects.none()

    context = {
        'restaurantnew': restaurantnew,
        'msg': msg
    }
    return render(request, 'management/management.html', context=context)


