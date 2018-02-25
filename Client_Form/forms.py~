from django import forms  

STAT_CHOICES= [
    ('active', 'Active'),
    ('passive', 'Passive'),
    ('pipeline', 'Pipeline'),
    ('prospect', 'Prospect'),
    ]

#creating our forms
class InputData(forms.Form):
	clientid = forms.CharField(label='ClientID', max_length=100)
	fname = forms.CharField(label='First Name', max_length=100)
	lname = forms.CharField(label='Last Name', max_length=100)
	email = forms.EmailField(label='Email', max_length=100)
	phonenum = forms.CharField(label='Phone Number', max_length=11)
	bussname = forms.CharField(label='Business Name', max_length=100)
	bankacc = forms.CharField(label='Bank Account Number', max_length=100)
	addstreet1 = forms.CharField(label='Address Street1', max_length=100)
	addstreet2 = forms.CharField(label='Address Street2', max_length=100)
	addcity = forms.CharField(label='City', max_length=100)
	addstate = forms.CharField(label='State', max_length=100)
	addcountry = forms.CharField(label='Country', max_length=100)
	addpincode = forms.CharField(label='PinCode', max_length=100)
	stat = forms.CharField(label='Status', widget=forms.Select(choices=STAT_CHOICES))



