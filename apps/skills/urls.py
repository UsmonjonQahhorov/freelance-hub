from rest_framework.routers import DefaultRouter

from apps.skills.views import SkillsViewSet

router = DefaultRouter()
router.register('skills', SkillsViewSet, basename='skills')

urlpatterns = router.urls
