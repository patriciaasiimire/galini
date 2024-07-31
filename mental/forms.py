
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Therapist

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

# PHQ9 FORM
class PHQ9Form(forms.Form):
    class PHQ9Form(forms.Form):
        q1 = forms.IntegerField(min_value=0, max_value=3, label="Little interest or pleasure in doing things")
        q2 = forms.IntegerField(min_value=0, max_value=3, label="Feeling down, depressed, or hopeless")
        q3 = forms.IntegerField(min_value=0, max_value=3, label="Trouble falling or staying asleep, or sleeping too much")
        q4 = forms.IntegerField(min_value=0, max_value=3, label="Feeling tired or having little energy")
        q5 = forms.IntegerField(min_value=0, max_value=3, label="Poor appetite or overeating")
        q6 = forms.IntegerField(min_value=0, max_value=3, label="Feeling bad about yourself — or that you are a failure or have let yourself or your family down")
        q7 = forms.IntegerField(min_value=0, max_value=3, label="Trouble concentrating on things, such as reading the newspaper or watching television")
        q8 = forms.IntegerField(min_value=0, max_value=3, label="Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual")
        q9 = forms.IntegerField(min_value=0, max_value=3, label="Thoughts that you would be better off dead, or thoughts of hurting yourself in some way")

    def calculate_score(self):
        return sum(self.cleaned_data.values())

# Chatroom registration form
