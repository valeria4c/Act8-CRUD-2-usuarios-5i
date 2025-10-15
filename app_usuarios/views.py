# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import UsuarioForm

# Lista de usuarios
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, 'index.html', {'usuarios': usuarios})

# Crear usuario
def crear_usuario(request):
    form = UsuarioForm(request.POST or None)
    if form.is_valid():
        usuario = form.save(commit=False)
        # Guardar password en password_hash (si quieres hashear aquí)
        usuario.password_hash = form.cleaned_data['password']
        usuario.save()
        return redirect('lista_usuarios')
    return render(request, 'crear.html', {'form': form})

# Editar usuario
def editar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    form = UsuarioForm(request.POST or None, instance=usuario)
    if form.is_valid():
        usuario = form.save(commit=False)
        usuario.password_hash = form.cleaned_data['password']
        usuario.save()
        return redirect('lista_usuarios')
    return render(request, 'editar.html', {'form': form, 'usuario': usuario})

# Eliminar usuario
def eliminar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuarios')
    return render(request, 'eliminar.html', {'usuario': usuario})
