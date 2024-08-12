from django.contrib import admin

# Register your models here.
from .models import UserDescription, Project, Portfolio, Customer


admin.site.register(UserDescription)
admin.site.register(Project)
admin.site.register(Portfolio)
admin.site.register(Customer)
