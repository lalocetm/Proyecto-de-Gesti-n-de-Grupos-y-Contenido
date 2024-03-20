from django.contrib import admin

from groups.models import Group, UserGroup

# Register your models here.

admin.site.register(Group)
admin.site.register(UserGroup)
