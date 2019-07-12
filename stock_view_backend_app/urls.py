from django.conf.urls import url
from stock_view_backend_app import views

# Template Tagging
app_name = 'stock_view_backend_app'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^help', views.help, name='help'),
	url(r'^access', views.access, name='access'),
	url(r'^users', views.users, name='users'),
	url(r'^formpage', views.form_name_view, name='form_name'),
	url(r'^other', views.other, name='other'),
	url(r'^relative', views.relative, name='relative'),
	url(r'^register', views.register, name='register'),
	url(r'^logout', views.user_logout, name='logout'),
	url(r'^user_login', views.user_login, name='user_login'),
	url(r'^CBView', views.CBView.as_view(), name='CBView'),
	url(r'^IndexView', views.IndexView.as_view(), name='IndexView'),
	url(r'^list', views.SchoolListView.as_view(), name='list'),
	url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail'),
]