# Generated by Django 2.0.2 on 2018-03-29 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0013_auto_20180329_1704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subquestion',
            name='sub_choice',
        ),
        migrations.AddField(
            model_name='subquestion',
            name='sub_choice',
            field=models.ManyToManyField(blank=True, to='questions.Choice'),
        ),
    ]
