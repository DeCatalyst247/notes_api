from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet,get_daily_quote
from .auth_views import RegisterView,LoginView,LogoutView

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')

urlpatterns = [
    path('', include(router.urls)),
    path ('register/',RegisterView.as_view(), name='register'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('login/',LoginView.as_view(), name='login'),
    path('daily_quote/',get_daily_quote,name='daily_quote'), 
]