from django.urls import path
from .views import (
     PostArchivedListView,
     PostCreateView,
     PostDraftListView,
     PostListView,
     PostDetailView,
     PostUpdateView,
     PostDeleteView,
)


urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post_detail"),
    path("post/new/", PostCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", PostUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("drafts/", PostDraftListView.as_view(), name="draft_list"),
    path("archived/", PostArchivedListView.as_view(), name="archived_list"),
]