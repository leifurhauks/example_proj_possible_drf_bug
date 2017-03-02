from rest_framework.viewsets import ModelViewSet

from .models import Profile
from .serializers import ProfileSerializer


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects
    serializer_class = ProfileSerializer

