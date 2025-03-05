from portfolio_app.models import *
from django import forms

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"


