from django.urls import path
from . import views

urlpatterns = [
    path("", views.blog_archive, name="blog_archive"),
    path("<int:pk>/", views.blog_detail, name="blog_detail"),
]
