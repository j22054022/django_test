from django.contrib import admin
from first_app.models import *
# Register your models here.

admin.site.register(AccessRecorder)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(User)
admin.site.register(UserProfileInfo)