from django import forms
from .models import Base
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit



class BaseForm(forms.ModelForm):

    class Meta:
        model = Base
        fields = ('name', 'email', 'subject', 'body')


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'
        self.helper.form_class = 'base-form'
        self.helper.layout = Layout(
            'name',
            'email',
            'subject',
            'body',
            Submit('submit', 'Submit', css_class='btn-success' )
        )
