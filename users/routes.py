from rest_framework import routers
from users.views import UserViewSet

router = routers.SimpleRouter()
router.register(r"users", UserViewSet, basename="users")

urlpatterns = []
urlpatterns += router.urls