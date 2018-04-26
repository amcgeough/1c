# Generated by Django 2.0.2 on 2018-03-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20180328_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_type',
            field=models.CharField(choices=[('1', 'Single Choice'), ('2', 'Multiple Choice'), ('3', 'Free-Text'), ('4', 'Enter Date'), ('5', 'File Upload'), ('6', 'Image-Upload'), ('7', 'Video-Upload')], default='Multiple Choice', max_length=200, verbose_name='Question Type'),
            preserve_default=False,
        ),
    ]
