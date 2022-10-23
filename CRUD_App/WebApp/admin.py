from django.contrib import admin
from django.contrib.auth.models import User

# Register your models here.
admin.site.unregister(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=['id','username','email']