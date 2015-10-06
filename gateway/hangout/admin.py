from django.contrib import admin

# Register your models here.
from .models import Hangout

class HangoutAdmin(admin.ModelAdmin):
    date_hierarchy = 'timestamp'
    search_fields = ['title', 'requested_hangout']
    list_display = ['__unicode__','title', 'price', 'timestamp', 'requested_hangout', 'active']
    list_editable = ['title', 'active']
    list_filter = ['title', 'price', 'timestamp', 'active']
    readonly_fields = ['timestamp','requested_hangout']
    prepopulated_fields = {'slug': ('title',)}
    class Meta:
        model = Hangout

admin.site.register(Hangout, HangoutAdmin)