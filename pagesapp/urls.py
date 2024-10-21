from django.urls import path

# from config.urls import urlpatterns
from .views import HomePageView,AboutPageView,HiPageView

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about'),
    path('hi/',HiPageView.as_view(), name = 'hi'),
]