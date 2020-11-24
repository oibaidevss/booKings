from django import forms
from .models import JobBooking
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from bootstrap_datepicker_plus import DateTimePickerInput, DatePickerInput, TimePickerInput

class AddBookingForm(forms.ModelForm):
	class Meta:
		model = JobBooking
		fields = [
			"tech",
			"note_to_tech",
			"date",
			"time",
			"service",
			"contact",
		]
		widgets = {
			'date': DatePickerInput(),
			'time': TimePickerInput(),
		}
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post' # get or post
		self.helper.add_input(Submit('submit', 'Add Book')) 