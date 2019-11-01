from django import forms
from .models import Menssagens


class MenssagensForm(forms.ModelForm):
    class Meta:
        model = Menssagens
        fields = ('nome', 'email', 'assunto', 'menssagem')
        widgets = {
            'nome': forms.TextInput(attrs={'type': 'text', 'name': 'name', 'class': 'form-control', 'id': 'name', 'placeholder': 'Seu nome', 'data-rule': 'minlen:4', 'data-msg': 'Digite pelo menos 4 caracteres'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control', 'name': 'email', 'id': 'email', 'placeholder': 'Seu Email', 'data-rule': 'email', 'data-msg': 'Por favor digite um email válido'}),
            'assunto': forms.TextInput(attrs={'type': 'text', 'name': 'subject', 'class': 'form-control', 'id': 'subject', 'placeholder': 'Assunto', 'data-rule': 'minlen:4', 'data-msg': 'Digite pelo menos 8 caracteres do assunto'}),
            'menssagem': forms.Textarea(attrs={'class': 'form-control', 'name': 'message', 'rows': '5', 'data-rule': 'required', 'data-msg': 'Por favor escreva algo', 'placeholder': 'Mensagem'})
        }