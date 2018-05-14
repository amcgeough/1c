# Generated by Django 2.0.2 on 2018-05-07 11:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0028_auto_20180425_1846'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audit_name', models.CharField(max_length=200, verbose_name='Audit')),
                ('start_date', models.DateTimeField()),
                ('owner', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questions.Question')),
            ],
        ),
        migrations.AlterField(
            model_name='choice',
            name='compliance_status',
            field=models.CharField(choices=[('1', 'Compliant'), ('2', 'Partially Compliant 75%'), ('3', 'Partially Compliant 50%'), ('4', 'Partially Compliant 25%'), ('5', 'Non-Compliant')], max_length=200),
        ),
        migrations.AlterField(
            model_name='subchoice',
            name='compliance_status',
            field=models.CharField(choices=[('1', 'Compliant'), ('2', 'Partially Compliant 75%'), ('3', 'Partially Compliant 50%'), ('4', 'Partially Compliant 25%'), ('5', 'Non-Compliant')], max_length=200),
        ),
        migrations.AlterField(
            model_name='subquestion',
            name='outcome',
            field=models.CharField(choices=[('1', 'Compliant'), ('2', 'Partially Compliant 75%'), ('3', 'Partially Compliant 50%'), ('4', 'Partially Compliant 25%'), ('5', 'Non-Compliant')], max_length=200),
        ),
    ]
