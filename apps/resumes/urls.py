from rest_framework.routers import DefaultRouter
from django.urls import path
from apps.resumes.views import ResumesSearchAPIView, ResumeDetailViewSet, ResumeCreateViewSet, ResumeDeleteViewSet, \
    ResumeUpdateViewSet, ResumeSkillCreateViewSet, ResumeSKillDeleteViewSet, ResumeSkillUpdateViewSet, \
    ResumeSkillDetailViewSet, VacancyResumeDetailViewSet, VacancyResumeUpdateViewSet, VacancyResumeDeleteViewSet, \
    VacancyResumeCreateViewSet

router = DefaultRouter()
urlpatterns = [
                  path('resumes/search/', ResumesSearchAPIView.as_view()),
                  path('resumes/create/', ResumeCreateViewSet.as_view()),
                  path('resumes/delete/<int:pk>/', ResumeDeleteViewSet.as_view()),
                  path('resumes/update/<int:pk>/', ResumeUpdateViewSet.as_view()),
                  path('resumes/detail/<int:pk>/', ResumeDetailViewSet.as_view()),
                  path('resume-skill/create/', ResumeSkillCreateViewSet.as_view()),
                  path('resume-skill/delete/<int:pk>/', ResumeSKillDeleteViewSet.as_view()),
                  path('resume-skill/update/<int:pk>/', ResumeSkillUpdateViewSet.as_view()),
                  path('resume-skill/detail/<int:pk>/', ResumeSkillDetailViewSet.as_view()),
                  path('vacancy-resume/create/', VacancyResumeCreateViewSet.as_view()),
                  path('vacancy-resume/delete/<int:pk>/', VacancyResumeDeleteViewSet.as_view()),
                  path('vacancy-resume/update/<int:pk>/', VacancyResumeUpdateViewSet.as_view()),
                  path('vacancy-resume/detail/<int:pk>/', VacancyResumeDetailViewSet.as_view()),

              ] + router.urls
