from apps.professions.models import Professions
from apps.professions.permissions import ProfessionPermission
from apps.professions.serializers import ProfessionsSerializer, ProfessionsCreateSerializer, \
    ProfessionsDetailSerializer, ProfessionsListSerializer
from rest_framework.viewsets import ModelViewSet


class ProfessionsViewSet(ModelViewSet):
    queryset = Professions.objects.all()
    serializer_class = ProfessionsSerializer
    permission_classes = [ProfessionPermission]

    def get_serializer_class(self):
        if self.action == "create":
            return ProfessionsCreateSerializer
        elif self.action in ("update", "partial_update"):
            return ProfessionsDetailSerializer
        elif self.action == "list":
            return ProfessionsListSerializer
        elif self.action == "retrieve":
            return ProfessionsDetailSerializer
        return self.serializer_class
