from django.contrib import admin
from receipts.models import Receipt, Account, ExpenseCategory

# Register your models here.


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    list_display = (
        "vendor",
        "total",
        "id",
	)

@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "id",
    )
