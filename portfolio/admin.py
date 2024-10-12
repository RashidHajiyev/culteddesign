from django.contrib import admin

# Register your models here.
from .models import UserDescription, Project, Portfolio, Contact


@admin.register(Contact)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')
    search_fields = ('name', 'email')

admin.site.register(UserDescription)
admin.site.register(Project)
admin.site.register(Portfolio)
#admin.site.register(Customer)
