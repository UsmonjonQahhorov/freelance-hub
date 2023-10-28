from rest_framework.routers import DefaultRouter
from .views import UserRegView
router = DefaultRouter()
router.register(r'user', UserRegView, basename='user-register')
# router.register(r'user_get-me', GetMeView, basename='user_get-me')

urlpatterns = router.urls
