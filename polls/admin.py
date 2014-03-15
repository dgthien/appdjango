from django.contrib import admin

from polls.models import Poll
from polls.models import Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    search_fields = ['question']

    list_display = ('question', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)