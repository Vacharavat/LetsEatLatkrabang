from django.shortcuts import render, redirect
from webpage.models import restaurant, restaurant_type
from django.conf import settings

# Create your views here.


def Add_Restaurant(request):
    """ หน้าเพิ่มร้านอาหารใหม่ """
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
        print(restaurantnew.picture)
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
    """ หน้าจัดการร้านอาหาร ที่สามารถเพิ่ม ลบ แก้ ร้านอาหารหรือประเภทได้ """
    restaurantfo = restaurant.objects.all()
    context = {
        'resinfo': restaurantfo
    }

    return render(request, 'management/management.html', context=context)


def restaurant_edit(request, restaurant_id):
    
    """ แก้ไขร้านอาหาร"""

    try:
        restauranted = restaurant.objects.get(pk=restaurant_id)
        res_type = restaurant_type.objects.all()
        msg = ''
    except restaurant.DoesNotExist:
        return redirect(to='Management')
    
    if request.method == 'POST':
        restauranted.restaurant_name = request.POST.get('restaurant_name')
        restauranted.desc = request.POST.get('desc')
        restauranted.location_address = request.POST.get('location_address'),
        restauranted.restaurant_type_id_id = request.POST.get('restaurant_type_id')
        restauranted.seller_phone = request.POST.get('seller_phone')
        restauranted.picture = request.FILES.get('picture')
        restauranted.restaurant_status = request.POST.get('restaurant_status')
        restauranted.save()
        msg = 'แก้ไขร้านอาหารสำเร็จแล้ว: %s' %(restauranted.restaurant_name)
    
    context = {
        'restauranted': restauranted,
        'res_type': res_type,
        'msg': msg
    }


    return render(request, 'management/edit_restaurant.html', context=context)



def Type_add(request):
    
    """ เพิ่มประเภทใหม่เข้าไปในดาต้าเบส """

    msg = ''

    if request.method == 'POST':
        Type = restaurant_type.objects.create(
            type_name=request.POST.get('type_name'),
        )
        msg = 'สร้างประเภทใหม่ได้แล้ว: %s' % (Type.type_name)
    else:
        Type = restaurant_type.objects.none()

    context = {
        'restaurant_type': Type,
        'msg': msg
    }

    return render(request, 'management/add_type.html', context=context)

def restaurant_delete(request, restaurant_id):

    """ ลบร้านอาหาร """
    restaurantdl = restaurant.objects.get(pk=restaurant_id)
    restaurantdl.delete()

    return redirect(to='Management')