from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('detalle/<id_campeon>/',views.vista_detalle, name='detalleCampeon')
]