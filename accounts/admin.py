from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import CustomUser
# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model=CustomUser
    list_display = ['email','username','first_name','last_name','age','birth_date','is_staff']

    # fieldsets = UserAdmin.fieldsets+(
    #     (None, {'fields':('age','birth_date')})
    # )
    # add_fieldsets = UserAdmin.add_fieldsets+(
    #     (None, {'fields':('age', 'birth_date')})
    # )
    # def birth_date(self):
    #      return self.birth_date
admin.site.register(CustomUser,CustomUserAdmin)
