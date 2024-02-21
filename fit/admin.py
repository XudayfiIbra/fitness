from django.contrib import admin
from . models import Abs, Note, Chest, Biceps, Shoulders, Back


class AbsAdmin(admin.ModelAdmin):
    list_display = ('exercise_name', 'exercise_body_part',)
admin.site.register(Abs, AbsAdmin)


class NoteAdmin(admin.ModelAdmin):
    list_display = ('set_and_reps', 'weight', 'comment')
admin.site.register(Note, NoteAdmin)

class ChestAdmin(admin.ModelAdmin):
    list_display = ('exercise_name', 'exercise_body_part',)
admin.site.register(Chest, ChestAdmin)

class BicepsAdmin(admin.ModelAdmin):
    list_display = ('exercise_name', 'exercise_body_part',)    
admin.site.register(Biceps, BicepsAdmin)

class ShoulderAdmin(admin.ModelAdmin):
    list_display = ('exercise_name', 'exercise_body_part',)
admin.site.register(Shoulders, ShoulderAdmin)
    
class BackAdmin(admin.ModelAdmin):
    list_display = ('exercise_name', 'exercise_body_part',)
admin.site.register(Back, BackAdmin)    
