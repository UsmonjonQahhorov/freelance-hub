from rest_framework.routers import DefaultRouter

from apps.professions.views import ProfessionsViewSet

router = DefaultRouter()
router.register('professions', ProfessionsViewSet, basename='professions')

urlpatterns = router.urls
