
from django.urls import path, include
from . import views


urlpatterns = [
    path('create',views.create, name='create'),
    path('<int:hunter_id>',views.detail, name='detail'),
    path('<int:hunter_id>/upvote',views.upvote, name='upvote'),
]
