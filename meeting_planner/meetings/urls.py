from django.urls import path, include
from . import views
urlpatterns = [
    path('<int:id>', views.detail, name="detail"),
    path('rooms', views.showRoomObjects, name='rooms'),
    path('new', views.new, name='new')
]
