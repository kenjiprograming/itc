from django import forms
from .models import ImageUpload, NippoModel

class NippoModelForm(forms.ModelForm):
    class Meta:
        model = NippoModel
        fields = "__all__"

    def __init__(self, *args, **kwards):
        for field in self.base_fields.values():
            field.widget.attrs.update({'class':'form-control'})
        super().__init__(*args, ** kwards)

class NippoFormsClass(forms.Form):
    title = forms.CharField(label='タイトル', widget=forms.TextInput(attrs={'placeholder': 'タイトル...'}))
    content = forms.CharField(label='内容', widget=forms.Textarea(attrs={'placeholder': '内容...'}))

    def __init__(self, *args, **kwards):
        for field in self.base_fields.values():
            field.widget.attrs.update({'class':'form-control'})
        super().__init__(*args, ** kwards)


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUpload
        fields = '__all__'
