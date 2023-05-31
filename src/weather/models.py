from django.db import models


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.name} ({self.country})"

    class Meta:
        verbose_name_plural = "Cities"
