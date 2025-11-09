from django import forms

class OrderForm(forms.Form):
    name = forms.CharField(max_length=150, required=True)
    phone = forms.CharField(max_length=50, required=True)


class ProfileForm(forms.Form):
    full_name = forms.CharField(label="Full name", max_length=150, required=False)
    email = forms.EmailField(label="Email", required=True)
    avatar = forms.ImageField(label="Avatar", required=False)


class PreferencesForm(forms.Form):
    TIMEZONES = [
        ("UTC", "+00:00 UTC"),
        ("Asia/Dubai", "Asia/Dubai"),
        ("Europe/Moscow", "Europe/Moscow"),
    ]
    LANGS = [
        ("en", "English"),
        ("ru", "Русский"),
    ]
    timezone = forms.ChoiceField(choices=TIMEZONES, required=True)
    language = forms.ChoiceField(choices=LANGS, required=True)
    newsletter = forms.BooleanField(label="Email me product updates", required=False)
