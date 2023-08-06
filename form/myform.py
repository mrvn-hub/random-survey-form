from django import forms
from django.forms import ModelForm
from .models import Form


# class MyForm(forms.Form):
# 	name = forms.CharField(label="Name and Surname", max_length=25)
# 	agreement = forms.BooleanField(label="Do you agree with our privacy policy and terms and conditions?")
	
class MyForm(ModelForm):
	name = forms.CharField(label="Name and Surname", max_length=25, required=True)
	agreement = forms.BooleanField(label="Do you agree with our privacy policy and terms and conditions?", required=True)
	class Meta:
		model = Form
		fields = ["name", "agreement"]