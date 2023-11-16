from rest_framework import routers
from .views import LocationViewSet

router = routers.SimpleRouter(trailing_slash=False)
router.register('', LocationViewSet)

urlpatterns = router.urls
