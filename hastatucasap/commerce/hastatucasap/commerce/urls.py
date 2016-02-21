from django.conf.urls import url

from . import views

app_name = 'commerce'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^registro/$', views.registro, name='registro'),
	url(r'^negocios/$', views.negocios, name='negocios'),
	url(r'^productos/$', views.productos, name='productos'),
	url(r'^registrarse/$', views.registrarse, name='registrarse'),
	url(r'^login/$', views.login, name='login'),
	url(r'^logout/$', views.logout, name='logout'),
	url(r'^(?P<negocio_id>[0-9]+)/productos/$', views.productos, name='productos'),
	url(r'^pedido/$', views.pedido, name='pedido'),
]