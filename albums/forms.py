from django import forms
from .models import Album, Details

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album 
        fields = [
            'albumtitle',
            'artistname',
            'released',
    
        ]

        widgets = {'released': forms.SelectDateWidget()
        }
        
class DetailForm(forms.ModelForm):
    class Meta:
        model = Details
        fields = ['text']
    