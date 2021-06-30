from django.urls import path
from . import views

app_name = 'superheroes_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.detail, name='detail'),
    path('edit/', views.edit, name='edit'),
    path('update/<str:superhero_id>/', views.update, name='update'),
    path('delete/<int:superhero_id>/', views.delete, name='delete'),
    path('new/', views.create, name='create'),
]
