# Generated by Django 4.2.6 on 2024-02-21 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fit', '0002_alter_note_set_and_reps_alter_note_weigth'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='weigth',
            new_name='weight',
        ),
    ]
