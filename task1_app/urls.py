from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter

routers=DefaultRouter()
routers.register(r'db',views.taskViewset)


urlpatterns=[
    path('api/',views.task),
    path('upd/<int:id>/',views.update),
    path('goto/',views.goto),
    path('file/',views.file_upload)
]

urlpatterns+=routers.urls