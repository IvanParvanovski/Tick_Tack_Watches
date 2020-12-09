from django.db import models


class Watch(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('teenagers', 'Teenagers'),
        ('children', 'Children'),
        ('unisex', 'Unisex'),
    )

    brand = models.CharField(max_length=20, blank=False, null=False)
    model = models.CharField(max_length=20, blank=False, null=False)
    price = models.PositiveIntegerField(default=0, blank=False, null=False)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default=GENDER_CHOICES[0])

    def __str__(self):
        return f'{self.brand} Model: {self.model}'
