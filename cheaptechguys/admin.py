from django.contrib import admin
from .models import Product, contact_us, Account, Comment
from django.contrib.auth.admin import UserAdmin
# Register your models here.


admin.site.register(contact_us)
admin.site.register(Comment)


class AccountAdmin(UserAdmin):
    list_display = ('email', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email', 'username')
    readonly_fields = ('id', 'date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
class ProductAdmin(admin.ModelAdmin):
    search_fields = ('Title',)
    readonly_fields = ()

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
admin.site.register(Product, ProductAdmin)
admin.site.register(Account, AccountAdmin)
