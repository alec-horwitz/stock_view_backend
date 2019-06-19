from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	my_dict = {'insert_me': "Hello I am from stock_view_backend_app/views.py !"}
	return render(request, 'stock_view_backend_app/index.html', context=my_dict)

def help(request):
	my_dict = {'insert_me': "Hello I am from stock_view_backend_app/views.py !"}
	return render(request, 'stock_view_backend_app/help.html', context=my_dict)