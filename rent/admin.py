from django.contrib import admin

from rent.models import Rent


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'type', 'volume', 'count', 'start_date', 'end_date')
    list_filter = ('owner', 'type', 'volume')
