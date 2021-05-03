from toThumb.models import Post
from django.forms import ModelForm


class ImageForm(ModelForm):

    class Meta:
        model = Post
        fields = ['name', 'image']
