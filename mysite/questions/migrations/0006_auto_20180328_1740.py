# Generated by Django 2.0.2 on 2018-03-28 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_question_question_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='question_type',
        ),
        migrations.AddField(
            model_name='choice',
            name='choice_type',
            field=models.CharField(choices=[('1', 'Single Choice'), ('2', 'Multiple Choice'), ('3', 'Free-Text'), ('4', 'Enter Date'), ('5', 'File Upload'), ('6', 'Image-Upload'), ('7', 'Video-Upload')], default='Multiple Choice', max_length=200, verbose_name='Choice Type'),
            preserve_default=False,
        ),
    ]
