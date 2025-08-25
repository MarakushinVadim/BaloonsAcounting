from django.contrib import admin

from balloon.models import Balloon, Client, BalloonType


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone')
    search_fields = ('name', 'phone')

@admin.register(BalloonType)
class BalloonTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Balloon)
class BalloonAdmin(admin.ModelAdmin):
    list_display = ('number', 'type', 'produced_at')
    list_filter = ('status',)
    search_fields = ('number',)