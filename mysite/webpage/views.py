from django.shortcuts import render
from django.http import HttpResponse
from webpage.models import restaurant

# Create your views here.
def index(request):
    """ หน้าหลักแสดงร้านอาหารที่มีทั้งหมด """
    restaurantfo = restaurant.objects.all()
    context = {
        'resinfo': restaurantfo
    }
    return render(request, 'webpage/index.html', context=context)


def res_detail(request, restaurant_id):
    """ดูรายละเอียดข้องร้านอาหาร และ มีปุ่มจองร้านอาหาร """