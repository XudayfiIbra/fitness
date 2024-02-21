from django.contrib import admin
from . models import Abs, Note


class AbsAdmin(admin.ModelAdmin):
    list_display = ('exercise_name', 'exercise_body_part',)
admin.site.register(Abs, AbsAdmin)


class NoteAdmin(admin.ModelAdmin):
    list_display = ('set_and_reps', 'weight', 'comment')
admin.site.register(Note, NoteAdmin)
