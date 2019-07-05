from django.shortcuts import render
from . import forms
from stock_view_backend_app.models import AccessRecord,Webpage,Topic
from stock_view_backend_app.forms import NewUserForm, UserForm, UserProfileInfoForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
	context_dict = {'text':'Hello world!', 'number':100}
	return render(request, 'stock_view_backend_app/index.html',context_dict)

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

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

def register(request):

    registered = False

    if request.method == 'POST':

        # Get info from "both" forms
        # It appears as one form to the user on the .html page
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        # Check to see both forms are valid
        if user_form.is_valid() and profile_form.is_valid():

            # Save User Form to Database
            user = user_form.save()

            # Hash the password
            user.set_password(user.password)

            # Update with Hashed password
            user.save()

            # Now we deal with the extra info!

            # Can't commit yet because we still need to manipulate
            profile = profile_form.save(commit=False)

            # Set One to One relationship between
            # UserForm and UserProfileInfoForm
            profile.user = user

            # Check if they provided a profile picture
            if 'profile_pic' in request.FILES:
                print('found it')
                # If yes, then grab it from the POST form reply
                profile.profile_pic = request.FILES['profile_pic']

            # Now save model
            profile.save()

            # Registration Successful!
            registered = True

        else:
            # One of the forms was invalid if this else gets called.
            print(user_form.errors,profile_form.errors)

    else:
        # Was not an HTTP post so we just render the forms as blank.
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    # This is the render and context dictionary to feed
    # back to the registration.html file page.
    return render(request,'stock_view_backend_app/registration.html', {'user_form':user_form,'profile_form':profile_form,'registered':registered})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("LOGIN FAILED")
            print("Username: {} and password: {}".format(username,password))
            return HttpResponse("invalidlogin details supplied!")

    else:
        return render(request, 'stock_view_backend_app/login.html', {})
