from django.contrib import admin

from .models import User,Store,Review

# Register your models here.

admin.site.register(User)
admin.site.register(Store)
admin.site.register(Review)