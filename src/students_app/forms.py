from django import forms

from students_app.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('first_name', 'age', 'phone')


class ContactUs(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    def save(self):
        from django.core.mail import send_mail
        data = self.cleaned_data
        send_mail(
            data['subject'],
            data['message'],
            data['email'],
            ['to@example.com'],  # TODO
            fail_silently=False,
        )
