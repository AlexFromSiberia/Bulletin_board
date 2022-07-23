from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('create/', views.BbCreateView.as_view(), name='create'),
    path('<int:category_id>/', views.by_category, name='by_category'),
]
