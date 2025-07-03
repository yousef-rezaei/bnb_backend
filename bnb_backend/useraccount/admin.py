from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    model = User
    ordering = ('email',)
    list_display = ('email', 'is_staff', 'is_active','name')  # update based on your model
    search_fields = ('email',)
    readonly_fields = ('date_joined',)

    fieldsets = (
        (None, {'fields': ('email', 'password','name')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
