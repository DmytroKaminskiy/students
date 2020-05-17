from django import forms

from students_app.models import Student
from students_app.tasks import send_email_async

# from students import settings  WRONG


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'age', 'phone')

    def clean_phone(self):
        value: str = self.cleaned_data['phone']

        if not value.isdigit():
            raise forms.ValidationError('Phone should contain only digits!')

        return value

    def clean(self):
        return super().clean()


class ContactUs(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def save(self):
        data = self.cleaned_data
        send_email_async.delay(data)
