#from django.views import generic
from django.http import HttpResponse
from terminal_monitoring.terminal.models.site import Site


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

#	template_name = 'terminal/index.html'

#	def get_queryset(self):
#		return Terminal.objects.all()