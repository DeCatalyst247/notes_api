from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet
from.auth_views import RegisterView,LogoutView,LogoutView

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
    path ('register/',RegisterView.as_view(), name='register'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('login/',LogoutView.as_view(), name='login')
]