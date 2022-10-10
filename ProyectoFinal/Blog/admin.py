from django.contrib import admin
from Blog.models import Articulo, Autor , Section

# Register your models here.

admin.site.register(Articulo)
admin.site.register(Autor)
admin.site.register(Section)