from django.db import models
from django import forms
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User

class Analysis(models.Model):
    user = models.ForeignKey(User, related_name="analysis", related_query_name="analysis", blank=False, on_delete=models.CASCADE)
    type = models.CharField(max_length=20)
    positive = models.DecimalField(max_digits=4, decimal_places=2)
    negative = models.DecimalField(max_digits=4, decimal_places=2)
    neutral = models.DecimalField(max_digits=4, decimal_places=2)

