
# from django.db import models

from django.contrib.auth.models import User
from .models import Question

users = User.objects.all()


class Audit(models.Model):
    audit_name = models.CharField('Audit', max_length=200)
    owner = models.ManyToManyField(User)
    start_date = models.DateTimeField()
    question = models.ManyToManyField(Question, blank=True, null=True)

    def __str__(self):
        return self.audit_name



