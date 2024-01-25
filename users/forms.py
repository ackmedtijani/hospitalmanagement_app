from django import forms

from allauth.account.forms import SignupForm


class MyCustomSignupForm(SignupForm):

    GENDER_CHOICES = [
        ('PATIENT', 'patient'),
        ('HEALTHWORKER', 'healthworker'),
    ]

    type = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select())

    def save(self, request):

        # Ensure you call the parent class's save.
        # .save() returns a User object.
        user = super(MyCustomSignupForm, self).save(request)

        # Add your own processing here.

        # You must return the original result.
        return user