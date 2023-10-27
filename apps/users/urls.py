from rest_framework.routers import DefaultRouter
from .views import UserRegView, UserLogViewSet

router = DefaultRouter()
router.register(r"user_register", UserRegView, basename="user-register")
router.register(r"user_login", UserLogViewSet, basename="user-login")
urlpatterns = router.urls
