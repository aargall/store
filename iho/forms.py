from django import forms


class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()

from django import forms
from iho.models import ImageUpload


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = ('description', 'image', )

    class Preview:
        js = ('/iho/js/imagepreview.js',)