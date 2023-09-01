from django.urls import path
from job import views

urlpatterns = [
     path('index/',views.index_view),
     path('development/',views.development_view),
     path('debug/',views.debug_view),
     path('hacking/',views.hacking_view),
]
