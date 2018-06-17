import datetime

from django.db import models
from django.utils import timezone
from django import forms

from django.contrib.auth.models import User

users = User.objects.all()


Choice_Type = (
    ('1', 'Single Choice'),
    ('2', 'Multiple Choice'),
    ('3', 'Free-Text'),
    ('4', 'Enter Date'),
    ('5', 'File Upload'),
    ('6', 'Image-Upload')
)

Compliance_Status = (
    ('1', 'Compliant'),
    ('2', 'Partially Compliant 75%'),
    ('3', 'Partially Compliant 50%'),
    ('4', 'Partially Compliant 25%'),
    ('5', 'Non-Compliant')
)

Frequency = (
    ('1', 'Once'),
    ('2', 'Hourly'),
    ('3', 'Daily'),
    ('4', 'Weekly'),
    ('5', 'Monthly'),
    ('6', 'Yearly')
)


# Create your models here.
class Question(models.Model):
    question_text = models.CharField('Question', max_length=200)
    choice_type = models.CharField('Choice Type', max_length=200, choices=Choice_Type)
    information = models.TextField('Information', max_length=500, blank=True)
    file_upload = models.FileField(blank=True, null=True, upload_to="compliance/%Y/%m/%D/")
    image_upload = models.ImageField(blank=True, null=True, upload_to="compliance_image/%Y/%m/%D/")
    footnote = models.TextField('Footnote', max_length=500, blank=True)

    pub_date = models.DateTimeField('Publish Date')
    frequency = models.CharField(max_length=200, choices=Frequency, default='Once')
    owner_email = models.EmailField('Owner Email')

    user = models.ManyToManyField(User, 'Assign_To')
    weight = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Audit(models.Model):
    audit_name = models.CharField('Audit', max_length=200)
    owner = models.ManyToManyField(User)
    start_date = models.DateTimeField()
    question = models.ManyToManyField(Question, blank=True, null=True)

    def __str__(self):
        return self.audit_name


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    compliance_status = models.CharField(max_length=200, choices=Compliance_Status)
    comment = models.BooleanField(default=False)
    action = models.BooleanField(default=False)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


# Create your models here.
class SubQuestion(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    outcome = models.CharField(max_length=200, choices=Compliance_Status)
    question_text = models.CharField(max_length=200)
    weight = models.IntegerField(default=0)
    pub_date = models.DateTimeField('Publish Date')
    owner_email = models.EmailField('Owner Email')

    choice_type = models.CharField('Choice Type', max_length=200, choices=Choice_Type)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class SubChoice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    sub_question = models.ForeignKey(SubQuestion, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    compliance_status = models.CharField(max_length=200, choices=Compliance_Status)
    comment = models.BooleanField(default=False)
    action = models.BooleanField(default=False)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
