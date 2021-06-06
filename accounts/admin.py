from django.contrib import admin
from .models import User,Employee,Owner
# Register your models here.

admin.site.register(User)
admin.site.register(Owner)
admin.site.register(Employee)
