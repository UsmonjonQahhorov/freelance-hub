from rest_framework.viewsets import ModelViewSet

from apps.skills.models import Skills
from apps.skills.permissions import SkillsPermission
from apps.skills.serializers import SkillsListSerializer, SkillsDetailSerializer, SkillsCreateSerializer, \
    SkillsSerializer


class SkillsViewSet(ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = [SkillsPermission]

    def get_serializer_class(self):
        if self.action == "create":
            return SkillsCreateSerializer
        elif self.action in ("update", "partial_update"):
            return SkillsDetailSerializer
        elif self.action == "list":
            return SkillsListSerializer
        elif self.action == "retrieve":
            return SkillsDetailSerializer
        return self.serializer_class
