from django.shortcuts import render
from django.http import HttpResponse
from stock_view_backend_app.models import AccessRecord,Webpage,Topic,User
# Create your views here.

def index(request):
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records': webpages_list}
	return render(request, 'stock_view_backend_app/index.html', context=date_dict)

def help(request):
	my_dict = {'insert_me': "Hello I am from stock_view_backend_app/views.py !"}
	return render(request, 'stock_view_backend_app/help.html', context=my_dict)

def users(request):
	user_list = User.objects.order_by('first_name')
	user_dict = {'users': user_list}
	return render(request, 'stock_view_backend_app/users.html', context=user_dict)