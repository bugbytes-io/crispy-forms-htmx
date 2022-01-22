from django import forms
from datetime import datetime
from django.urls import reverse_lazy
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from .models import User 


class UniversityForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        # self.helper.form_action = reverse_lazy('index')
        # self.helper.form_method = 'POST'
        self.helper.form_id = 'university-form'
        self.helper.attrs = {
            'hx-post': reverse_lazy('index'),
            'hx-target': '#university-form',
            'hx-swap': 'outerHTML'
        }
        self.helper.add_input(Submit('submit', 'Submit'))
    
    subject = forms.ChoiceField(
        choices=User.Subjects.choices,
        widget=forms.Select(attrs={
            'hx-get': reverse_lazy('check-subject'),
            'hx-target': '#div_id_subject',
            'hx-trigger': 'change'
        })
    )
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date()}))

    class Meta:
        model = User
        fields = ('username', 'password', 'date_of_birth', 'subject')
        widgets = {
            'password': forms.PasswordInput(),
            'username': forms.TextInput(attrs={
                'hx-get': reverse_lazy('check-username'),
                'hx-target': '#div_id_username',
                'hx-trigger': 'keyup[target.value.length > 3]'
            })
        }

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) <= 3:
            raise forms.ValidationError("Username is too short")
        return username

    def clean_subject(self):
        subject = self.cleaned_data['subject']
        if User.objects.filter(subject=subject).count() > 3:
            raise forms.ValidationError("There are no spaces on this course")
        return subject


    def save(self, commit=True):
        """ Hash user's password on save """
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
