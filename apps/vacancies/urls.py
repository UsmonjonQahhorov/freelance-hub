from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.vacancies.views import VacanciesSearchAPIView, VacancyCreateViewSet, VacancyDeleteViewSet, \
    VacancyUpdateViewSet, \
    VacanciesDetailViewSet, VacancySkillDetailViewSet, VacancySkillUpdateViewSet, VacancySkillDeleteViewSet, \
    VacancySKillCreateViewSet

router = DefaultRouter()

urlpatterns = [
                  path('vacancy/search/', VacanciesSearchAPIView.as_view()),
                  path('vacancy/create/', VacancyCreateViewSet.as_view()),
                  path('vacancy/delete/<int:pk>/', VacancyDeleteViewSet.as_view()),
                  path('vacancy/update/<int:pk>/', VacancyUpdateViewSet.as_view()),
                  path('vacancy/detail/<int:pk>/', VacanciesDetailViewSet.as_view()),
                  path('vacancy-skill/create/', VacancySKillCreateViewSet.as_view()),
                  path('vacancy-skill/delete/<int:pk>/', VacancySkillDeleteViewSet.as_view()),
                  path('vacancy-skill/update/<int:pk>/', VacancySkillUpdateViewSet.as_view()),
                  path('vacancy-skill/detail/<int:pk>/', VacancySkillDetailViewSet.as_view()),
              ] + router.urls
