from django import forms


class ConcertFilterForm(forms.Form):
    county = forms.CharField(label='Country', max_length=50, required=False,
                             widget=forms.TextInput(attrs={'placeholder': 'Enter Country'}))
    city = forms.CharField(label='City', max_length=50, required=False,
                           widget=forms.TextInput(attrs={'placeholder': 'Enter City'}))
    month = forms.CharField(label='Month', max_length=10, required=False,
                            widget=forms.TextInput(attrs={'placeholder': 'Enter Month'}))
    week_day = forms.CharField(label='Day of week', max_length=10, required=False,
                               widget=forms.TextInput(attrs={'placeholder': 'Enter Day: Monday etc'}))
    day_number = forms.IntegerField(label='Number of the day', required=False, min_value=1, max_value=31,
                                    widget=forms.NumberInput(attrs={'placeholder': 'Enter positive nuber'}))
    year = forms.IntegerField(label='Year', required=False,
                              widget=forms.NumberInput(attrs={'placeholder': 'Enter year'}))
    address = forms.CharField(label='Address of the Concert', max_length=50, required=False,
                              widget=forms.TextInput(attrs={'placeholder': 'Enter Address'}))
    exact_time = forms.TimeField(label='Time', required=False,
                                 help_text='Enter time as HH:MM:SS', widget=forms.TimeInput(attrs={'placeholder': '19:00:00 etc'}))
