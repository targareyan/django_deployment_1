from django.shortcuts import render
from django.http import HttpResponse
from app_afresh.models import user

# Create your views here.

def index(request):
	return render(request, 'app_afresh/index.html')

def user1(request):
	user_list = user.objects.order_by('firstname')
	user_dict = {'input': user_list}
	return render(request, 'app_afresh/user.html', context=user_dict)

