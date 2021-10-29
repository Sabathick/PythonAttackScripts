from django.urls import path 

from . import views

app_name = "blog"

urlpatterns = [
    path("/blog", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", view.PostDetailView.as_view(), name="detail"),
]