from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class RegistroFormulario(UserCreationForm):
    # Añadimos el campo de email con sus validaciones básicas
    email = forms.EmailField(
        required=True,
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )

    class Meta(UserCreationForm.Meta):
        # Usamos los mismos campos del UserCreationForm más el email
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

    def save(self, commit=True):
        # Llama al método save del padre para crear el usuario
        user = super().save(commit=False)
        # Asigna el email al usuario
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
