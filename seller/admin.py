from django.contrib import admin
from seller.models import Handler

@admin.register(Handler)
class HandlerAdmin(admin.ModelAdmin):
    pass