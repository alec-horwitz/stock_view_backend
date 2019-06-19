from django.contrib import admin
from stock_view_backend_app.models import AccessRecord,Topic,Webpage
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)