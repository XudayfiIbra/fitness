from django.db import models


class Note(models.Model):
    set_and_reps = models.IntegerField()
    weight = models.IntegerField()
    comment = models.TextField()

#exercises
class Abs(models.Model):
    exercise_name = models.CharField(max_length=250)
    exercise_thumnail = models.ImageField(upload_to='fit/files/thumnails/Abs')
    exercise_body_part = models.CharField(max_length=100)
    exercise_description = models.TextField()
    
class Shoulders(models.Model):
    exercise_name = models.CharField(max_length=250)
    exercise_thumnail = models.ImageField(upload_to='fit/files/thumnails/Shoulders')
    exercise_body_part = models.CharField(max_length=100)
    exercise_description = models.TextField()
    
    
class Biceps(models.Model):
    exercise_name = models.CharField(max_length=250)
    exercise_thumnail = models.ImageField(upload_to='fit/files/thumnails/Biceps')
    exercise_body_part = models.CharField(max_length=100)
    exercise_description = models.TextField()

class Chest(models.Model):
    exercise_name = models.CharField(max_length=250)
    exercise_thumnail = models.ImageField(upload_to='fit/files/thumnails/Chest')
    exercise_body_part = models.CharField(max_length=100)   
    exercise_description = models.TextField()

class Back(models.Model):
    exercise_name = models.CharField(max_length=250)
    exercise_thumnail = models.ImageField(upload_to='fit/files/thumnails/Back')
    exercise_body_part = models.CharField(max_length=100)   
    exercise_description = models.TextField()
        


