from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
    """
        Index page - หน้าจอรายการวิชาที่มีการสอนทั้งหมด
    """
    # classes = models.classes
    # courses = models.courses
    # for cl in classes:
    #     cl['course'] = [co for co in courses if co['id'] == cl['course_id']][0]
    
    # context = {
    #     'new_classes': classes
    # }
    return render(request, 'webpage/index.html')