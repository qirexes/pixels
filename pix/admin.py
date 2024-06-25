from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from .models import Balance, Category, Image, Notification, Profile, CollectionClickLog, Deposit, Withdrawal,ImageFile, Transaction
from django import forms



admin.site.unregister(User)
admin.site.register(ImageFile)

@admin.register(User)
class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

@admin.register(Balance)
class BalanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')

    def get_username(self, obj):
        return obj.user.username if obj.user else '-'
    get_username.short_description = 'Username'


class BalanceInline(admin.StackedInline):
    model = Balance
    can_delete = True


class CategoryAdminForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget = forms.Select(choices=[
            ('Art', 'Art'),
            ('Nature', 'Nature'),
            ('Pfp', 'Pfp'),
            ('Painting', 'Painting'),
            ('Digital Art', 'Digital Art'),
            ('Photography', 'Photography'),
            ('AI', 'AI'),
        ])

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('category', 'user', 'name', 'price')
    list_filter = ('category', 'user')
    search_fields = ('category__name', 'user__username')


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'timestamp', 'read')
    search_fields = ('user__username', 'title')
    list_filter = ('read', 'timestamp')

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('profile_picture', 'user')

@admin.register(CollectionClickLog)
class CollectionClickLogAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp')
    list_filter = ('user', 'timestamp')
    search_fields = ('user__username',)

# class DepositAdmin(admin.ModelAdmin):
#     list_display = ('user', 'amount', 'created_at')
#     search_fields = ('user__username', 'amount')
#     list_filter = ('created_at',)

# admin.site.register(Deposit, DepositAdmin)



@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'created_at')
    search_fields = ('user__username', 'amount')
    list_filter = ('user', 'amount', 'created_at',)


@admin.register(Withdrawal)
class WithdrawalAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'withdrawal_date')
    search_fields = ('user__username', 'amount')
    list_filter = ('user', 'withdrawal_date')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'timestamp', 'transaction_type', 'amount', 'description')
    list_filter = ('transaction_type', 'timestamp')
    search_fields = ('user__username', 'description')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set user during the first save.
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not request.user.is_superuser:
            form.base_fields['user'].queryset = User.objects.filter(id=request.user.id)
        return form

admin.site.register(Transaction, TransactionAdmin)