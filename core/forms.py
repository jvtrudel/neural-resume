from django import forms
from core.models import Person, Address



class PersonForm(forms.Form):
    firstName=forms.CharField(max_length=50)
    lastName=forms.CharField(max_length=50)
    birthDate=forms.DateField()

class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields='__all__'

