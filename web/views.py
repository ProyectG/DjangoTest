from django.http import HttpResponse
import datetime

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>Son las %s.</body></html>" % now
	return HttpResponse(html)


def hola_mundo(request):
	html="<html><head></head><body><center>Hola Mundo</center></body></html>"
	return HttpResponse(html)

def horas_adelante(request, offset):
	offset = int(offset)
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>En %s Horas, seran las %s</body></html>" % (offset, dt)
	return HttpResponse(html)

def index(request):
	html ="<html></body>Inicio</body></html>"
	return HttpResponse(html)
