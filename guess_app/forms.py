from django import forms


class GuessForm(forms.Form):
    body = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Your guess", "width": '20%'}
        ),
    )