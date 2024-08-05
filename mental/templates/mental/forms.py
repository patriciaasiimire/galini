
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Therapist
from validate_email import validate_email


# therapists for the therapists_summary
class TherapistForm(forms.ModelForm):
    class Meta:
        model = Therapist
        fields = ['name', 'specialty', 'email', 'phone']

# registration form
class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
              'required':'',
              'name':'username',
              'type':'text',
              'class':'input-box',
              'placeholder':'Username'
          })

        self.fields['email'].widget.attrs.update({
              'required': '',
              'name':"email",
              'type':"email",
              'class':'input-box',
              'placeholder':"email address"
          })

        self.fields['password1'].widget.attrs.update({
              'required': '',
              'name':"password1",
              'type':"password",
              'class':'input-box',
              'placeholder':"password"
          })
        self.fields['password2'].widget.attrs.update({
              'required': '',
              'name':"password2",
              'type':"password",
              'class':'input-box',
              'placeholder':"confirm password"
          })
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    
# appointment form
class AppointmentForm(forms.Form):
    yourname = forms.CharField(max_length=100, required=True)
    youremail = forms.EmailField(required=True)
    yourcontact = forms.CharField(max_length=100, required=True)
    yourday = forms.ChoiceField(choices=[
        ('', 'Day'),
        ('Sunday', 'Sunday'),
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
    ])
    yourtime = forms.ChoiceField(choices=[
        ('', 'Time'),
        ('9AM', '9AM'),
        ('12PM', '12PM'),
    ])
    yourdoc = forms.ChoiceField(choices=[
        ('', 'Doctor Name'),
        ('Mr.XYZ', 'Mr.XYZ'),
        ('Mr.ABC', 'Mr.ABC'),
    ])
    yourmessage = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), required=False)

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['yourname'].widget.attrs.update({
            'required': '',
            'name': 'yourname',
            'type': 'text',
            'class': 'input-box',
            'placeholder': 'Your Name',
        })
        self.fields['youremail'].widget.attrs.update({
            'required': '',
            'name': 'youremail',
            'type': 'email',
            'class': 'input-box',
            'placeholder': 'Your Email',
        })
        self.fields['yourcontact'].widget.attrs.update({
            'required': '',
            'name': 'yourcontact',
            'type': 'text',
            'class': 'input-box',
            'placeholder': 'Your Contact',
        })
        self.fields['yourday'].widget.attrs.update({
            'required': '',
            'name': 'yourday',
            'class': 'input-box',
        })
        self.fields['yourtime'].widget.attrs.update({
            'required': '',
            'name': 'yourtime',
            'class': 'input-box',
        })
        self.fields['yourdoc'].widget.attrs.update({
            'required': '',
            'name': 'yourdoc',
            'class': 'input-box',
        })
        self.fields['yourmessage'].widget.attrs.update({
            'name': 'yourmessage',
            'class': 'input-box',
            'placeholder': 'Your Message',
        })