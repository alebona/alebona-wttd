from django.shortcuts import render

# Create your views here.

def home(request):	
	return render(request, 'index.html')

def sobre(request):
	return render(request, 'sobre.html')

def contato(request):
	return render(request, 'contato.html')
