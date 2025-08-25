from django import forms

from balloon.models import Balloon, Client


class BalloonForm(forms.ModelForm):
    class Meta:
        model = Balloon
        fields = '__all__'

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'