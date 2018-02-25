# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
import Client_Form.forms as cffm


def inputdata(request):
	#if form is submitted
	if request.method == 'POST':
		form = cffm.InputData(request.POST)
	
		#checking the form is valid or not 	
		if form.is_valid():
			#if valid rendering new view with values
			#the form values contains in cleaned_data dictionary
			return render(request, 'result.html', {
				'clientid': form.cleaned_data['clientid'],
				'fname': form.cleaned_data['fname'],
				'lname': form.cleaned_data['lname'],
				'email': form.cleaned_data['email'],
				'phonenum': form.cleaned_data['phonenum'],
				'bussname': form.cleaned_data['bussname'],
				'bankacc': form.cleaned_data['bankacc'],
				'addstreet1': form.cleaned_data['addstreet1'],
				'addstreet2': form.cleaned_data['addstreet2'],
				'addcity': form.cleaned_data['addcity'],
				'addstate': form.cleaned_data['addstate'],
				'addcountry': form.cleaned_data['addcountry'],
				'addpincode': form.cleaned_data['addpincode'],
				'stat': form.cleaned_data['stat'],
				})
	else:
		#creating a new form
		form = cffm.InputData()
	
	#returning form 
	return render(request, 'form.html', {'form':form});
