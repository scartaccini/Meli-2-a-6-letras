from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator

class Palabra(models.Model):
    palabra=models.CharField(blank=False, null=False, max_length=6,validators=[MinLengthValidator(2)])
    dificultad=models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)], blank=True, null=True,)

    def __str__(self):
        return "{}".format(self.palabra)