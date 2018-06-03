from django.contrib import admin

from schedule.forms import EventAdminForm
from schedule.models import Calendar, CalendarRelation, Event, Occurrence, Rule


@admin.register(Calendar)
class CalendarAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'desc')
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']
    fieldsets = (
        (None, {
            'fields': [
                ('name', 'slug', 'desc'),
            ]
        }),
    )


@admin.register(CalendarRelation)
class CalendarRelationAdmin(admin.ModelAdmin):
    list_display = ('calendar', 'content_object')
    list_filter = ('inheritable',)
    fieldsets = (
        (None, {
            'fields': [
                'calendar',
                ('content_type', 'object_id', 'distinction',),
                'inheritable',
            ]
        }),
    )


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'calendar', 'status', 'start', 'end')
    list_filter = ('calendar', 'status', 'start')
    ordering = ('-start',)
    date_hierarchy = 'start'
    search_fields = ('title', 'description')
    fieldsets = (
        (None, {
            'fields': [
                ('title', 'color_event', 'status'),
                ('description',),
                ('price', 'price_old'),
                ('start', 'end'),
                ('creator', 'calendar'),
                ('rule', 'end_recurring_period'),
            ]
        }),
    )
    form = EventAdminForm


admin.site.register(Occurrence, admin.ModelAdmin)


@admin.register(Rule)
class RuleAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('frequency',)
    search_fields = ('name', 'description')
