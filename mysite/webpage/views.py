from django.shortcuts import render
from django.http import HttpResponse
from webpage.models import restaurant
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    """ หน้าหลักแสดงร้านอาหารที่มีทั้งหมด """
    restaurantfo = restaurant.objects.all()
    context = {
        'resinfo': restaurantfo
    }
    return render(request, 'webpage/index.html', context=context)


def res_detail(request, restaurant_id):
    """ดูรายละเอียดข้องร้านอาหาร และ มีปุ่มจองร้านอาหาร """