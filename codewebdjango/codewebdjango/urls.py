from django.contrib import admin
from django.urls import path
from codewebdjango.vista import index, chat, perfil, apoyo, coins, suscripciones

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index),
    path('chat.html', chat),
    path('perfil.html', perfil),
    path('apoyo.html', apoyo), 
    path('coins.html', coins),
    path('suscripciones.html', suscripciones)
]
