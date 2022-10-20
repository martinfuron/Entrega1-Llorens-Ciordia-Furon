from django import forms

class AutorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    profesion = forms.CharField()

class ArticuloFormulario(forms.Form):
    titulo = forms.CharField()
    fecha = forms.DateField()
    texto = forms.Textarea()

class SeccionFormulario(forms.Form):
    nombre = forms.CharField()


