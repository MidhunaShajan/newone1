from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegistrationForm(UserCreationForm):


    class Meta:
        model = User
        fields = ['username']

DEPARTMENT_CHOICES = [
    ('commerce', 'Commerce'),
    ('biology', 'Biology Science'),
    ('computer', 'Computer science'),
    ('english', 'English Literature'),
    ('humanities', 'Humanities')]
# COURSE_CHOICES = {
#     'commerce': [('accounting', 'Accounting'), ('finance', 'Finance')],
#     'biology': [('zoology', 'Zoology'), ('botany', 'Botany')],
#     'computer': [('python', 'Python')],
#     'english': [('drama', 'Drama')],
#     'humanities': [('history', 'History'), ('geography', 'Geography')]}
# COURSE_CHOICES = [('accounting', 'Accounting'), ('finance', 'Finance'),('zoology', 'Zoology'), ('botany', 'Botany'),
#     ('python', 'Python'),('drama', 'Drama'),('history', 'History'), ('geography', 'Geography')]
MATERIALS_CHOICES = [
    ('pen', 'Pen'),
    ('notebook', 'Notebook'),
    ('papers', 'Papers'),
]
class RegistrationsForm(forms.Form):
    name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    age = forms.IntegerField()
    # gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('transgender', 'Transgender')])
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],widget=forms.RadioSelect)
    phone_number = forms.CharField(max_length=10)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    course = forms.ChoiceField(choices=(
        ('Commerce', (
            ('accounting', 'Accounting'),
            ('finance', 'Finance'),
        )),
        ('Biology science', (
            ('botany', 'Botany'),
            ('zoology', 'Zoology'),
        )),
        ('Computer science', (
            ('python', 'Python'),
            ('javascript', 'Javascript'),
        )),
        ('English literature', (
            ('drama', 'Drama'),
            ('literature', 'Literature'),
        )),
        ('Humanities', (
            ('geography', 'Geography'),
            ('history', 'History'),
        )),
    ))
    purpose = forms.ChoiceField(choices=[('enquiry', 'For Enquiry'),('registration','For Registration')])
    materials_required = forms.MultipleChoiceField(choices=MATERIALS_CHOICES, widget=forms.CheckboxSelectMultiple())

    # def __init__(self, *args, **kwargs):
    #     super(RegistrationsForm, self).__init__(*args, **kwargs)
    #     initial_department = self.initial.get('department')
    #     self.fields['course'].choices = COURSE_CHOICES.get(initial_department, [])

    def save(self):
        pass



