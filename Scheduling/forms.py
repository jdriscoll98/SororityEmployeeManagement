from django import forms
from Scheduling.models import ShiftType, Shift, Availability, SchedulePeriod
from django.forms import CheckboxSelectMultiple
from django.forms import ModelForm
from Employment.models import Employee

class ShiftTypeForm(ModelForm):
    class Meta:
        model = ShiftType
        fields = '__all__'

class ShiftForm(ModelForm):
    class Meta:
        model = Shift
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ShiftForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['Type'].disabled = True
            self.fields['Employee'].required = False
            self.fields['Employee'].widget.attrs['disabled'] = 'disabled'
            self.fields['up_for_trade'].disabled = True
            self.fields['date'].disabled = True

class AvailabilityForm(ModelForm):
    class Meta:
        model = Availability
        fields = '__all__'
        widgets = {
            'days' : CheckboxSelectMultiple
        }

class SchedulePeriodForm(ModelForm):
    class Meta:
        model = SchedulePeriod
        fields = '__all__'
        widgets = {
            'start_date': forms.DateInput(attrs={'class':'datepicker'}),
            'end_date': forms.DateInput(attrs={'class':'datepicker'})
        }

    def clean(self):
        cleaned_data = super(SchedulePeriodForm, self).clean()
        start_date, end_date= cleaned_data['start_date'], cleaned_data['end_date']
        if end_date > start_date:
            pass
        else:
            raise forms.ValidationError('The end date must be after the start date')
        return cleaned_data
