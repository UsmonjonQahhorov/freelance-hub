from rest_framework.routers import DefaultRouter
from .views import UserRegViewSet

router = DefaultRouter()
router.register(r"user_register", UserRegViewSet, basename="user-register")
urlpatterns = router.urls
