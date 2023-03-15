from django.shortcuts import render
from django.views.generic import View
from .models import Profile
# Create your views here.
class IndeXView(View):
    def get(self,request,*args,**kwargs):
        profile_data=Profile.objects.all()
        if profile_data.exists():
            profile_data = profile_data.order_by('-id')[0]
        return render(request,'templates/index.html',{'prfile_data':profile_data})