# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required  # ¡Importa este decorador!
from .forms import RegistroFormulario


def register(request):
    # Si el usuario ya está autenticado, redirigirlo
    if request.user.is_authenticated:
        messages.info(
            request, "Ya has iniciado sesión. No puedes registrarte de nuevo.")
        # Redirige a la página principal del blog, o a donde prefieras
        return redirect('blog:home')

    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'¡Cuenta creada para {username}! Ahora puedes iniciar sesión.')
            return redirect('login')
    else:
        form = RegistroFormulario()
    return render(request, 'accounts/register.html', {'form': form})
