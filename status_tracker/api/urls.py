from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = "request"


urlpatterns = [
    path('api/request/', views.InstallationRequestListView.as_view()),
    path('api/request/<int:pk>/', views.InstallationRequestDetailsView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
