from django import forms
from transport.models import TruckLists, NotificationInsurance, NotificationFitness, NotificationPollution


class AddTruck(forms.ModelForm):
    class Meta:
        model = TruckLists
        exclude = []


class ExpiryNotificationInsurance(forms.ModelForm):
    class Meta:
        model = NotificationInsurance
        exclude = []


class ExpiryNotificationFitness(forms.ModelForm):
    class Meta:
        model = NotificationFitness
        exclude = []


class ExpiryNotificationPollution(forms.ModelForm):
    class Meta:
        model = NotificationPollution
        exclude = []


class ImportTruck(forms.Form):
    excel = forms.FileField(required=True)