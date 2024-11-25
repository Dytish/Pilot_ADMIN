from django.db import models

class District(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "Область"
        verbose_name_plural = "Области"

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Регион"
        verbose_name_plural = "Регионы"
        constraints = [
            models.UniqueConstraint(fields=['name', 'district'], name='unique_region_in_district')
        ]
    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Город"
        verbose_name_plural = "Города"
        constraints = [
            models.UniqueConstraint(fields=['name', 'region'], name='unique_city_in_region')
        ] 

    def __str__(self):
        return self.name
