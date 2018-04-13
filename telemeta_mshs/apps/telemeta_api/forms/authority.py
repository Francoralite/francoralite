import django.forms as forms
from django.forms import ModelForm
from telemeta.models import Authority

class AuthorityForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(AuthorityForm, self).__init__(*args, **kwargs)


    class Meta:
        model = Authority
        exclude = []
