from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from . forms import CustomUserChangeForm, CustomUserCreationForm
from . models import User, Compras, Ventas

# Register your models here.
class CustomUserAdmin(UserAdmin):    
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ['email', 'last_login']


admin.site.register(User, CustomUserAdmin)
admin.site.register(Compras)
admin.site.register(Ventas)