from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.resumes.permissions import UserPermission
from apps.vacancies.choices import VacancyStatusChoice
from apps.vacancies.models import Vacancies, VacancySkills
from apps.vacancies.serializers import VacanciesDetailSerializer, VacanciesSerializer, VacanciesCreateSerializer, \
    SearchVacancySerializer, VacancySkillSerializer


class VacanciesDetailViewSet(RetrieveAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == VacancyStatusChoice.ACTIVE.value or instance.owner == request.user:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response(data={"detail": "The resume is not active."}, status=status.HTTP_404_NOT_FOUND)


class VacancyCreateViewSet(CreateAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesCreateSerializer


class VacancyDeleteViewSet(DestroyAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer
    permission_classes = [UserPermission, AllowAny]

    def destroy(self, request, *args, **kwargs):
        try:
            resume = self.get_object()
            if resume.owner == request.user:
                self.perform_destroy(resume)
            else:
                return Response(data={"detail": "You are not the creator of this resume."},
                                status=status.HTTP_401_UNAUTHORIZED)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vacancies.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class VacancyUpdateViewSet(UpdateAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesCreateSerializer
    permission_classes = [UserPermission, AllowAny]

    def update(self, request, *args, **kwargs):
        try:
            resume = self.get_object()
            if resume.owner == request.user:
                serializer = self.get_serializer(resume, data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(data={"detail": "You are not the creator of this resume."},
                                status=status.HTTP_401_UNAUTHORIZED)
        except Vacancies.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class VacanciesSearchAPIView(ListAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = SearchVacancySerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description', 'company', 'salary_from', 'salary_to']
    permission_classes = [AllowAny]


class VacancySkillDetailViewSet(RetrieveAPIView):
    queryset = VacancySkills.objects.all()
    serializer_class = VacancySkillSerializer


class VacancySKillCreateViewSet(CreateAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesCreateSerializer


class VacancySkillDeleteViewSet(DestroyAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesSerializer
    permission_classes = [UserPermission, AllowAny]


class VacancySkillUpdateViewSet(UpdateAPIView):
    queryset = Vacancies.objects.all()
    serializer_class = VacanciesCreateSerializer
    permission_classes = [UserPermission, AllowAny]
