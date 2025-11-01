from django import forms
from .models import Student
from django.core.validators import RegexValidator

class StudentForm(forms.ModelForm):
    student_id = forms.CharField(
        validators=[
            RegexValidator(
                regex=r'^\d{8}$',
                message='Student ID must be 8 digits'
            )
        ]
    )
    
    # Email field with built-in validation
    email = forms.EmailField(
        error_messages={
            'invalid': 'Please enter a valid email address'
        }
    )
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'student_id', 'password', 'course', 'email', 'goals', 'stu_year', 'modules']
        widgets = {
            'password': forms.PasswordInput(),
            'stu_year': forms.DateInput(attrs={'type': 'date'}),
            'modules': forms.CheckboxSelectMultiple(),
        }
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if len(first_name) < 2:
            raise forms.ValidationError("First name must be at least 2 characters long")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if len(last_name) < 2:
            raise forms.ValidationError("Last name must be at least 2 characters long")
        return last_name

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long")
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError("Password must contain at least one number")
        if not any(char.isupper() for char in password):
            raise forms.ValidationError("Password must contain at least one uppercase letter")
        return password

    def clean_goals(self):
        goals = self.cleaned_data.get('goals')
        if goals and len(goals) < 10:
            raise forms.ValidationError("Please provide more detailed goals (at least 10 characters)")
        return goals

    def clean(self):
        cleaned_data = super().clean()
        # Add any cross-field validations here
        return cleaned_data