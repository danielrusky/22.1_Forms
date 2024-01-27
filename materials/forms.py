from django import forms

from materials.models import Material


class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = ('title', 'body', 'image',)