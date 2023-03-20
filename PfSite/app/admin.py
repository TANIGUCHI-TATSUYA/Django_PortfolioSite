from django.contrib import admin
from .models import Profile,Work,Education,Experience
# Register your models here.
admin.site.register(Profile)
admin.site.register(Work)
admin.site.register(Experience)
admin.site.register(Education)
