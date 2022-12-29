from rest_framework.permissions import AllowAny
from rest_framework import viewsets

from twitter_api.models import TwitterUser
from twitter_api.serializers import TwitterUserSerializer


class TwitterUserViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = TwitterUser.objects.all()
    serializer_class = TwitterUserSerializer
