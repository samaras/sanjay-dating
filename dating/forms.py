from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from fields import CreditCardField, ExpiryDateField, VerificationValueField

from dating.models import *

class AddressMixin(forms.ModelForm):
	class Meta:
		model = CreditCardCharges
		fields = (address_line1, address_line2,	city, address_zip, address_state)
		widgets = {
			'address_line1': forms.TextInput(attrs={'class':'form-control'}), 
			'address_line2': forms.TextInput(attrs={'class':'form-control'}),	
			'city': forms.TextInput(attrs={'class':'form-control'}), 
			'address_zip': forms.TextInput(attrs={'class':'form-control'}), 
			'address_state': forms.TextInput(attrs={'class':'form-control'}),
		}

class PaymentForm(AddressMixin, forms.Form):
	name_on_card = forms.CharField(max_length=50, required=True)
	card_number = CreditCardField(required=True)
	expiry_date = ExpiryDateField(required=True)
	card_code = VerificationValueField(required=True)
