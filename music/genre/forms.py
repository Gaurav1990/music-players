from django import forms
from django.utils.translation import ugettext as _
from genre.models import Genre
from django.conf import settings

RATING = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
]

def get_genre():
    genre = []
    all_genres = Genre.objects.all()
    
    for gen in all_genres:
        genre.append((gen.name,gen.name))
    return genre


class AddSong(forms.Form):
    def __init__(self,*args,**kwargs):
        super (AddSong, self).__init__(*args,**kwargs)
        self.fields['genre'].choices = get_genre()

    title = forms.CharField(label=_("Title"), max_length=256,
                               widget=forms.TextInput(attrs={'class': 'form-control full-width',
                                                             'placeholder': 'Title of Song', 'autocomplete': 'off',
                                                             'style': 'width: 100%;'}))
    genre = forms.ChoiceField(choices=get_genre(), label=_("Genre"))
    rating = forms.ChoiceField(choices=RATING, label=_("Rating"))
    url = forms.FileField(
        label='Select a mp3 file',
        help_text='max. 42 megabytes',
        allow_empty_file=False
    )
    singer = forms.CharField(label=_("Singer"), max_length=256)
    composer = forms.CharField(label=_("composer"), max_length=256)

    def clean( self ): 
        cleaned_data = self.cleaned_data
        file = cleaned_data.get( "url" )
        file_exts = ('.mp3',) 

        if file is None:
            raise forms.ValidationError( 'Please select file first ' ) 
        if not file.content_type in settings.UPLOAD_AUDIO_TYPE: #UPLOAD_AUDIO_TYPE contains mime types of required file
            raise forms.ValidationError( 'Audio accepted only in: %s' % ' '.join( file_exts ) ) 
    
    
        return cleaned_data
class AddGenre(forms.Form):
    name = forms.CharField(label=_("Genre"), max_length=256)