from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('inicio/', views.inicio, name='inicio'),
    path('peliculas/', views.peliculas, name='peliculas'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('peliculas/crear', views.crear, name= 'crear'),
    path('peliculas/editar/<int:id>', views.editar,name= 'editar'),
    path('peliculas/form', views.form, name= 'form'),
    path('peliculas/eliminar/<int:id>', views.eliminar, name='eliminar')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)