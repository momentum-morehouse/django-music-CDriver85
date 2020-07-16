from django import forms
from .models import Album 

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
