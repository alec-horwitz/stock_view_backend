from django.conf.urls import url
from stock_view_backend_app import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^help', views.help, name='help'),
	url(r'^users', views.users, name='users'),
]