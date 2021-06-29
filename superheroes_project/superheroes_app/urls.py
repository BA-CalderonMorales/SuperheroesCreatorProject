from django.urls import path
from . import views

app_name = 'superheroes_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.detail, name='detail'),
    path('edit/<int:superhero_id>/', views.edit, name='edit'),
    path('new/', views.create, name='create')
]
