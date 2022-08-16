from django.urls import path
from .views import index, create_taks, delete_taks, update_taks, update
urlpatterns = [
    path('', index, name="index"),
    path('new/', create_taks, name="create_taks"),
    path('update', update, name='update'),
    path('update_taks/<int:taks_id>/', update_taks, name='update_taks'),
    path('delete_taks/<int:taks_id>/', delete_taks, name='delete_taks'),
]
