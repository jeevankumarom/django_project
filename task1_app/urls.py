from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

routers=DefaultRouter()
routers.register(r'db',views.taskViewset)
routers.register(r'log',views.loginViewset,basename='log')

urlpatterns=[
    path('api/',views.task),
    path('upd/<int:id>/',views.update)
    
]

urlpatterns+=routers.urls