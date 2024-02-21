from django.db import models


class Note(models.Model):
    set_and_reps = models.IntegerField()
    weight = models.IntegerField()
    comment = models.TextField()

#exercises
class Abs(models.Model):
    exercise_name = models.CharField(max_length=250)
    exercise_thumnail = models.ImageField(upload_to='fit/files/thumnails')
    exercise_body_part = models.CharField(max_length=100)
    exercise_description = models.TextField()



