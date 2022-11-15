from django.urls import path
from .views import LinksAPIView

urlpatterns = [
    path('visited_links/', LinksAPIView.as_view()),
    path('visited_domains/', LinksAPIView.as_view())
]
