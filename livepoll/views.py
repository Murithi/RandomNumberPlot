
from random import *
import threading
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from rest_framework import status
from django.shortcuts import render

from django.http import JsonResponse
from django.views.generic import TemplateView

from channels import Channel

# Create your views here.


def periodic():
    global t
    n = random.randint(10, 200)
    sendmsg(str(n))
    t = threading.Timer(5, periodic)
    t.start()


def send_rand_num(num):
    Channel('random-num').send({
        'randNum': randNum
    })


def random_num(request):
    return JsonResponse(randint(1, 10), safe=False)


class HomePageView(TemplateView):
    template_name = 'index.html'

    # def get(self, request, **kwargs):
    #     return render(request, 'index.html', context=None)
