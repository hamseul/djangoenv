from django import forms
import datetime
from django.forms import SelectDateWidget

class SetCertificationDateForm(forms.ModelForm):
    certification_date=forms.DateField(
        widget=SelectDateWidget,
        initial=(datetime.date.today())
    )
