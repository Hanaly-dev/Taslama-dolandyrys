from django import forms
from .models import*
from django.contrib.auth.models import User

class TaslamaCreateForm(forms.ModelForm):
    enjamlary = forms.ModelMultipleChoiceField(
        queryset=Enjam.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select'}),
        required=False
)
    class Meta:
        model = Taslama
        fields = '__all__'
        widgets = {
            'ady': forms.TextInput(attrs={'class': 'form-control'}),
            'müşderi': forms.Select(attrs={'class': 'form-control'}),
            'gornusi': forms.Select(attrs={'class': 'form-control'}),
            'baslanan_senesi': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'tamamlanjak_senesi': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'beyan': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'suraty': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }