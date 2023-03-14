from django.urls import path
from .views import ReportAPIView

urlpatterns = [
    path('', ReportAPIView.as_view(), name='report'),
]