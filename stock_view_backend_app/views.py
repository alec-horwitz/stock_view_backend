from django.shortcuts import render
from . import forms
from stock_view_backend_app.models import AccessRecord,Webpage,Topic
from stock_view_backend_app.forms import NewUserForm
# Create your views here.

def index(request):
	context_dict = {'text':'Hello world!', 'number':100}
	return render(request, 'stock_view_backend_app/index.html',context_dict)

def help(request):
	my_dict = {'insert_me': "Hello I am from stock_view_backend_app/views.py !"}
	return render(request, 'stock_view_backend_app/help.html', context=my_dict)

def access(request):
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records': webpages_list}
	return render(request, 'stock_view_backend_app/access.html', context=date_dict)

def users(request):
	form = NewUserForm()
	if request.method == "POST":
		form = NewUserForm(request.POST)

		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print("ERROR: Form Invalid!")

	return render(request, 'stock_view_backend_app/users.html', {'form': form})

def form_name_view(request):
	form = forms.FormName()

	if request.method == 'POST':
		form = forms.FormName(request.POST)

		if form.is_valid():
			print("VALIDATION SUCCESS!")
			print("NAME: "+form.cleaned_data['name'])
			print("EMAIL: "+form.cleaned_data['email'])
			print("TEXT: "+form.cleaned_data['text'])

	return render(request, 'stock_view_backend_app/form_page.html', {'form':form})

def other(request):
	return render(request, 'stock_view_backend_app/other.html')

def relative(request):
	return render(request, 'stock_view_backend_app/relative_url_templates.html')