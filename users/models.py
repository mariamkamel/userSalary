from django.db import models

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class User(models.Model):
    name = models.CharField(
        max_length=200,
    )
    percentage = models.FloatField(blank=True, null=True)
    salary = models.FloatField()

    def __str__(self):
        return self.name

    def get_fields(self):
        return [
            (field.verbose_name, field.value_from_object(self))
            for field in self.__class__._meta.fields[1:]
        ]
