from django.urls import path
from rest_framework import routers

from twitter_api.views import TwitterUserViewset


router = routers.SimpleRouter()
router.register(r"twitter-users", TwitterUserViewset, basename="twitter-users")

urlpatterns = []

urlpatterns += router.urls