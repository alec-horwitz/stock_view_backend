from django.db import models
from django.contrib.auth.models import User

class School(models.Model):
	name = models.CharField(max_length=264)
	principal = models.CharField(max_length=264)
	location = models.CharField(max_length=264)

	def __str__(self):
		return self.name

class Student(models.Model):
	name = models.CharField(max_length=264)
	age = models.PositiveIntegerField()
	school = models.ForeignKey(School, related_name='students')
	
	def __str__(self):
		return self.name
		


class Topic(models.Model):
	top_name = models.CharField(max_length=264, unique=True)

	def __str__(self):
		return self.top_name

class Webpage(models.Model):
	topic = models.ForeignKey(Topic)
	name = models.CharField(max_length=264, unique=True)
	url = models.URLField(unique=True)

	def __str__(self):
		return self.name

class AccessRecord(models.Model):
	name = models.ForeignKey(Webpage)
	date = models.DateField()

	def __str__(self):
		return str(self.date)

class UserModel(models.Model):
	first_name = models.CharField(max_length=264)
	last_name = models.CharField(max_length=264)
	email = models.EmailField(max_length=264, unique=True)

	def __str__(self):
		return self.first_name+" "+self.last_name

class UserProfileInfo(models.Model):

	# Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
    profile_pic = models.ImageField(upload_to='basic_app/profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username