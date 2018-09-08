from django import *
from .models import *

class lugar_agregar_form (forms.ModelForm):
	class Meta:
		model = Lugar
		fields= '__all__'
		
class galeria_agregar_form (forms.ModelForm):
	class Meta:
		model = Galeria
		fields= '__all__'
