from django.shortcuts import render
from webpage.models import restaurant
# Create your views here.

def Management(request):
    # msg = ''


    # if request.method == 'POST':
    #     restaurant = restaurant.objects.create(
    #         name=request.POST.get('restaurant_name'),
    #         desc=request.POST.get('desc'),
    #         picture=request.POST.get('picture'),
    #         status=request.POST.get('restaurant_status'),
    #     )
    #     msg = 'สร้างร้านค้าได้แล้ว: %s' % (restaurant.name)
    # else:
    #     restaurant = restaurant.objects.none()

    # context = {
    #     'restaurant': restaurant,
    #     'msg': msg
    # }

    return render(request, 'management/management.html')
