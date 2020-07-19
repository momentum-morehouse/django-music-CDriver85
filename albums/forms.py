from django import forms
from .models import Album, Details

class albumForm(forms.ModelForm):
    class Meta:
        model = Album 
        fields = [
            'title',
            'artist',
            'released',
    
        ]

        widgets = {'released': forms.SelectDateWidget()
        }
        
class DetailForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['text']
    