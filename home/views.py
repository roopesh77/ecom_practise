from django.shortcuts import render
from .models import *
from django.views.generic import View
# Create your views here.
class BaseView(View):
     pass


class HomeView(BaseView):
    def get(self,request):

        return render(request,'index.html', self.views)