from django import forms
from .models import Usuario
from django.contrib.auth.hashers import make_password

class UsuarioForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput(),
        label="Contraseña",
        required=True
    )

    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        # Convertimos la contraseña en hash
        user.password_hash = make_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
