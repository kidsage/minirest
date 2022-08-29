from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from accountapp.models import User
from accountapp.forms import UserChangeForm, UserCreationForm


# Register your models here.
class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'is_admin', 'date_joined')
    list_filter = ('is_admin', 'is_superuser', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        # ('Personal info', {'fields': ('organization',)}),
        ('Permissions', {'fields': ('is_admin', 'is_superuser', 'is_active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)