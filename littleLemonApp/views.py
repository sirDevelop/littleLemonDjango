from django.shortcuts import render
from littleLemonApp import models
from django.http import HttpResponse
from django.views import View

# Create your views here.
# User1 = models.User.objects.create_user(username='admin', password='admin')

# User2 = models.User.objects.create_user(username='admin2', password='admin2')

class UserView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello world!")