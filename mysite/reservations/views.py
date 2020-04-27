from django.shortcuts import render
from webpage.models import restaurant
from django.contrib.auth.models import User
from reservations.models import myreservation
# Create your views here.

def start_reservation(request, restaurant_id):
    """ จองร้านอาหาร """
    restaurantrv = restaurant.objects.get(pk=restaurant_id)
    msg = ''
    if request.method == "POST":
        reservationcreat = myreservation.objects.create(
            person=request.POST.get("person"),
            reser_day=request.POST.get("reser_day"),
            reser_time=request.POST.get("reser_time"),
            reser_as=request.POST.get("reser_as"),
            contact=request.POST.get("contact"),
            user=request.user,
            restaurant_id=restaurant_id)
        msg = 'สร้างคำจองเสร็จแล้ว'

    context = {
        'restaurantrv': restaurantrv,
        'msg': msg,
        # 'reservationcreat': reservationcreat,
    }

    return render(request, 'reservations/reservation.html', context=context)


# def res_reservation_show(request)