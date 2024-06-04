from django import forms


class ConcertFilterForm(forms.Form):
    county = forms.CharField(label='Country', max_length=50, required=False)
    city = forms.CharField(label='City', max_length=50, required=False)
    month = forms.CharField(label='Month', max_length=10, required=False)
    week_day = forms.CharField(label='Day of week', max_length=10, required=False)
    day_number = forms.IntegerField(label='Number of the day', required=False, min_value=1, max_value=31)
    year = forms.IntegerField(label='Year', required=False)
    address = forms.CharField(label='Address of the Concert', max_length=50, required=False)
    exact_time = forms.TimeField(label='Time', required=False,
                                 help_text='Enter time as HH:MM:SS')
