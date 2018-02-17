from django.db import models


class TruckLists(models.Model):
    truck_number = models.CharField(max_length=10, null=False, blank=False, help_text="MH02VG1111")
    insurance = models.DateField(blank=False, null=False, help_text="insurance expiry date(YYYY-MM-DD)")
    fitness = models.DateField(blank=False, null=False, help_text="Fitness expiry date(YYYY-MM-DD)")
    pollution = models.DateField(blank=False, null=False, help_text="pollution expiry date(YYYY-MM-DD)")


class NotificationInsurance(models.Model):
    truck_number = models.CharField(max_length=10, null=False, blank=False)
    insurance = models.DateField(blank=False, null=False)
    read = models.BooleanField(default=False)
    remainder = models.BooleanField(default=False)
    remaining_insurance = models.IntegerField(blank=False, null=False)
    remainded_for_remaining_day = models.IntegerField(blank=True, null=True)


class NotificationFitness(models.Model):
    truck_number = models.CharField(max_length=10, null=False, blank=False)
    fitness = models.DateField(blank=False, null=False)
    read = models.BooleanField(default=False)
    remainder = models.BooleanField(default=False)
    remaining_fitness = models.IntegerField(blank=False, null=False)
    remainded_for_remaining_day = models.IntegerField(blank=True, null=True)


class NotificationPollution(models.Model):
    truck_number = models.CharField(max_length=10, null=False, blank=False)
    pollution = models.DateField(blank=False, null=False)
    read = models.BooleanField(default=False)
    remainder = models.BooleanField(default=False)
    remaining_pollution = models.IntegerField(blank=False, null=False)
    remainded_for_remaining_day = models.IntegerField(blank=True, null=True)


