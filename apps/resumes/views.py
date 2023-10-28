from apps.resumes.models import Resumes
from rest_framework.viewsets import ModelViewSet

from apps.resumes.permissions import ResumePermission
from apps.resumes.serializers import ResumesSerializer, ResumesCreateSerializer, ResumesDetailSerializer, \
    ResumesListSerializer


class ResumeViewSet(ModelViewSet):
    queryset = Resumes.objects.all()
    serializer_class = ResumesSerializer
    permission_classes = [ResumePermission]

    def get_serializer_class(self):
        if self.action == "create":
            return ResumesCreateSerializer
        elif self.action in ("update", "partial_update"):
            return ResumesDetailSerializer
        elif self.action == "list":
            return ResumesListSerializer
        elif self.action == "retrieve":
            return ResumesDetailSerializer
        return self.serializer_class
