from django.urls import path
from . import views

urlpatterns = [
    path('calc/', views.IndexView.as_view()),
    path('calc/history/', views.HistoryView.as_view()),
]