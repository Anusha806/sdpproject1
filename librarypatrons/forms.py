from django import forms
from .models import *

class BookApplicantsForm(forms.ModelForm):
    class Meta:
        model=BookApplicants
        fields=['name','email','id_document','department']
    def __init__(self,*args,**kwargs):
        super(BookApplicantsForm,self).__init__(*args,**kwargs)

