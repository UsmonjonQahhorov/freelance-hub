from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.resumes.choices import ResumeStatusChoice
from apps.resumes.models import Resumes, ResumeSkills, VacancyResume
from apps.resumes.permissions import UserPermission
from apps.resumes.serializers import SearchResumeSerializer, ResumesSerializer, ResumesCreateSerializer, \
    ResumesDetailSerializer, ResumeSkillDetailSerializer, ResumeSkillCreateSerializer, VacancyResumeSerializer, \
    VacancyResumeCreateSerializer, ResumeSkillSerializer


class ResumeDetailViewSet(RetrieveAPIView):
    queryset = Resumes.objects.all()
    serializer_class = ResumesDetailSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.status == ResumeStatusChoice.ACTIVE.value or instance.owner == request.user:
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        else:
            return Response(data={"detail": "The resume is not active."}, status=status.HTTP_404_NOT_FOUND)


class ResumeCreateViewSet(CreateAPIView):
    queryset = Resumes.objects.all()
    serializer_class = ResumesCreateSerializer


class ResumeDeleteViewSet(DestroyAPIView):
    queryset = Resumes.objects.all()
    serializer_class = ResumesSerializer
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
        except Resumes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ResumeUpdateViewSet(UpdateAPIView):
    queryset = Resumes.objects.all()
    serializer_class = ResumesCreateSerializer
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
        except Resumes.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class ResumesSearchAPIView(ListAPIView):
    queryset = Resumes.objects.all()
    serializer_class = SearchResumeSerializer
    filter_backends = [SearchFilter]
    search_fields = ['gender', 'location', 'experience_year', 'citizenship']
    permission_classes = [AllowAny]


class ResumeSkillDetailViewSet(RetrieveAPIView):
    queryset = ResumeSkills.objects.all()
    serializer_class = ResumeSkillDetailSerializer


class ResumeSkillCreateViewSet(CreateAPIView):
    queryset = ResumeSkills.objects.all()
    serializer_class = ResumeSkillCreateSerializer


class ResumeSKillDeleteViewSet(DestroyAPIView):
    queryset = ResumeSkills.objects.all()
    serializer_class = ResumeSkillSerializer
    permission_classes = [UserPermission, AllowAny]


class ResumeSkillUpdateViewSet(UpdateAPIView):
    queryset = ResumeSkills.objects.all()
    serializer_class = ResumeSkillCreateSerializer
    permission_classes = [UserPermission, AllowAny]


class VacancyResumeDetailViewSet(RetrieveAPIView):
    queryset = VacancyResume.objects.all()
    serializer_class = VacancyResumeSerializer


class VacancyResumeCreateViewSet(CreateAPIView):
    queryset = VacancyResume.objects.all()
    serializer_class = VacancyResumeCreateSerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return super(VacancyResumeCreateViewSet, self).create(request, *args, **kwargs)


class VacancyResumeDeleteViewSet(DestroyAPIView):
    queryset = VacancyResume.objects.all()
    serializer_class = VacancyResumeSerializer
    permission_classes = [UserPermission, AllowAny]


class VacancyResumeUpdateViewSet(UpdateAPIView):
    queryset = VacancyResume.objects.all()
    serializer_class = VacancyResumeCreateSerializer
    permission_classes = [UserPermission, AllowAny]