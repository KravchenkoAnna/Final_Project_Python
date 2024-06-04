from django.db import models


class Concerts(models.Model):
    county = models.CharField("County", max_length=50)
    city = models.CharField("City", max_length=50)
    month = models.CharField("Month", max_length=10)
    week_day = models.CharField("Week Day", max_length=9)
    day_number = models.IntegerField("Day Number")
    year = models.IntegerField("Year", default=1900)
    address = models.TextField("Address")
    exact_time = models.TimeField("Time")

    def __str__(self):
        return self.county

    class Meta:
        verbose_name = "Concert"
        verbose_name_plural = "Concerts"
