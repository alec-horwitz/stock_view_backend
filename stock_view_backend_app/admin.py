from django.contrib import admin
from stock_view_backend_app.models import AccessRecord,Topic,Webpage,UserModel,UserProfileInfo
# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(UserModel)
admin.site.register(UserProfileInfo)