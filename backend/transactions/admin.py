from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Transaction

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('username', 'email', 'first_name', 'last_name')

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'type', 'category', 'date')
    list_filter = ('type', 'category', 'date')
    search_fields = ('user__username', 'description')
    date_hierarchy = 'date'

    fields = ('user', 'amount', 'type', 'category', 'date', 'description')  # 👈 обязательно!
