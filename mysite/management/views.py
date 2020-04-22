from django.shortcuts import render
from webpage.models import restaurant, restaurant_type
from django.conf import settings

# Create your views here.


def Add_Restaurant(request):
    msg = ''
    res_type = restaurant_type.objects.all().order_by('id')
    if request.method == 'POST':
        restaurantnew = restaurant.objects.create(
            restaurant_name=request.POST.get('restaurant_name'),
            seller_phone=request.POST.get('seller_phone'),
            desc=request.POST.get('desc'),
            restaurant_type_id_id=request.POST.get('restaurant_type_id'),
            location_address=request.POST.get('location_address'),
            picture=request.FILES.get('picture'),
            restaurant_status=request.POST.get('restaurant_status'),
        )
        msg = 'สร้างร้านค้าได้แล้ว: %s' % (restaurantnew.restaurant_name)

    else:
        restaurantnew = restaurant.objects.none()

    context = {
        'restaurantnew': restaurantnew,
        'res_type': res_type,
        'msg': msg
    }
    return render(request, 'management/add_restaurant.html', context=context)

def Management(request):
    # msg = ''
    # if request.method == 'POST':
    #     restaurantnew = restaurant.objects.create(
    #         restaurant_name=request.POST.get('restaurant_name'),
    #         seller_phone=request.POST.get('seller_phone'),
    #         desc=request.POST.get('desc'),
    #         picture=request.FILES.get('picture'),
    #         restaurant_status=request.POST.get('restaurant_status'),
    #     )
    #     msg = 'สร้างร้านค้าได้แล้ว: %s' % (restaurantnew.restaurant_name)

    # else:
    #     restaurantnew = restaurant.objects.none()

    # context = {
    #     'restaurantnew': restaurantnew,
    #     'msg': msg
    # }
    # return render(request, 'management/add_restaurant.html', context=context)
    """ หน้าจัดการร้านอาหาร ที่สามารถเพิ่ม ลบ แก้ ร้านอาหารหรือประเภทได้ """
    restaurantfo = restaurant.objects.all()
    context = {
        'resinfo': restaurantfo
    }

    return render(request, 'management/management.html', context=context)


