from django import forms
from django.core import validators
from stock_view_backend_app.models import UserModel, UserProfileInfo, Post, Comment
from django.contrib.auth.models import User

# def check_for_z(value):
# 	if value[0].lower() != 'z':
# 		raise forms.ValidationError("The value for the name field input needs to start with the character z!")

class FormName(forms.Form):
	# name = forms.CharField(validators=[check_for_z])
	name = forms.CharField()
	email = forms.EmailField()
	verify_email = forms.EmailField(label='Enter your email again:')
	text = forms.CharField(widget=forms.Textarea)

	def clean(self):
		all_clean_data = super().clean()
		email = all_clean_data['email']
		vmail = all_clean_data['verify_email']

		if email != vmail:
			raise forms.ValidationError("Make sure emails match!")

	# botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

	# def clean_botcatcher(self):
	# 	botcatcher = self.cleaned_data['botcatcher']
	# 	if len(botcatcher) > 0:
	# 		raise forms.ValidationError("GOTCHA BOT!")
	# 	return botcatcher

class NewUserForm(forms.ModelForm):
	class Meta():
		model = UserModel
		fields = '__all__'

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta(object):
		model = User
		fields = ('username', 'email', 'password')

class UserProfileInfoForm(forms.ModelForm):
	class Meta(object):
		model = UserProfileInfo
		fields = ('portfolio_site', 'profile_pic')

class PostForm(forms.ModelForm):
	class Meta():
		model = Post
		fields = ('author', 'title', 'text')

		widget = {
			'title': forms.TextInput(attrs={'class':'textinputclass'})
			'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
		}

class CommentForm(forms.ModelForm):
	class Meta():
		model = Comment
		fields = ('author', 'text')

		widget = {
			'author': forms.TextInput(attrs={'class':'textinputclass'})
			'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
		}