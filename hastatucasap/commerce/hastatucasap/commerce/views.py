from django.shortcuts import get_object_or_404, render
from django.views import generic
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from .models import Usuario, Producto_precio, Empresa, Clasificacion

# Create your views here.

def index(request):
	return render(request, 'index.html',)

def registro(request):
	return render(request, 'registro.html',)

def registrarse(request):
	usuario = Usuario(nombre=request.POST['nombre'],
					apellidos=request.POST['apellido'],
					email=request.POST['email'],
					password=request.POST['pass'])
	usuario.save()
	request.session['id'] = usuario.pk
	return HttpResponseRedirect(reverse('commerce:negocios'))

def login(request):
	usuario = Usuario.objects.filter(email=request.POST['email'])
	if len(usuario) > 0:
		usuario = usuario[0]
		if str(usuario.password) == str(request.POST['pass']):
			request.session['id'] = usuario.pk
			return HttpResponseRedirect(reverse('commerce:negocios'))
	return HttpResponseRedirect(reverse('commerce:index'))

def negocios(request):
	if 'id' in request.session:
		usuario = get_object_or_404(Usuario, pk=request.session['id'])
		negocios = usuario.empresa_set.all()
		return render(request, 'negocios.html',{'negocios': negocios})
	else:
		return render(request, 'index.html')

def productos(request, negocio_id):
	consulta = Producto_precio.objects.filter(empresa=Empresa.objects.filter(pk=negocio_id)[0])
	return render(request, 'productos.html', {'productos': consulta})

def logout(request):
	del(request.session['id'])
	return render(request, 'index.html')

def pedido(request):
	consulta = Clasificacion.objects.all()
	consulta2 = Empresa.objects.all()
	return render(request, 'pedido.html', {'categorias': consulta, 'empresas': consulta2})