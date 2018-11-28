from django import forms
from core.forms import AddressForm
from user.models import User
from core.models import Address

class UserForm(forms.ModelForm):
    addresses=AddressForm()
    class Meta:
        model=User
        fields=['firstName','lastName','birthDate']
      #  labels={
      #      'firstName': 'First Name',
       # }
        #help_texts={
         #   'firstName':'' 
       #}
    #adresses=forms.ModelMultipleChoiceField(queryset=Address.objects.all())

    #def __init__(self,*args, **kwargs):

     #   if kwargs.get('instance'):
     #       initial=kwargs.setdefault('initial',{})
     #       initial['addresses']=[t.pk for t in kwargs['instance'].address_set.all()]
     #   forms.ModelForm.__init__(self,*args,**kwargs)


      # def save(self,commit=True):
