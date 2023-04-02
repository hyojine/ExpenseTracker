from django.urls import path
from . import views


urlpatterns = [
    path('',views.TrackerView.as_view(), name='tracker_view'),
    path('<int:tracker_id>/',views.TrackerDetailView.as_view(), name='tracker_detail_view'),
]