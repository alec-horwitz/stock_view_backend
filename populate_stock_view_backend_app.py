import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','stock_view_backend.settings')

import django
django.setup()

## FAKE POP SCRIPT

import random
from stock_view_backend_app.models import AccessRecord,Webpage,Topic,User
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
	t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
	t.save
	return t

def populate(N=5):

	for entry in range(N):

		# get topic for the entry
		top = add_topic()

		# create the fake data for that entry
		fake_url = fakegen.url()
		fake_date = fakegen.date()
		fake_name = fakegen.company()

		fake_first_name = fakegen.first_name()
		fake_last_name = fakegen.last_name()
		fake_email = fakegen.email()

		# create the new webpage entry
		webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

		# create a fake access record for that webpage
		acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

		usr = User.objects.get_or_create(first_name=fake_first_name,last_name=fake_last_name,email=fake_email)[0]

if __name__ == '__main__':
	print("populating script!")
	populate(20)
	print("populating complete!")