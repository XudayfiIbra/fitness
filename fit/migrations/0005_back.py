# Generated by Django 4.2.6 on 2024-02-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0004_biceps_chest_shoulders_alter_abs_exercise_thumnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Back',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise_name', models.CharField(max_length=250)),
                ('exercise_thumnail', models.ImageField(upload_to='fit/files/thumnails/Back')),
                ('exercise_body_part', models.CharField(max_length=100)),
                ('exercise_description', models.TextField()),
            ],
        ),
    ]
