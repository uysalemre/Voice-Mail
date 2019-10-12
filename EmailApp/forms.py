from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class SendMailForm(forms.Form):
    receivers = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')
    subject = forms.CharField(max_length=100,required=False,help_text="You may provide a subject with 100 chars")
    message = forms.CharField(widget=forms.Textarea)
    file = forms.FileField(required=False)

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Send'))


class AnswerMailForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea,required=False)
    file = forms.FileField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Answer'))


class RedirectMailForm(forms.Form):
    receivers = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Redirect'))


