from django.shortcuts import render
from django.http import HttpResponse
from webpage.models import restaurant
from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required(login_url='login')
def index(request):
    """ หน้าหลักแสดงร้านอาหารที่มีทั้งหมด """

    # เป็นตัวแปรเพื่อรับค่าค้นหานั้นมา (Frame)
    search_restaurant = request.GET.get('search_restaurant', '')
    # เป็นตัวแปรที่ดึงข้อมูลจาก models restaurant (Frame)
    restaurantfo = restaurant.objects.all()

    # ถ้ามีการค้นหาจะเรียกเงื่อนไขนี้มาทำแล้วแสดงข้อมูลตาม keyword ที่หาไป (Frame)
    if request.method == 'GET':
        if search_restaurant != '':
            restaurantfo = restaurant.objects.filter(restaurant_name__icontains=search_restaurant)
    
    # แปลงเพื่อไปใช้บนหน้า html (Frame)
    context = {
        'search_restaurant': search_restaurant,
        'resinfo': restaurantfo
    }
    return render(request, 'webpage/index.html', context=context)

def index_type(request, type_id):
    """ แสดงตามประเภท """
    # เป็นตัวแปรเพื่อรับค่าค้นหานั้นมา (Frame)
    search_restaurant = request.GET.get('search_restaurant', '')
    # เป็นตัวแปรที่ดึงข้อมูล models restaurant ที่เอาข้อมูลแค่ประเภทของร้านอาหารนั้นๆ (Frame)
    restaurantfo = restaurant.objects.filter(restaurant_type_id_id=type_id)

    if request.method == 'GET':
        if search_restaurant != '':
            restaurantfo = restaurant.objects.filter(restaurant_name__icontains=search_restaurant)
    # แปลงเพื่อไปใช้บนหน้า html (Frame)
    context = {
        'search_restaurant': search_restaurant,
        'resinfo': restaurantfo
    }
    return render(request, 'webpage/index.html', context=context)


# หน้ารายละเอียดนี่ยังไม่ได้ทำนะครับ (Frame)
def res_detail(request, restaurant_id):
    """ดูรายละเอียดข้องร้านอาหาร และ มีปุ่มจองร้านอาหาร """