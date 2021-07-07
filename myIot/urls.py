from django.urls import path, include
from . import views


urlpatterns = [
    path('test/<data>', views.testUpdateData, name='testUpdateData')
]